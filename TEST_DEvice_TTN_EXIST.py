# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 04:15:39 2024

@author: FSauve
"""

import requests

# Remplacez ces valeurs par les informations spécifiques à votre application et votre dispositif
# app_id = 'votre_app_id'
# access_key = 'votre_access_key'
# dev_id = 'votre_dev_id'

app_id = 'test-all'
access_key = 'NNSXS.2LE6RRAOFP7EAFZ46SJEUSOAZVYMW4F4BUR4ANY.GFXCOLU22BOUARVUOOMPAE22INOOHTQBUWSTP2R3FFVPEI6GQJ2A'
dev_id = 'eui-70b3d57ed0063abd'


# URL de l'API TTN V3 pour récupérer les détails du dispositif
api_url = f'https://eu1.cloud.thethings.network/api/v3/as/applications/{app_id}/devices/{dev_id}'

# En-têtes de la requête avec l'access key
headers = {
    'Authorization': f'Bearer {access_key}',
    'Content-Type': 'application/json'
}

# Envoi de la requête HTTP GET pour récupérer les détails du dispositif
response = requests.get(api_url, headers=headers)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    print(f"Le dispositif {dev_id} existe dans l'application {app_id}.")
    device_details = response.json()
    print("Détails du dispositif:")
    print(device_details)
else:
    if response.status_code == 404:
        print(f"Le dispositif {dev_id} n'existe pas dans l'application {app_id}.")
    else:
        print(f"Erreur lors de la récupération des détails du dispositif. Code de statut : {response.status_code}")
        print(response.text)



# URL de l'API TTN V3 pour récupérer les détails du dispositif
api_url = f'https://eu1.cloud.thethings.network/api/v3/as/applications/{app_id}/devices/{dev_id}'

# En-têtes de la requête avec l'access key
headers = {
    'Authorization': f'Bearer {access_key}',
    'Content-Type': 'application/json'
}

# Envoi de la requête HTTP GET pour récupérer les détails du dispositif
response = requests.get(api_url, headers=headers)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    device_details = response.json()
    print(f"Caractéristiques du dispositif {dev_id} dans l'application {app_id}:")
    print(device_details)
else:
    print(f"Erreur lors de la récupération des détails du dispositif. Code de statut : {response.status_code}")
    print(response.text)
