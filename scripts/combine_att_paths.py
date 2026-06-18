import pandas as pd

files = [
    "generated_outputs/ArcFace_subset_adv_paths.csv",
    "generated_outputs/Facenet512_subset_adv_paths.csv",
    "generated_outputs/GhostFaceNet_subset_adv_paths.csv",
    "generated_outputs/VGG-Face_subset_adv_paths.csv",
]

dfs = [pd.read_csv(f) for f in files]

combined = pd.concat(dfs, ignore_index=True)

combined.to_csv(
    "att_results/all_attacker_att_paths.csv",
    index=False
)

print("Rows:", len(combined))