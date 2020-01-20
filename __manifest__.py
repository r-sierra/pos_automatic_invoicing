# License GPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Point of Sale - Automatic Invoicing',
    'version': '12.0.1.0.0',
    'category': 'Sales/Point Of Sale',
    'sequence': 20,
    'summary': 'Automatically generate invoices from Point of Sale',
    'description': "",
    'depends': [
        'point_of_sale'
    ],
    'data': [
        'views/pos_config_view.xml',
        'static/src/xml/templates.xml',
    ],
    'installable': True,
    'author': 'Roberto Sierra',
    'website': 'https://github.com/r-sierra',
    'license': 'GPL-3',
}
