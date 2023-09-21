
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-warehouse&target_branch=16.0)
[![Pre-commit Status](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/OCA/stock-logistics-warehouse/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/OCA/stock-logistics-warehouse/branch/16.0/graph/badge.svg)](https://codecov.io/gh/OCA/stock-logistics-warehouse)
[![Translation Status](https://translation.odoo-community.org/widgets/stock-logistics-warehouse-16-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/stock-logistics-warehouse-16-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# stock-logistics-warehouse

TODO: add repo description.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_move_line_product](account_move_line_product/) | 16.0.1.0.0 |  | Displays the product in the journal entries and items
[account_move_line_stock_info](account_move_line_stock_info/) | 16.0.1.1.0 |  | Account Move Line Stock Info
[procurement_auto_create_group](procurement_auto_create_group/) | 16.0.1.0.0 |  | Allows to configure the system to propose automatically new procurement groups during the procurement run.
[scrap_reason_code](scrap_reason_code/) | 16.0.1.1.0 | [![bodedra](https://github.com/bodedra.png?size=30px)](https://github.com/bodedra) | Reason code for scrapping
[stock_demand_estimate](stock_demand_estimate/) | 16.0.1.1.0 |  | Allows to create demand estimates.
[stock_helper](stock_helper/) | 16.0.1.1.0 |  | Add methods shared between various stock modules
[stock_location_lockdown](stock_location_lockdown/) | 16.0.1.0.1 |  | Prevent to add stock on locked locations
[stock_location_position](stock_location_position/) | 16.0.1.0.0 |  | Add coordinate attributes on stock location.
[stock_location_product_restriction](stock_location_product_restriction/) | 16.0.1.0.0 | [![lmignon](https://github.com/lmignon.png?size=30px)](https://github.com/lmignon) [![rousseldenis](https://github.com/rousseldenis.png?size=30px)](https://github.com/rousseldenis) | Prevent to mix different products into the same stock location
[stock_location_zone](stock_location_zone/) | 16.0.1.0.1 |  | Classify locations with zones.
[stock_move_auto_assign](stock_move_auto_assign/) | 16.0.1.1.0 |  | Try to reserve moves when goods enter in a location
[stock_move_auto_assign_auto_release](stock_move_auto_assign_auto_release/) | 16.0.1.1.0 |  | Auto release moves after auto assign
[stock_move_common_dest](stock_move_common_dest/) | 16.0.1.0.1 |  | Adds field for common destination moves
[stock_move_location](stock_move_location/) | 16.0.1.2.0 |  | This module allows to move all stock in a stock location to an other one.
[stock_move_packaging_qty](stock_move_packaging_qty/) | 16.0.1.1.0 | [![yajo](https://github.com/yajo.png?size=30px)](https://github.com/yajo) | Add packaging fields in the stock moves
[stock_mts_mto_rule](stock_mts_mto_rule/) | 16.0.1.0.0 |  | Add a MTS+MTO route
[stock_packaging_calculator](stock_packaging_calculator/) | 16.0.1.0.1 |  | Compute product quantity to pick by packaging
[stock_picking_commercial_partner](stock_picking_commercial_partner/) | 16.0.1.0.0 |  | Add Commercial Partner on the Stock Picking
[stock_picking_procure_method](stock_picking_procure_method/) | 16.0.1.0.0 |  | Allows to force the procurement method from the picking
[stock_picking_volume](stock_picking_volume/) | 16.0.1.0.0 | [![lmignon](https://github.com/lmignon.png?size=30px)](https://github.com/lmignon) | Compute volume information on stock moves and pickings
[stock_picking_volume_packaging](stock_picking_volume_packaging/) | 16.0.1.0.0 |  | Use volume information on potential product packaging to compute the volume of a stock.move
[stock_putaway_product_template](stock_putaway_product_template/) | 16.0.1.0.0 | [![kevinkhao](https://github.com/kevinkhao.png?size=30px)](https://github.com/kevinkhao) [![sebastienbeau](https://github.com/sebastienbeau.png?size=30px)](https://github.com/sebastienbeau) | Add product template in putaway strategies from the product view
[stock_quant_cost_info](stock_quant_cost_info/) | 16.0.1.0.0 |  | Shows the cost of the quants
[stock_quant_manual_assign](stock_quant_manual_assign/) | 16.0.1.0.1 |  | Stock - Manual Quant Assignment
[stock_reserve](stock_reserve/) | 16.0.1.1.0 |  | Stock reservations on products
[stock_route_mto](stock_route_mto/) | 16.0.1.0.0 |  | Allows to identify MTO routes through a checkbox and availability to filter them.
[stock_search_supplierinfo_code](stock_search_supplierinfo_code/) | 16.0.1.0.1 |  | Allows to search for picking from supplierinfo code
[stock_storage_category_capacity_name](stock_storage_category_capacity_name/) | 16.0.1.0.0 |  | Allows to have a better display name for Stock Storage Category Capacity model
[stock_warehouse_calendar](stock_warehouse_calendar/) | 16.0.1.0.0 | [![JordiBForgeFlow](https://github.com/JordiBForgeFlow.png?size=30px)](https://github.com/JordiBForgeFlow) | Adds a calendar to the Warehouse


Unported addons
---------------
addon | version | maintainers | summary
--- | --- | --- | ---
[stock_package_type_button_box](stock_package_type_button_box/) | 16.0.1.0.0 (unported) | [![rousseldenis](https://github.com/rousseldenis.png?size=30px)](https://github.com/rousseldenis) | DEPRECATED - This module is a technical module that allows to fill in a button box for Stock Package Type form view

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
