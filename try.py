import requests

url = 'http://127.0.0.1:5000/test'

new_item = {'name': 'New Item', 'description': 'This is a new item'}
response = requests.post(url, json=new_item)

if response.status_code == 201:
    print('Item added successfully')
else:
    print('Error occurred')