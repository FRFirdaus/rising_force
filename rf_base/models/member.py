from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFMember(models.Model):
    _name = 'rf.member'
    _description = 'Member of Guild RF'
    _inherit = ['mail.thread']
    _order = 'name'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    mobile = fields.Char()
    discord = fields.Char()

    character_ids = fields.One2many('rf.character', 'member_id')

    def name_get(self):
        result = []
        for rec in self:
            characters = [char.name for char in rec.character_ids]
            result.append((rec.id, "%s (%s)" % (rec.name, ', '.join(characters))))

        return result

class RFCharacter(models.Model):
    _name = 'rf.character'

    member_id = fields.Many2one('rf.member', required=True)
    name = fields.Char(required=True, string="IGN/Nick")
    race_id = fields.Many2one('rf.race', required=True)
    class_id = fields.Many2one('rf.jobclass', required=True)
