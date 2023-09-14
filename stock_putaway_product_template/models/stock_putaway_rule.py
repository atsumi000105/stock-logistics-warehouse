# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright 2020 Sergio Teruel - Tecnativa
# Copyright 2020 Víctor Martínez - Tecnativa

from odoo import api, fields, models


class StockPutawayRule(models.Model):
    _inherit = "stock.putaway.rule"

    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        compute="_compute_product_tmpl_id",
        store=True,
        readonly=False,
        ondelete="cascade",
    )

    @api.depends("product_id")
    def _compute_product_tmpl_id(self):
        for rec in self:
            rec.product_tmpl_id = False
            if rec.product_id:
                rec.product_tmpl_id = rec.product_id.product_tmpl_id
            else:
                params = self.env.context.get("params", {})
                if params.get("model", "") == "product.template":
                    rec.product_tmpl_id = params.get("id", False)

    def filtered(self, func):
        res = super(StockPutawayRule, self).filtered(func)
        if res or not self.env.context.get("filter_putaway_rule"):
            return res
        product = func.__closure__[0].cell_contents
        if product._name != "product.product":
            return res
        return self.with_context(filter_putaway_rule=False).filtered(
            lambda x: (
                x.product_tmpl_id == product.product_tmpl_id and not x.product_id
            )
        )
