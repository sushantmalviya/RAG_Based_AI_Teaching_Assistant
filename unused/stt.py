from faster_whisper import WhisperModel
import json

model = WhisperModel(
    "large",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(
    "audios/output.mp3",
    language="hi",
    task="translate"
)

chunks = []
text = ""

for segment in segments:
    chunks.append(
        {
        "id": segment.id,
        "start": segment.start,
        "end": segment.end,
        "text": segment.text
        }
    )

    text += segment.text + " "



print(chunks)

with open("output.json" , "w") as f:
    json.dump(chunks,f)


