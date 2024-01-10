from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFPitBoss(models.Model):
    _name = 'rf.pb'
    _description = 'Pit Boss in RF'

    name = fields.Char(required=True)
    initial_name = fields.Char()
    location = fields.Char()