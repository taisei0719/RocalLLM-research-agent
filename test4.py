import requests
import base64

# 画像を読み込んでbase64にエンコード
with open("/home/nagata/ensyuu/image.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "gemma4:latest",
    "prompt": "この画像に含まれる回路図を詳しく解説してください。回路の構成要素、信号の流れ、全体的な役割を説明してください。",
    "images": [image_b64],
    "stream": False
})

print(response.json()["response"])