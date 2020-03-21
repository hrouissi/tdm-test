from odoo import api, fields, models, _
from odoo.exceptions import UserError

##class CrmLeadTestdrive(models.Model):
##    _name = 'crm.lead.testdrive'
##    
##    product_id =  fields.Many2one('product.product',string='Product')
##    description = fields.Text(string='Description')
##    
##    
##    lead_id = fields.Many2one('crm.lead')
##    
##    @api.onchange('product_id')
##    def onchange_product_id(self):
##        if self.product_id:
##            self.description = self.product_id.name
            

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    lead_testdrive_ids = fields.One2many('car.rental.contract','lead_id',string='Test Drive')
    testdrive_count = fields.Integer(compute='_compute_testdrive_count', string="Test Drive Count")


    
    def _compute_testdrive_count(self):
        for lead in self:
            total = 0
            for order in lead.testdrive_ids:
                                  

                    total += 1
            lead.testdrive_count = total
           
##    def _compute_testdrive_count(self):
##        count = 0
##        testdrive_ids = self.env['car.rental.contract'].search([])
##        for record in self:
##            if record:
##              testdrive_ids  
##                for testdrive_id in testdrive_ids:
##                    if record.partner_id == testdrive_id.customer_id:
##                        count=count+1 
##                        record.testdrive_count = count
##        return True


    def action_car_testdrive_contract(self):
        action = self.env.ref('fleet_rental.action_car_rental_contract').read()[0]
        action['context'] = {
            'search_default_lead_id': self.id,
            'search_default_customer_id': self.partner_id.id,
            'default_lead_id': self.id,
            'default_customer_id': self.partner_id.id
            
        }
        action['domain'] = [('lead_id', '=', self.id),('customer_id', '=', self.partner_id.id)]
        
        return action    
    
    
