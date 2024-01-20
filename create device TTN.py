# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 04:05:02 2024
This script demonstrate TTN device approvisionning
Python 3.11 Windows and linux work's well
@author: FSauve
"""

import requests
import json

# Credentials and all that we need to create
app_id = 'test-all'
access_key = '.......................4F4BUR4ANY.GFXCOLU22BOUARVUOOMPAE22INOOHTQBUWSTP2R3FFVPEI6GQJ2A'
dev_id = 'eui-70b3d57ed0063abd'
nwk_key = 'E5784B6171A5DAA2F1F5D8A6AB149ABD'
app_key = 'E8C54D73F451C89A1C402C49DF27DABD'

# URL de lAPI TTN V3 pour approvisionner un dispositif en ABP
# Mode ABP URL set in TTN DOC
api_url = f'https://eu1.cloud.thethings.network/api/v3/as/applications/{app_id}/devices/{dev_id}'

# Donnees du dispositif LoRaWAN
# Data to create device value to TTN
device_data = {
    "ids": {"device_id": dev_id},
    "lorawan_device": {
        "device_keys": {
            "nwk_key": nwk_key,
            "app_key": app_key
        },
        "supports_join": False,
        "mac_settings": {
            "reset_frame_counters": True
        }
    }
}

# En-têtes de la requête avec l'access key
headers = {
    'Authorization': f'Bearer {access_key}',
    'Content-Type': 'application/json'
}

# Envoi de la requête HTTP PUT pour approvisionner le dispositif
# Send HTTP request to TTN with credentials 
response = requests.put(api_url, headers=headers, data=json.dumps(device_data))

# Vérification du code de statut de la réponse
if response.status_code == 200:
    # response 200 = OK this device is create
    print(f"Dispositif {dev_id} approvisionné avec succès en mode ABP avec reset des compteurs.")
    print(response.text)
    print('--------------')
    print(' status code:', response.status_code)
else:
    # HTTP response != 200 so no creation
    print(f"Erreur lors de l'approvisionnement du dispositif. Code de statut : {response.status_code}")
    print(response.text)





