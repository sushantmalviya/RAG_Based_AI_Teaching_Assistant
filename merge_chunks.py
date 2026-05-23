import json 
import math
import os 

n = 7

for filename in os.listdir("jsons"):
    file_path = os.path.join("jsons", filename)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        new_chunks =[]
        num_chunks = len(data["chunks"])
        new_num_chunks = math.ceil(num_chunks/n)

        for i in range(new_num_chunks):
            start_idx = i*n
            end_idx = min((i+1)*n, num_chunks)
            chunk_group = data["chunks"][start_idx:end_idx]

            new_chunks.append(
                {
                    "number" : chunk_group[0]["number"],
                    "title" : chunk_group[0]["title"],
                    "start" : chunk_group[0]["start"],
                    "end" : chunk_group[-1]["end"],
                    "text" : " ".join([c["text"] for c in chunk_group])
                }
            )

        os.makedirs("new_jsons", exist_ok=True)
        with open(os.path.join("new_jsons",filename), "w", encoding="utf-8") as json_file:
            json.dump({
                "chunks" : new_chunks,
                "text" : data["text"],
            }, 
            json_file, indent= 4)
 