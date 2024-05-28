# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def write(self, vals):
        if 'workorder_ids' in self:
            self = self.with_context(force_not_replan=True)
        return super(MrpProduction, self).write(vals)

    def _plan_workorders(self, replan=False):
        force_not_replan = self.env.context.get('force_not_replan', False)
        if force_not_replan:
            replan = False
        return super()._plan_workorders(replan=replan)