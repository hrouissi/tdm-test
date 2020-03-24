# Copyright 2004-2016 Odoo SA (<http://www.odoo.com>)
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class CrmLead(models.Model):
    """Added the phonecall related details in the lead."""

    _inherit = "crm.lead"

    phonecall_ids = fields.One2many(
        comodel_name='crm.phonecall',
        inverse_name='opportunity_id',
        string='Phonecalls',
    )
    phonecall_count = fields.Integer(
        compute='_compute_phonecall_count',
    )

    realisedphonecall_ids = fields.One2many(
        comodel_name='voip.phonecall',
        inverse_name='partner_id',
        string='Appels effectues',
    )
    realisedphonecall_count = fields.Integer(
        compute='_compute_realisedphonecall_count',
    )

    def _compute_phonecall_count(self):
        """Calculate number of phonecalls."""
        for lead in self:
            lead.phonecall_count = self.env[
                'crm.phonecall'].search_count(
                [('opportunity_id', '=', lead.id)])

    def _compute_realisedphonecall_count(self):
        """Calculate number of realised phonecalls."""
        for lead in self:
            lead.realisedphonecall_count = self.env[
                'voip.phonecall'].search_count(
                [('partner_id', '=', lead.partner_id.id)])

    def button_open_phonecall(self):
        self.ensure_one()
        action = self.env.ref('crm_phonecall.crm_case_categ_phone_incoming0')
        action_dict = action.read()[0] if action else {}
        action_dict['context'] = safe_eval(
            action_dict.get('context', '{}'))
        action_dict['context'].update({
            'default_opportunity_id': self.id,
            'search_default_opportunity_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_duration': 1.0,
        })
        return action_dict

    def button_open_realisedphonecall(self):
        self.ensure_one()
        action = self.env.ref('crm_phonecall.crm_phonecall_report_action_log')
        action_dict = action.read()[0] if action else {}
        action_dict['context'] = safe_eval(
            action_dict.get('context', '{}'))
        action_dict['context'].update({
            'default_partner_id': self.partner_id.id,,
            'search_default_partner_id': self.partner_id.id,
            
            
        })
        return action_dict

##class VoipPhonecallrec(models.Model):
##    """Added the phonecall related details in the call voip odoo entreprise."""
##
##    _inherit = "voip.phonecall"
##
##    @api.model
##    def create(self, vals):
##        rec = super(VoipPhonecallrec, self).create(vals)
##        partner_id = vals['partner_id']
##        user_id = vals['user_id']
##        listopportunity_id = self.env['crm.lead'].search([('partner_id', '=',vals['partner_id'])])
##        opportunity_id = False
##        if listopportunity_id :
##            opportunity_id = listopportunity_id[0].id
##            
##        crmphonecall = self.env['crm.phonecall']
##        values = {
##                'name': call_summary,
##                'user_id': user_id or False,
##                'description': call.description or False,
##                'date': schedule_time,
##                'team_id': team_id or False,
##                'partner_id': call.partner_id.id or False,
##                'partner_phone': call.partner_phone,
##                'partner_mobile': call.partner_mobile,
##                'priority': call.priority,
##                'opportunity_id': call.opportunity_id.id or False,
##                
##            }
##        crmphonecall.create(values)
##
##        return rec

