{
    'name': 'Mugie Custom Repair App',
    'version': '3.1.1',
    'category': 'Services/Repair',
    'summary': 'Adds expense accounts and analytic distribution fields to Repair Orders',
    'description': """
This module extends Repair Orders to:
- Specify an expense account for each repair.
- Link an analytic distribution model for reporting and allocation.
""",
    'author': 'Brian Kipkemboi Kibet',
    'website': '',
    'license': 'LGPL-3',  # TMCL is non-standard, safer to use LGPL-3 unless you need proprietary
    'depends': [
        'base',
        'account',
        'analytic',
        'repair',
        # On Enterprise, repair.order is extended by mrp_repair
        # On Community, this will just be ignored if mrp_repair is not installed
        'mrp_repair',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/custom_repair_order_rules.xml',
        'views/custom_repair_menu_views.xml',
        'views/custom_repair_form_extend.xml',
        'views/custom_repair_tree_extend.xml',
    ],
    'installable': True,
    'application': True,
}
