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

{
    'name': 'Project Meetings',
    'version': '8.0.1.0.0',
    'author': 'Paramjit Singh A. Sahota',
    'category': 'Project',
    'depends': ['calendar', 'project'],
    'description': """
Project Meetings
============================
Manage the meetings related to your projects.

This module is better to manage the meetings related to your projects.

This module will add 'Meetings' tab in the project form and a statinfo button to helps you create new meetings from the projects
and can track the status of existing meetings.
    """,
    'data': [
        'views/project_view.xml',
        'views/project_meetings_view.xml',
    ],
    'demo': [],
    'installable': True,
}
