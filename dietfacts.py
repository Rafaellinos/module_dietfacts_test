# Dietfacts application
from openerp import models, fields

# Extend product.template model with calories

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer(string=u'Calories')
    serving_size = fields.Float(string=u'Serving Size')
    last_updated = fields.Date(string=u'Last Update')
    is_diet_item = fields.Boolean(string=u'Diet Item')

class Dietfacts_res_users_meal(models.Model):
    _name = 'res.users.meal'

    name = fields.Char(string=u'Meal Name')
    meal_date = fields.Datetime(string=u'Menu Date')
    item_ids = fields.One2many(
        comodel_name='res.users.mealitem',
        inverse_name='meal_id',
        string=u'Items List')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Meal Users')
    notes = fields.Text(string=u'Meal Notes')

class Dietfacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'

    meal_id = fields.Many2one(
        comodel_name='res.users.meal'
        string=u'Meal ID')
    item_id = fields.Many2one(
        comodel_name='product.template',
        string=u'Item ID')
    servings = fields.Float(string=u'Servings')
    notes = fields.Text(string=u'Meal item notes')