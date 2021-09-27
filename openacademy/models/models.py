# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'
    _description = 'Course'
    
    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=False)
    responsible = fields.Many2one('res.users')
    
class Session(models.Model):
    _name = 'session'
    _description = 'Session'
    
    name = fields.Char('Name', required=True)
    instructor = fields.Many2one('res.partner')
    start_date = fields.Date('Date Start', required=True)
    duration = fields.Float('Duration', help="Duration in days", required=True)
    seats = fields.Integer('Seats', help="Seats Quantity", required=False)