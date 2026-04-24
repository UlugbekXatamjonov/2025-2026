

# # import requests
# # url = 'https://service.muxlisa.uz/api/v2/stt'
# # headers = {
# #     'x-api-key': 'n7mRtdlG443S1SioRLX8uF4cyMpcZcq2czynXq4U',
# # }
# # files = [
# #   ('audio', ('audio.wav', open('audio.wav', 'rb'), 'audio/wav'))
# # ]
# # payload = {}
# # response = requests.request("POST", url, headers=headers, data=payload, files=files)

# # print(response.text)




# import requests
# import sounddevice as sd
# from scipy.io.wavfile import write

# # 🎤 record
# fs = 16000
# seconds = 2

# print("🎤 Gapiring...")
# audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()
# write("audio.wav", fs, audio)

# # 🧠 send to muxlisa
# url = "https://service.muxlisa.uz/api/v2/stt"
# headers = {"x-api-key": "n7mRtdlG443S1SioRLX8uF4cyMpcZcq2czynXq4U"}

# with open("audio.wav", "rb") as f:
#     files = {"audio": ("audio.wav", f, "audio/wav")}
#     response = requests.post(url, headers=headers, files=files)

# data = response.json()
# text = data.get("result", {}).get("text", "")

# print("💬 Siz aytdingiz:", text)


import requests
import sounddevice as sd
from scipy.io.wavfile import write

# 🔐 Put your API key here
API_KEY = "n7mRtdlG443S1SioRLX8uF4cyMpcZcq2czynXq4U"

AUDIO_FILE = "audio.wav"

# 🎤 Record audio
def record_audio(seconds=3, fs=16000):
    print("🎤 Gapiring...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    write(AUDIO_FILE, fs, audio)
    print("✅ Yozib olindi")

# 🧠 Convert speech to text
def speech_to_text(audio_path):
    url = "https://service.muxlisa.uz/api/v2/stt"
    headers = {
        "x-api-key": API_KEY,
    }

    with open(audio_path, "rb") as f:
        files = {
            "audio": ("audio.wav", f, "audio/wav")
        }

        response = requests.post(url, headers=headers, files=files)

    try:
        return response.json()["result"]["text"]
    except:
        return ""

# ▶️ Run
if __name__ == "__main__":
    record_audio()
    text = speech_to_text(AUDIO_FILE)

    print("💬 Natija:", text)



import requests

url = 'https://service.muxlisa.uz/api/v2/stt'
headers = {
    'x-api-key': 'n7mRtdlG443S1SioRLX8uF4cyMpcZcq2czynXq4U',
}
files=[
  ('audio', ('audio.wav', open('/path/to/audio/file.wav', 'rb'), 'audio/wav'))
]
payload = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)