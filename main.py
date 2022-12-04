
import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()  
    
