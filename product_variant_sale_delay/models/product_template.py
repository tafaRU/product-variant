# -*- coding: utf-8 -*-
# Copyright 2016-17 Alex Comba <alex.comba@agilebg.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'sale_delay' in vals:
            self.mapped('product_variant_ids').write(
                {'sale_delay': vals['sale_delay']})
        return res

    @api.model
    def create(self, vals):
        product_tmpl = super(ProductTemplate, self).create(vals)
        if 'sale_delay' in vals:
            product_tmpl.product_variant_ids.write(
                {'sale_delay': vals['sale_delay']})
        return product_tmpl
