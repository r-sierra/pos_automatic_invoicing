from odoo import api, fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_invoicing_auto = fields.Boolean(
        string='Automatic invoice generation',
        default=False,
        help='The invoice will automatically be generated from the Point of Sale.'
    )

    @api.onchange('module_account')
    def _onchange_module_account(self):
        super(PosConfig, self)._onchange_module_account()
        if not self.module_account:
            self.iface_invoicing_auto = False
