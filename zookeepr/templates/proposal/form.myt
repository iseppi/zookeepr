<p>
% if 'organiser' not in [x.name for x in c.signed_in_person.roles]:
<div style="display:none">
% # endif
<span class="mandatory">*</span>
<label for="proposal.title">Title:</label><br />
<% h.text_field('proposal.title', size=80) %></p>

<p>
<span class="mandatory">*</span>
<label for="proposal.proposal_type">Type:</label>
#<span class="fielddesc">What sort of proposal is this?</span>
<br />

% for st in c.proposal_types:
%   if c.proposal and c.proposal.type:
%       czeched = c.proposal.type == st
%   else:
%       czeched = False
%   #endif
<% h.radio_button('proposal.type', st.id, checked=czeched) %>
<label for="proposal.type"><% st.name |h %></label>
<br />
% #endfor

</p>


<p>
<label for="proposal.url">Project URL:</label>
<br />
<% h.text_field('proposal.url', size=80) %>
</p>

<p>
<label for="attachment">Attach a paper:</label>
<% h.file_field('attachment', size=50) %>
</p>
% if 'organiser' not in [x.name for x in c.signed_in_person.roles]:
</div>
% # endif
<p>
<span class="mandatory">*</span>
<label for="proposal.abstract">Abstract:</label>
<br />
<% h.text_area('proposal.abstract', size="80x10") %></p>

<p>
<span class="mandatory">*</span>
<label for="person.experience">Experience:</label>
<br />
<% h.text_area('person.experience', size="80x5") %></p>

<p>
<span class="mandatory">*</span>
<label for="person.bio">Bio:</label>
<br />
<% h.text_area('person.bio', size="80x5") %></p>

<p>
<span class="mandatory">*</span>
<label>Travel & Accommodation Assistance:</label>
<br />
% for ta in c.assistance_types:
%   if c.proposal and c.proposal.assistance:
%       czeched = c.proposal.assistance == ta
%   else:
%       czeched = False
%   #endif
    <% h.radio_button('proposal.assistance', ta.id, checked=czeched) %>
    <label for="proposal.assistance"><% ta.name |h %></label>
    <br />
% #endfor

<p>
<span class="mandatory">*</span>
- Mandatory field
</p>
