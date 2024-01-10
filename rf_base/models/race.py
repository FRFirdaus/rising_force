from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFRace(models.Model):
    _name = 'rf.race'
    _description = 'Races'
    
    name = fields.Char(required=True)

class RFJobClass(models.Model):
    _name = 'rf.jobclass'
    _description = 'Race Job Class'

    name = fields.Char(required=True)