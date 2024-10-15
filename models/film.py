# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Film(models.Model):
    _name = 'film.film'
    _description = 'Film'

    name = fields.Char(string='Nom du film', required=True)
    release_date = fields.Date(string='Date de sortie')
    duration = fields.Float(string='Durée (en heures)')
    director_id = fields.Many2one('film.director', string='Réalisateur')
    location_ids = fields.Many2many('film.location', string='Lieux de tournage')
    production_company_id = fields.Many2one('film.production.company', string='Maison de production')
    film_type = fields.Selection([
        ('action', 'Action'),
        ('comedy', 'Comédie'),
        ('drama', 'Drame'),
        ('documentary', 'Documentaire'),
    ], string='Type de film')
    size = fields.Float(string='Taille (en Go)')
    selling_price = fields.Float(string='Prix de vente')
    shooting_ids = fields.One2many('film.shooting', 'film_id', string='Tournages')







