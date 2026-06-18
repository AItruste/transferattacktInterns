import pandas as pd
import json

scores = pd.read_csv(
    "att_results/att_all_victims_scores.csv"
)

meta = pd.read_csv(
    "generated_outputs/ArcFace_subset_adv_paths.csv"
)

with open("core/verification_thresholds.json") as f:
    thresholds = json.load(f)

scores = scores.merge(
    meta[
        [
            "row_id",
            "attacker_model",
            "dataset",
            "attack_type"
        ]
    ],
    on=["row_id","dataset","attack_type"],
    how="left"
)

clean = pd.read_csv(
    "results_baseline/subset_raw_similarities_long.csv"
)

clean = clean[
    clean["attack_method"] == "clean"
]

clean = clean[
    [
        "row_id",
        "attacker_model",
        "victim_model",
        "dataset",
        "attack_type",
        "similarity"
    ]
].rename(
    columns={
        "similarity":"clean_similarity"
    }
)

merged = scores.merge(
    clean,
    on=[
        "row_id",
        "attacker_model",
        "victim_model",
        "dataset",
        "attack_type"
    ],
    how="left"
)

merged["threshold"] = merged.apply(
    lambda r:
    thresholds[r["victim_model"]][r["dataset"]]["threshold"],
    axis=1
)

def success(row):
    if row["attack_type"] == "impersonation_attack":
        return int(
            row["similarity"] >= row["threshold"]
        )
    else:
        return int(
            row["similarity"] < row["threshold"]
        )

merged["breach"] = merged.apply(
    success,
    axis=1
)

def impact(row):
    if row["attack_type"] == "impersonation_attack":
        return (
            row["similarity"]
            - row["clean_similarity"]
        )
    else:
        return (
            row["clean_similarity"]
            - row["similarity"]
        )

merged["impact"] = merged.apply(
    impact,
    axis=1
)

merged["attack_method"] = "ATT"
merged["variant"] = "att"
merged["adv_similarity"] = merged["similarity"]

merged.to_csv(
    "att_results/ATT_subset_attack_eval_long.csv",
    index=False
)

print()
print("Rows:", len(merged))
print()
print(
    "Breach Rate:",
    100*merged["breach"].mean()
)
print(
    "Impact Mean:",
    merged["impact"].mean()
)