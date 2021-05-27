import requests

key = "secret_erKXuLKqnAPHFbS6kx9TB5XqV6SHm2h53O7GkwZyuBa"
db_key = "7c662f74975c43279416b0fc17eb0bca"


url = "127.0.0.1:3030"
params = {"Authorization": "Bearer " + key , 
  		  "Notion-Version": "2021-05-13",
  		  "Content-Type" : "application.json",
  		  "data" : "{}"}

print(url)
print(params)
print(requests.get(url, params).text)