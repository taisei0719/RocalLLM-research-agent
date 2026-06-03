import requests
import csv

# 事前知識ファイルを読み込む
with open("/home/nagata/1/lip_reading/lipnet/options.py") as f:
    options = f.read()

with open("/home/nagata/1/lip_reading/lipnet/model.py") as f:
    model = f.read()

# CSVを読み込む
path = "/home/nagata/1/lip_reading/lipnet/log/nagata_real_medicalABCDE_123_kana/test1.csv"

with open(path) as f:
    data = [float(row[0]) for row in csv.reader(f)]

avg_cer = sum(data) / len(data)
min_cer = min(data)
max_cer = max(data)

# システムプロンプト（事前知識）
system_prompt = f"""
あなたは機械読唇の研究支援AIエージェントです。
以下のコードを理解した上で実験結果を分析してください。

## モデル設定 (options.py)
```python
{options}
```

## モデルアーキテクチャ (model.py)
```python
{model}
```
"""

# 実験結果のプロンプト（毎回変わるデータ）
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
    "system": system_prompt,
    "prompt": prompt,
    "stream": False
})

print(response.json()["response"])