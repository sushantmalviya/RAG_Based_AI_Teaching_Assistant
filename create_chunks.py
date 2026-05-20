from faster_whisper import WhisperModel
import json
import os

model = WhisperModel(
    "large",
    device="cpu",
    compute_type="int8"
)

audios = os.listdir("audios")

for audio in audios:
    vid_no = audio.split("-")[0]
    vid_name = audio.split("-",1)[1].split(".")[0]

    print(vid_name,vid_no)
    segments, info = model.transcribe(
        f"audios/{audio}",
        language="hi",
        task="translate"
    )
    chunks = []
    whole_text = ""

    for segment in segments:
        chunks.append(
            {
            "number": vid_no,
            "title" : vid_name,
            "id": segment.id,
            "start": segment.start,
            "end": segment.end,
            "text": segment.text
            }
        )

        whole_text += segment.text + " "

    chunks_with_metadata = {"chunks": chunks, "text" : whole_text}


    with open(f"jsons/{audio}.json" , "w") as f:
        json.dump(chunks_with_metadata,f)