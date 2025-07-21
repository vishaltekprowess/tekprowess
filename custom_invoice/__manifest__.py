# -*- coding: utf-8 -*-
{
    'name': "Custom Invoice",

    'summary': "Custom Invoice Layout and Features",

    'description': """
This module provides a custom invoice layout and additional features for managing invoices in Odoo.
    """,

    'author': "Tekprowess",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','web','account','l10n_in'],

    'data': [
        # 'security/ir.model.access.csv',
        "report/custom_layout.xml",
        "report/report_invoice.xml"
    ],
}

