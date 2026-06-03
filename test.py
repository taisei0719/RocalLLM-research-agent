import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "gemma4:latest",
    "prompt": "機械読唇の実験結果のCERが0.23でした。これはどういう意味ですか？",
    "stream": False
})

print(response.json()["response"])