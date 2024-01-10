from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFBase(models.Model):
    _name = 'rf.base'
    _description = 'RF Base'

    name = fields.Char(required=True, string="RF Name")
    server = fields.Char(string="Server")
    type = fields.Selection([
        ('official', 'Official'),
        ('private', 'Private')
    ])

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, "%s (%s) | %s" % (rec.name, rec.server, rec.type)))

        return result