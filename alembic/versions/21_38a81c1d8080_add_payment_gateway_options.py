"""add_payment_gateway_options

Revision ID: 38a81c1d8080
Revises: 58ee75910929
Create Date: 2015-10-27 21:46:33.566968

"""

# revision identifiers, used by Alembic.
revision = '38a81c1d8080'
down_revision = '58ee75910929'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("INSERT INTO config (category, key, value, description) VALUES ('payment', 'gateway', '\"securepay\"', 'The enabled payment gateway. Can be one of (securepay)')")
    op.execute("INSERT INTO config (category, key, value, description) VALUES ('payment', 'gateway_url', '\"https://payment.securepay.com.au/test/v2/invoice\"', 'The URL for the payment gateway. (For SecurePay, Test is https://payment.securepay.com.au/test/v2/invoice and Live is https://payment.securepay.com.au/live/v2/invoice)')")
    op.execute("INSERT INTO config (category, key, value, description) VALUES ('payment', 'merchant_id', '\"TST001\"', 'The merchant ID as supplied by your payment gateway')")
    op.execute("INSERT INTO config (category, key, value, description) VALUES ('payment', 'default_transaction_type', '\"4\"', 'The transaction type as required by your payment gateway. (For SecurePay 0 for Payment, 1 for Pre-Auth, 2 for Payment with FraudGuard, 3 for Pre-Auth with FraudGuard, 4 for Payment with 3D-Secure, 5 for Pre-Auth with 3D-Secure, 6 for Payment with FraudGuard and 3D-Secure and 7 for Pre-Auth with FraudGuard and 3D-Secure')")
    op.execute("INSERT INTO config (category, key, value, description) VALUES ('payment', 'merchant_key', '\"somethingsecure\"', 'The merchant key as supplied by your payment gateway')")

def downgrade():
    op.execute("DELETE FROM config WHERE category='payment' AND key='gateway'")
    op.execute("DELETE FROM config WHERE category='payment' AND key='gateway_url'")
    op.execute("DELETE FROM config WHERE category='payment' AND key='merchant_id'")
    op.execute("DELETE FROM config WHERE category='payment' AND key='default_transaction_type'")
    op.execute("DELETE FROM config WHERE category='payment' AND key='merchant_key'")
