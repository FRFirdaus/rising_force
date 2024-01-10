from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFReward(models.Model):
    _name = 'rf.reward'
    _description = 'Guild Reward'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')
    ])
    date = fields.Datetime(required=True)
    boss_ids = fields.Many2many('rf.pb')
    reward_uom_id = fields.Many2one('rf.reward.uom')
    description = fields.Text()
    rf_id = fields.Many2one('rf.base')
    auto_split = fields.Boolean()
    total_reward = fields.Float()

    line_ids = fields.One2many('rf.reward.line', 'reward_id')

class RFRewardUOM(models.Model):
    _name = 'rf.reward.uom'
    _description = 'Guild Reward UoM'

    name = fields.Char(required=True)

class RFRewardLine(models.Model):
    _name = 'rf.reward.line'
    _description = 'Guild Reward details'

    reward_id = fields.Many2one('rf.reward')
    member_id = fields.Many2one('rf.member')
    character_id = fields.Many2one('rf.character')
    total_reward = fields.Float()
    is_done = fields.Boolean(string="Is Done?")
