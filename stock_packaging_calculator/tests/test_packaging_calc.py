# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo.tests import SavepointCase


class TestCalc(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.uom_unit = cls.env.ref("uom.product_uom_unit")
        cls.uom_kg = cls.env.ref("uom.product_uom_kgm")
        cls.product_a = cls.env["product.product"].create(
            {
                "name": "Product A",
                "type": "product",
                "uom_id": cls.uom_unit.id,
                "uom_po_id": cls.uom_unit.id,
            }
        )
        cls.pkg_box = cls.env["product.packaging"].create(
            {"name": "Box", "product_id": cls.product_a.id, "qty": 50}
        )
        cls.pkg_big_box = cls.env["product.packaging"].create(
            {"name": "Big Box", "product_id": cls.product_a.id, "qty": 200}
        )
        cls.pkg_pallet = cls.env["product.packaging"].create(
            {"name": "Pallet", "product_id": cls.product_a.id, "qty": 2000}
        )

    def test_calc_1(self):
        """Test easy behavior 1."""
        self.assertEqual(
            self.product_a.product_qty_by_packaging(2655),
            [(1, "Pallet"), (3, "Big Box"), (1, "Box"), (5, self.uom_unit.name)],
        )

    def test_calc_2(self):
        """Test easy behavior 2."""
        self.assertEqual(
            self.product_a.product_qty_by_packaging(350), [(1, "Big Box"), (3, "Box")]
        )

    def test_calc_3(self):
        """Test easy behavior 3."""
        self.assertEqual(
            self.product_a.product_qty_by_packaging(80),
            [(1, "Box"), (30, self.uom_unit.name)],
        )

    def test_calc_4(self):
        """Test minimal unit override."""
        self.assertEqual(
            self.product_a.product_qty_by_packaging(80, min_unit=(5, "Pack 5")),
            [(1, "Box"), (6, "Pack 5")],
        )

    def test_calc_5(self):
        """Test no minimal unit."""
        self.assertEqual(
            self.product_a.product_qty_by_packaging(80, min_unit=False), [(1, "Box")]
        )

    def test_calc_6(self):
        """Test fractional qty is lost."""
        self.assertEqual(self.product_a.product_qty_by_packaging(50.5), [(1, "Box")])
