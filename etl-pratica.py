import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))


[
  {
    "id": 4,
    "name": "Jash",
    "account": {
      "id": 7,
      "number": "00001-1",
      "agency": "0001",
      "balance": 0.0,
      "limit": 1500.0
    },
    "card": {
      "id": 4,
      "number": "**** **** **** 1111",
      "limit": 2000.0
    },
    "features": [],
    "news": [
      {
        "id": 9,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Jash, invista hoje para garantir um futuro seguro e pr\u00f3spero. Seu futuro agradece!"
      }
    ]
  },
  {
    "id": 5,
    "name": "Mel",
    "account": {
      "id": 8,
      "number": "00002-2",
      "agency": "0001",
      "balance": 0.0,
      "limit": 600.0
    },
    "card": {
      "id": 5,
      "number": "**** **** **** 2222",
      "limit": 1200.0
    },
    "features": [],
    "news": [
      {
        "id": 10,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Invista hoje para um futuro seguro e est\u00e1vel, Mel. O seu futuro financeiro depende disso!"
      }
    ]
  },
  {
    "id": 6,
    "name": "Ken",
    "account": {
      "id": 9,
      "number": "00003-3",
      "agency": "0001",
      "balance": 0.0,
      "limit": 800.0
    },
    "card": {
      "id": 6,
      "number": "**** **** **** 3333",
      "limit": 1600.0
    },
    "features": [],
    "news": [
      {
        "id": 11,
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": "Oi Ken, investir \u00e9 a chave para multiplicar seu dinheiro. N\u00e3o deixe sua grana parada!"
      }
    ]
  }
]


import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
