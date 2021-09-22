# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    
    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=False)
