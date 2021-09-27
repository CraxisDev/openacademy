# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'
    _description = 'Course'
    
    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=False)
    
class Session(models.Model):
    _name = 'session'
    _description = 'Session'
    
    name = fields.Char('Name', required=True)
    start_date = fields.Char('Date Start', required=True)
    duration = fields.Float('Duration', help="Duration in days", required=True)
    seats = fields.Integer('Seats', help="Seats Quantity", required=False)