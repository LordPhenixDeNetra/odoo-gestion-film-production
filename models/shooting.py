# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Shooting(models.Model):
    _name = 'film.shooting'
    _description = 'Tournage'

    name = fields.Char(string='Numéro de tournage', required=True)
    start_date = fields.Date(string='Date de début')
    end_date = fields.Date(string='Date de fin')
    duration = fields.Float(string='Durée du tournage (en jours)', compute='_compute_duration')
    film_id = fields.Many2one('film.film', string='Film tourné')

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for shooting in self:
            if shooting.start_date and shooting.end_date:
                delta = shooting.end_date - shooting.start_date
                shooting.duration = delta.days
            else:
                shooting.duration = 0