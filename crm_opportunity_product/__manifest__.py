# -*- encoding: utf-8 -*-
{
	"name": "CRM Opportunity Product Test Drive",
	"version": "13.0",
	"author": "TNC",
	"website": "http://tnc.agency",
	"sequence": 1,
	"depends": [
		"base",'sale_crm','sale','product','fleet_rental'
	],
	"category": "Settings",
	"complexity": "easy",
	"description": """
	This  module allow to add products on opportunity and create quote with that ! . 
	""",
	"data": [
		'security/ir.model.access.csv',
		'views/opportunity_product.xml',
	],
	"demo": [
	],
	"test": [
	],
	"auto_install": False,
	"installable": True,
	"application": False,
    'images': ['static/description/banner.png'],



        
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
