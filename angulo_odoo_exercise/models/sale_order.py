# -*- coding: utf-8 -*-

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_orderlines_for_report(self):
        line_dic = {}
        for line in self.order_line:
            if line.product_id.categ_id in line_dic:
                line_dic[line.product_id.categ_id].append(line)
            else:
                line_dic[line.product_id.categ_id] = [line]
        return line_dic

