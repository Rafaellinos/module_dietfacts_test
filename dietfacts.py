# Dietfacts application
from openerp import models, fields, api

# Extend product.template model with calories

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer(string=u'Calories')
    serving_size = fields.Float(string=u'Serving Size')
    last_updated = fields.Date(string=u'Last Update')
    is_diet_item = fields.Boolean(string=u'Diet Item')
    nutrient_ids = fields.One2many(
        comodel_name='product.template.nutrient',
        inverse_name='product_id',
        string=u'Nutrients')

    @api.one
    @api.depends('nutrient_ids','nutrient_ids.value','nutrition_score')
    def _cal_score(self):
        currentscore = 0
        sodium = self.env['product.nutrient'].search([('name','=','Sodium')], limit=1).id
        protein = self.env['product.nutrient'].search([('name','=','Protein')], limit=1).id

        for nutrient in self.nutrient_ids:
            if nutrient.nutrient_id == sodium:
                currentscore = currentscore + (nutrient.value * 5)
            elif nutrient.nutrient_id == protein:
                currentscore = currentscore + (nutrient.value / 5)
            else:
                currentscore = currentscore + nutrient.value
        self.nutrition_score = currentscore
         

    nutrition_score = fields.Float(
        string=u'Score',
        store=True,
        compute='_cal_score')

# Create new model to keep the meal saved

class Dietfacts_res_users_meal(models.Model):
    _name = 'res.users.meal'

    name = fields.Char(string=u'Meal Name')
    meal_date = fields.Datetime(string=u'Menu Date')
    item_ids = fields.One2many(
        comodel_name='res.users.mealitem',
        inverse_name='meal_id',
        string=u'Items List')

    @api.one # Tell Odoo when to call the method
    @api.depends('item_ids','item_ids.servings') #When field change, recalculate

    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
        self.totalcalories = currentcalories

    totalcalories = fields.Integer(
        string=u'Total Meal Calories',
        store=True,
        compute="_calccalories")
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Meal Users')
    notes = fields.Text(string=u'Meal Notes')

# Create a model fot the field item_ids, that will contains the products list

class Dietfacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'

    meal_id = fields.Many2one(
        comodel_name='res.users.meal',
        string=u'Meal ID')
    item_id = fields.Many2one(
        comodel_name='product.template',
        string=u'Item ID')
    servings = fields.Float(
        string=u'Servings',
        default=1)
    calories = fields.Integer(
        related='item_id.calories',
        string=u'Calories Serving',
        store=True,
        readonly=True)
    notes = fields.Text(string=u'Meal item notes')

# Model to products nutrients uom

class Dietfacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    
    name = fields.Char(string=u'Nutrient Name')
    uom_id = fields.Many2one(
        comodel_name='product.uom',
        string=u'Unit of Mesure')
    description = fields.Text(string=u'Description')

class Dietfacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'

    nutrient_id = fields.Many2one(
        comodel_name='product.nutrient', 
        string=u'Product Nutrient')
    product_id = fields.Many2one(
        comodel_name='product.template',
        string=u'ID do Produto')
    uom = fields.Char(
        related='nutrient_id.uom_id.name', 
        string=u'Uom',
        readonly=True)
    value = fields.Float(string=u'Nutrient Value')
    dailypercent = fields.Float(string=u'Daily Recommended Value')
