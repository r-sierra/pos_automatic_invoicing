odoo.define('pos_automatic_invoicing.pos_automatic_invoicing', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    // Overload 'set_to_invoice' function. Always set true if automatic
    // invoicing is enabled
    var _set_to_invoice_ = models.Order.prototype.set_to_invoice;
    models.Order.prototype.set_to_invoice = function(to_invoice) {
      _set_to_invoice_.call(this, to_invoice);
      if(this.pos.config.iface_invoicing_auto) {
        this.to_invoice = true;
      }
    };

    // Overload 'is_to_invoice' function. Always return true if automatic
    // invoicing is enabled
    var _is_to_invoice_ = models.Order.prototype.is_to_invoice;
    models.Order.prototype.is_to_invoice = function() {
      if(this.pos.config.iface_invoicing_auto) {
        return true;
      } else {
        return _is_to_invoice_.call(this);
      }
    };
});
