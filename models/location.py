# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Location(models.Model):
    _name = 'film.location'
    _description = 'Lieu de tournage'

    name = fields.Char(string='Nom du lieu', required=True)
    film_ids = fields.Many2many('film.film', string='Films tournés')
    film_count = fields.Integer(string='Nombre de films tournés', compute='_compute_film_count')

    @api.depends('film_ids')
    def _compute_film_count(self):
        for location in self:
            location.film_count = len(location.film_ids)