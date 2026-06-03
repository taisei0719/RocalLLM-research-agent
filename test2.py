import requests
import csv

# CSVを読み込む
path = "/home/nagata/1/lip_reading/lipnet/log/nagata_real_medicalABCDE_123_kana/test1.csv"

with open(path) as f:
    data = [float(row[0]) for row in csv.reader(f)]

avg_cer = sum(data) / len(data)
min_cer = min(data)
max_cer = max(data)

# LLMに渡すプロンプト
prompt = f"""
機械読唇の実験結果です。分析してください。

データセット名: nagata_real_medicalABCDE_123_kana
文数: {len(data)}
平均CER: {avg_cer:.4f}
最小CER: {min_cer:.4f}
最大CER: {max_cer:.4f}

問題点と改善案を教えてください。
"""

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "gemma4:latest",
    "prompt": prompt,
    "stream": False
})

print(response.json()["response"])