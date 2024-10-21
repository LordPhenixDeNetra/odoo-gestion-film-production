# Module de Gestion des Tournages de Films

Ce module Odoo permet de gérer les tournages de films, les réalisateurs, les lieux de tournage et les maisons de production.

## Développeurs du module 
 * #### Moussa THIOR
 * #### Mamadou SENE
 * #### Couly FAYE
 * #### Ndeye Khady SY

## Fonctionnalités

Le module offre les fonctionnalités suivantes :

- Gestion des films
- Gestion des lieux de tournage
- Suivi des tournages
- Gestion des maisons de production
- Gestion des réalisateurs

## Modèles

### Film

- Nom
- Date de sortie
- Durée
- Réalisateur
- Lieux de tournage
- Maison de production
- Type de film
- Taille (en Go)
- Prix de vente

### Lieu de tournage

- Nom
- Films tournés
- Nombre de films tournés

### Tournage

- Numéro de tournage
- Date de début
- Date de fin
- Durée du tournage
- Film tourné

### Maison de production

- Nom
- Liste des films produits
- Nombre de films
- Capital

### Réalisateur

- Nom
- Films réalisés
- Nombre de films
- Sexe
- Situation matrimoniale
- Date de naissance
- Âge

## Installation

1. Copiez le dossier `film_production` dans le répertoire `addons` de votre installation Odoo.
2. Mettez à jour la liste des applications dans Odoo.
3. Recherchez "Gestion des tournages de films" dans la liste des applications et cliquez sur "Installer".

## Utilisation

Après l'installation, vous trouverez un nouveau menu "Production de Films" dans le menu principal d'Odoo. Ce menu contient des sous-menus pour accéder à chaque modèle :

- Films
- Lieux de tournage
- Tournages
- Maisons de production
- Réalisateurs

## Personnalisation

Vous pouvez personnaliser ce module en modifiant les fichiers de vue XML ou en étendant les modèles Python.

## Support

Pour toute question ou problème, veuillez créer une issue sur le dépôt du projet ou contacter l'équipe de développement.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à forker le projet et à soumettre vos pull requests.

## Licence

Ce module est sous licence LGPL-3.0. Voir le fichier `LICENSE` pour plus de détails.






