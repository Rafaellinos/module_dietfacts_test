# Dietfacts application
from openerp import models, fields

# Extebd product.template model with calories

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer(string=u'Calories')
