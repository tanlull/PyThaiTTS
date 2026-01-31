from pythaitts import TTS

tts = TTS()
file = tts.tts("หากรู้สึกเจ็บแปลบ เจ็บแสบในปากจากแผลร้อนใน ดวก แถมไม่รู้ว่า", filename="tan.wav") # It will get wav file path.
#wave = tts.tts("ภาษาไทย ง่าย มาก มาก",return_type="waveform") # It will get waveform.

