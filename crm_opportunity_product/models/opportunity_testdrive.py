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



    
    
    
