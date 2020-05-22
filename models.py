# -*- coding: utf-8 -*-

from openerp import models,api
class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def auto_unpublish_product(self):
        self.search([
            ('qty_available', '<=', 0)]).write({'web_published': False})



    @api.model
    def auto_publish_product(self):
        self.search([
            ('qty_available', '>=', 1)]).write({'web_published': True})