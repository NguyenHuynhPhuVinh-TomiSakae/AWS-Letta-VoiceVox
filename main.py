import requests
import json

# Tạo text input
text = "こんにちは、音声合成の世界へようこそ"
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Gọi API audio_query
query_params = {"text": text, "speaker": 1}
response = requests.post(
    "http://54.251.229.43:50021/audio_query",
    params=query_params
)
query_data = response.json()

# Lưu query json
with open("query.json", "w") as f:
    json.dump(query_data, f)

# Gọi API synthesis
headers = {"Content-Type": "application/json"}
response = requests.post(
    "http://54.251.229.43:50021/synthesis?speaker=1",
    headers=headers,
    json=query_data
)

# Lưu file audio
with open("audio.wav", "wb") as f:
    f.write(response.content)
