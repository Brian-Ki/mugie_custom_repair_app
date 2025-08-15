{
    'name': 'Mugie Custom Repair App',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Custom features for adding expense accounts and analytic accounting to repair orders',
    'description': """This module extends repair orders to specify expense accounts and analytic distribution
        that will be used in the accounting entries generated from repairs""",
    'author': 'Brian Kipkemboi Kibet',
    'depends': ['base', 'repair',],
    'website': '',
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/repair_form_extend.xml',
        'views/repair_tree_extend.xml',



    ],


    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
}
