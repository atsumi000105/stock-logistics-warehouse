# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from odoo import _, models

from odoo.addons.queue_job.job import identity_exact


class StockMove(models.Model):
    _inherit = "stock.move"

    def _action_done(self, cancel_backorder=False):
        done_moves = super()._action_done(cancel_backorder=cancel_backorder)
        done_moves._prepare_auto_assign()
        return done_moves

    def _prepare_auto_assign(self):
        product_locs = defaultdict(set)
        for move in self:
            # select internal locations where we moved goods not for the
            # purpose of another move (so no further destination move)
            if move.move_dest_ids:
                continue
            product = move.product_id
            if product.type != "product":
                continue
            locations = move.mapped("move_line_ids.location_dest_id").filtered(
                lambda l: l.usage == "internal"
            )
            product_locs[product.id].update(locations.ids)

        for product_id, location_ids in product_locs.items():
            if not location_ids:
                continue
            self._enqueue_auto_assign(
                self.env["product.product"].browse(product_id),
                self.env["stock.location"].browse(location_ids),
            )

    def _enqueue_auto_assign(self, product, locations, **job_options):
        """Enqueue a job ProductProduct.moves_auto_assign()

        Can be extended to pass different options to the job (priority, ...).
        The usage of `.setdefault` allows to override the options set by default.
        """
        job_options = job_options.copy()
        job_options.setdefault(
            "description",
            _('Try reserving "{}" for quantities added in: {}').format(
                product.display_name, ", ".join(locations.mapped("name"))
            ),
        )
        # do not enqueue 2 jobs for the same product and locations set
        job_options.setdefault("identity_key", identity_exact)
        product.with_delay(**job_options).moves_auto_assign(locations)
