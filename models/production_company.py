# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class ProductionCompany(models.Model):
    _name = 'film.production.company'
    _description = 'Maison de production'

    name = fields.Char(string='Nom de la société', required=True)
    film_ids = fields.One2many('film.film', 'production_company_id', string='Films produits')
    film_count = fields.Integer(string='Nombre de films', compute='_compute_film_count')
    capital = fields.Float(string='Capital')

    @api.depends('film_ids')
    def _compute_film_count(self):
        for company in self:
            company.film_count = len(company.film_ids)