# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    accom = fields.Integer('Accommodation')
    trans = fields.Integer('Transportation')
    mobi = fields.Integer('Mobile')
    food = fields.Integer('Food')
    nature = fields.Integer('Nature Of Work')