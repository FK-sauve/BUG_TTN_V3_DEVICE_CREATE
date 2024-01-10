# BUG_TTN_V3_DEVICE_CREATE
BUG-TTNV3
------------------- CREATE DEVICE RESULT ----------
runfile('A:/APP/root/UPPA-TEST/create device TTN.py', 
wdir='A:/APP/root/UPPA-TEST')

Dispositif eui-70b3d57ed0063abc approvisionné avec succès en mode ABP avec reset des compteurs.
{"ids":{"device_id":"eui-70b3d57ed0063abc","application_ids":{"application_id":"test-all"}},"created_at":"2024-01-10T05:05:56.196456285Z","updated_at":"2024-01-10T05:05:56.196456285Z"}
 status code: 200

 
--------------- TEST IF device EXIST -----------   

runfile('A:/APP/root/UPPA-TEST/TEST_DEvice_TTN_EXIST.py', 

wdir='A:/APP/root/UPPA-TEST')
Le dispositif eui-70b3d57ed0063abc existe dans l'application test-all.
Détails du dispositif:
{'ids': {'device_id': 'eui-70b3d57ed0063abc', 'application_ids': {'application_id': 'test-all'}}, 'created_at': '2024-01-10T05:05:56.196456285Z', 'updated_at': '2024-01-10T05:05:56.196456285Z'}
Caractéristiques du dispositif eui-70b3d57ed0063abc dans l'application test-all:
{'ids': {'device_id': 'eui-70b3d57ed0063abc', 'application_ids': {'application_id': 'test-all'}}, 'created_at': '2024-01-10T05:05:56.196456285Z', 'updated_at': '2024-01-10T05:05:56.196456285Z'}
---------------------------------------------------
