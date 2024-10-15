# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Director(models.Model):
    _name = 'film.director'
    _description = 'Réalisateur'

    name = fields.Char(string='Nom du réalisateur', required=True)
    film_ids = fields.One2many('film.film', 'director_id', string='Films réalisés')
    film_count = fields.Integer(string='Nombre de films', compute='_compute_film_count')
    gender = fields.Selection([
        ('male', 'Homme'),
        ('female', 'Femme'),
        ('other', 'Autre'),
    ], string='Sexe')
    marital_status = fields.Selection([
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve'),
    ], string='Situation matrimoniale')
    birth_date = fields.Date(string='Date de naissance')
    age = fields.Integer(string='Âge', compute='_compute_age')

    @api.depends('film_ids')
    def _compute_film_count(self):
        for director in self:
            director.film_count = len(director.film_ids)

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for director in self:
            if director.birth_date:
                age = today.year - director.birth_date.year
                if today.month < director.birth_date.month or (today.month == director.birth_date.month and today.day < director.birth_date.day):
                    age -= 1
                director.age = age
            else:
                director.age = 0