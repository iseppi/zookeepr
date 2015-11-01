import sqlalchemy as sa

from meta import Base

from pylons.controllers.util import abort

from meta import Session

from config import Config

class Payment(Base):
    """Stores details of payments made against invoices
    """
    __tablename__ = 'payment'

    id = sa.Column(sa.types.Integer, primary_key=True)
    invoice_id = sa.Column(sa.types.Integer, sa.ForeignKey('invoice.id'), nullable=False)
    amount = sa.Column(sa.types.Integer, nullable=False)
    creation_timestamp = sa.Column(sa.types.DateTime, nullable=False, default=sa.func.current_timestamp())
    last_modification_timestamp = sa.Column(sa.types.DateTime, nullable=False, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

    def __init__(self, **kwargs):
        super(Payment, self).__init__(**kwargs)

    def __repr__(self):
        return '<Payment id=%r>' % (self.id)

    @property
    def gateway(self):
        return Config.get('gateway', 'payment')

    @property
    def gateway_url(self):
        return Config.get('gateway_url', 'payment')

    @property
    def merchant_id(self):
        return Config.get('merchant_id', 'payment')

    @property
    def transaction_reference(self):
        return Config.get('event_shortname') + ' i-' + str(self.invoice.id) + ' p-' + str(self.id)

    @property
    def transaction_type(self):
        return Config.get('default_transaction_type', 'payment')

    @property
    def securepay_fingerprint(self):
        import hashlib
        fingerprint_values = [self.merchant_id, Config.get('merchant_key', 'payment'), self.transaction_type, self.transaction_reference, str(self.amount), self.creation_timestamp_utc.strftime('%Y%m%d%H%M%S')]
        return hashlib.sha1("|".join(fingerprint_values)).hexdigest()

    @property
    def creation_timestamp_utc(self):
        from datetime import timedelta
        return self.creation_timestamp - timedelta(hours=10)

    @classmethod
    def find_all(cls):
        return Session.query(Payment).order_by(Payment.id).all()

    @classmethod
    def find_by_id(cls, id, abort_404 = False):
        result =  Session.query(Payment).filter_by(id=id).first()
        if result is None and abort_404:
            abort(404, "No such payment object")
        return result

