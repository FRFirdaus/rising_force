import datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RFReward(models.Model):
    _name = 'rf.reward'
    _description = 'Guild Reward'
    _inherit = ['mail.thread']
    _order = 'date desc'
    
    state = fields.Selection(
        [('draft', 'Draft'),
        ('confirm', 'In Progress'),
        ('done', 'Done')], 
        tracking=True, 
        default="draft"
    )
    date = fields.Datetime(required=True, tracking=True)
    boss_ids = fields.Many2many('rf.pb', string="Pit Boss", tracking=True)
    reward_uom_id = fields.Many2one('rf.reward.uom', string="Satuan Reward", tracking=True)
    description = fields.Text(tracking=True)
    total_participants = fields.Integer(compute="_compute_total_participants")
    rf_id = fields.Many2one('rf.base', required=True, string="RF")
    auto_split = fields.Boolean(tracking=True)
    total_reward = fields.Float(tracking=True)

    line_ids = fields.One2many('rf.reward.line', 'reward_id')

    @api.onchange('total_reward', 'auto_split', 'line_ids')
    def _onchange_total_reward_split(self):
        for rec in self:
            if not rec.auto_split:
                for line in rec.line_ids:
                    line.total_reward = 0

            if rec.auto_split and rec.line_ids:
                total_line = len(rec.line_ids)
                split_reward = rec.total_reward / total_line
                for line in rec.line_ids:
                    line.total_reward = split_reward

    def action_confirm(self):
        self.write({
            "state": "confirm"
        })
    
    def action_validate(self):
        self.write({
            "state": "done"
        })

    def _compute_total_participants(self):
        for rec in self:
            total_p = 0
            if rec.line_ids:
                total_p = len(rec.line_ids)
            
            rec.total_participants = total_p
    
    def name_get(self):
        result = []
        for rec in self:
            wib_time = rec.date + datetime.timedelta(hours=7)
            result.append((rec.id, "%s (%s WIB)" % (rec.rf_id.display_name, wib_time.strftime("%d-%m-%Y %H:%M:%S"))))

        return result

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
