# BUG_TTN_V3_DEVICE_CREATE
'''BUG-TTNV3
------------------- CREATE DEVICE RESULT ----------
runfile('A:/APP/root/UPPA-TEST/create device TTN.py', 
wdir='A:/APP/root/UPPA-TEST')

Dispositif eui-70b3d57ed0063abc approvisionné avec succès en mode ABP avec reset des compteurs.
{"ids":{"device_id":"eui-70b3d57ed0063abc","application_ids":{"application_id":"test-all"}},"created_at":"2024-01-10T05:05:56.196456285Z","updated_at":"2024-01-10T05:05:56.196456285Z"}
 status code: 200'''

Not seen in TTN console
 ![image](https://github.com/FK-sauve/BUG_TTN_V3_DEVICE_CREATE/assets/126117269/8c5aa853-7121-4872-b8d9-6677ff43e033)
But Created In TTN:
![image](https://github.com/FK-sauve/BUG_TTN_V3_DEVICE_CREATE/assets/126117269/d4c2f362-83b1-47cd-94d2-6adc063c65ed)
 
'''--------------- TEST IF device EXIST -----------'''   
'''
runfile('A:/APP/root/UPPA-TEST/TEST_DEvice_TTN_EXIST.py', 
Return FOM TTN as exist:

wdir='A:/APP/root/UPPA-TEST')
Le dispositif eui-70b3d57ed0063abc existe dans l'application test-all.
Détails du dispositif:
{'ids': {'device_id': 'eui-70b3d57ed0063abc', 'application_ids': {'application_id': 'test-all'}}, 'created_at': '2024-01-10T05:05:56.196456285Z', 'updated_at': '2024-01-10T05:05:56.196456285Z'}
Caractéristiques du dispositif eui-70b3d57ed0063abc dans l'application test-all:
{'ids': {'device_id': 'eui-70b3d57ed0063abc', 'application_ids': {'application_id': 'test-all'}}, 'created_at': '2024-01-10T05:05:56.196456285Z', 'updated_at': '2024-01-10T05:05:56.196456285Z'}
---------------------------------------------------'''


