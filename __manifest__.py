# -*- coding: utf-8 -*-
{
    'name': "Gestion des tournages de films",
    'summary': """
        Module pour gérer les tournages de films, les réalisateurs, les lieux et les maisons de production
    """,
    'description': """
        Ce module permet de gérer :
        - Les films
        - Les lieux de tournage
        - Les tournages
        - Les maisons de production
        - Les réalisateurs
    """,
    'author': "Groupe 2",
    'sequence': 4,
    'website': "https://www.ucad.edu.sn",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/film_views.xml',
        'views/location_views.xml',
        'views/shooting_views.xml',
        'views/production_company_views.xml',
        'views/director_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    # 'auto_install': False,
    'license': 'LGPL-3',
}