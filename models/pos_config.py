from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_invoicing_auto = fields.Boolean(
        string='Automatic invoice generation',
        default=False,
        help='The invoice will automatically be generated from the Point of Sale.'
    )
