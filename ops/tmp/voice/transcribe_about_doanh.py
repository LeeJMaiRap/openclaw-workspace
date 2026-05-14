from faster_whisper import WhisperModel

model = WhisperModel('small', compute_type='int8')
segments, info = model.transcribe('/root/.openclaw/workspace/tmp/voice/about-doanh.ogg', language='vi')
print('LANG:', info.language)
print('PROB:', info.language_probability)
print('---TRANSCRIPT---')
for segment in segments:
    print(segment.text.strip())
