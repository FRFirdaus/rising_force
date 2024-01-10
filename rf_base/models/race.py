from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFRace(models.Model):
    _name = 'rf.race'
    name = fields.Char(required=True, string="IGN/Nick")

class RFJobClass(models.Model):
    _name = 'rf.jobclass'

    name = fields.Char(required=True, string="IGN/Nick")