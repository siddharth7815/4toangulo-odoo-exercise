# -*- coding: utf-8 -*-

{
    'name': 'Sales Report Enhancement',
    'version': '1.1.0',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
        This module contains adding product's category as a section in quotation and order report.
    """,
    'depends': ['sale_management'],
    'data': [
        "views/sale_order_view.xml",
        "report/sale_report_templates.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False
}
