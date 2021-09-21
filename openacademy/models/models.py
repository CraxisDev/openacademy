# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy.course'
    
    name = fields.Char()
    description = fields.Text()
    free = fields.Boolean()