# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models
from odoo.tools import float_compare


class Product(models.Model):
    _inherit = "product.product"

    def product_qty_by_packaging(self, prod_qty, min_unit=None):
        """Calculate quantity by packaging.

        Limitation: fractional quantities are lost.

        :prod_qty: total qty to satisfy.
        :min_unit: minimal unit of measure as a tuple (qty, name).
                   Default: to UoM unit.
        :returns: list of tuple in the form [(qty_per_package, package_name)]

        """
        packagings = [(x.qty, x.name) for x in self.packaging_ids]
        if min_unit is None:
            # You can pass `False` to skip it.
            single_unit = self.uom_id
            min_unit = (single_unit.factor, single_unit.name)
        if min_unit:
            packagings.append(min_unit)
        return self._product_qty_by_packaging(
            sorted(packagings, reverse=True), prod_qty
        )

    def _product_qty_by_packaging(self, pkg_by_qty, qty):
        """Produce a list of tuple of packaging qty and packaging name."""
        # TODO: refactor to handle fractional quantities (eg: 0.5 Kg)
        res = []
        for pkg_qty, pkg in pkg_by_qty:
            qty_per_pkg, qty = self._qty_by_pkg(pkg_qty, qty)
            if qty_per_pkg:
                res.append((qty_per_pkg, pkg))
            if not qty:
                break
        return res

    def _qty_by_pkg(self, pkg_qty, qty):
        """Calculate qty needed for given package qty."""
        qty_per_pkg = 0
        while float_compare(qty - pkg_qty, 0.0, precision_digits=3) >= 0.0:
            qty -= pkg_qty
            qty_per_pkg += 1
        return qty_per_pkg, qty
