import pandas as pd
import numpy as np
from deepface import DeepFace

df = pd.read_csv(
    "generated_outputs/ArcFace_subset_adv_paths.csv"
)

victims = [
    "ArcFace",
    "Facenet512",
    "GhostFaceNet",
    "VGG-Face"
]

results = []

for victim in victims:

    print("\nVictim:", victim)

    for idx, row in df.iterrows():

        print(
            victim,
            idx + 1,
            "/",
            len(df)
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
            "dataset": row["dataset"],
            "attack_type": row["attack_type"],
            "victim_model": victim,
            "similarity": sim
        })

pd.DataFrame(results).to_csv(
    "att_results/att_all_victims_scores.csv",
    index=False
)

print("\nDONE")