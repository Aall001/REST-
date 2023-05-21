#GET
import requests

status = 'available'
# r = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
#                  headers= {'accept': 'application/json'})

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})
print('GET-запрос, код статус', res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

print("-------------")


#POST

url = 'https://petstore.swagger.io/v2/user'
headers = {'accept': 'application/json', 'Content-Type': 'applicayion/json'}
data = {
"id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
r = requests.post(url, headers= headers, json= data)

print("POST-запрос, код статус", r.status_code)
print(r.text)
print(r.json())

print("----------")


#DELETE

username = 'available'
url = f'https://petstore.swagger.io/v2/user/{username}'
headers = {'accept': 'application/json'}

r = requests.delete(url, )

print('Удаляем пользователя, код статус', r.status_code)
print(r.text)
print("------------")

#PUT

username = 'available'
url = f'https://petstore.swagger.io/v2/user/{username}'
header = {'accept': 'application/json', 'Content-Type': 'applicayion/json'}
data_change = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
r = requests.put(url, headers= header, json= data_change)

print('Изменяем данные пользователя, код статус', r.status_code)
print(r.text)
