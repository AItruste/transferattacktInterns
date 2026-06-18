import pandas as pd
import numpy as np
from deepface import DeepFace

VICTIMS = [
    "ArcFace",
    "Facenet512",
    "GhostFaceNet",
    "VGG-Face",
]

df = pd.read_csv(
    "att_results/all_attacker_att_paths.csv"
)

results = []

for victim in VICTIMS:

    print()
    print("Victim:", victim)
    print()

    for idx, row in df.iterrows():

        print(
            f"{victim} : {idx+1}/{len(df)}",
            end="\r"
        )

        adv_img = row["att_path"]

        target_img = row["img2"].replace(
            "/content/face_module/dataset_extractedfaces/",
            "dataset_extractedfaces\\"
        )

        adv_emb = DeepFace.represent(
            img_path=adv_img,
            model_name=victim,
            enforce_detection=False
        )[0]["embedding"]

        tgt_emb = DeepFace.represent(
            img_path=target_img,
            model_name=victim,
            enforce_detection=False
        )[0]["embedding"]

        adv_emb = np.array(adv_emb)
        tgt_emb = np.array(tgt_emb)

        sim = np.dot(
            adv_emb,
            tgt_emb
        ) / (
            np.linalg.norm(adv_emb)
            *
            np.linalg.norm(tgt_emb)
        )

        results.append({
            "row_id": row["row_id"],
            "attacker_model": row["attacker_model"],
            "dataset": row["dataset"],
            "attack_type": row["attack_type"],
            "victim_model": victim,
            "attack_method": "ATT",
            "similarity": sim
        })

pd.DataFrame(results).to_csv(
    "att_results/att_transfer_style_scores.csv",
    index=False
)

print()
print("DONE")