# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY Odoo S.A. <http://www.odoo.com>
#    @author Paramjit Singh A. Sahota <sahotaparamjitsingh@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    project_id = fields.Many2one('project.project', 'Project')


class Project(models.Model):

    _inherit = "project.project"

    @api.one
    def _project_meeting_count(self):
        self.project_meeting_count = self.env['calendar.event'].search_count(
            [('project_id', 'in', self.ids)])

    calendar_events = fields.One2many(
        'calendar.event', 'project_id', string='Meetings')
    project_meeting_count = fields.Integer(
        compute="_project_meeting_count", string="Meetings")
