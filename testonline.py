import requests

response = requests.get('http://10.100.0.62:5000/check_connection')
if response.status_code == 200:
    data = response.json()
    if data['status'] == 'online':
        print('Server is online')
else:
    print('Server is not reachable')