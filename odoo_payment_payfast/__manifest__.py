# -*- coding: utf-8 -*-

{
    'name': 'PayFast',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Paypal Implementation',
    'version': '2.0',
    'description': """PayFast Payment Acquirer""",
    'author': "Magnesium Tech",
    "price": 35.00,
    "currency": "USD"
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_paypal_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'post_init_hook': 'create_missing_journal_for_acquirers',
}
