import pandas as pd
import json

scores = pd.read_csv(
    "att_results/att_all_victims_scores.csv"
)

with open("core/verification_thresholds.json") as f:
    thresholds = json.load(f)

clean = pd.read_csv(
    "results_baseline/subset_raw_similarities_long.csv"
)

clean = clean[
    clean["attack_method"] == "clean"
]

clean = clean[
    ["row_id", "victim_model", "similarity"]
].rename(
    columns={"similarity": "clean_similarity"}
)

clean = clean.drop_duplicates(
    subset=["row_id", "victim_model"]
)

merged = scores.merge(
    clean,
    on=["row_id", "victim_model"]
)

merged["threshold"] = merged.apply(
    lambda r: thresholds[r["victim_model"]][r["dataset"]]["threshold"],
    axis=1
)

def breach(row):
    if row["attack_type"] == "impersonation_attack":
        return int(row["similarity"] >= row["threshold"])
    else:
        return int(row["similarity"] < row["threshold"])

merged["breach"] = merged.apply(
    breach,
    axis=1
)

merged["impact"] = merged.apply(
    lambda r:
    (
        r["similarity"] - r["clean_similarity"]
    )
    if r["attack_type"] == "impersonation_attack"
    else
    (
        r["clean_similarity"] - r["similarity"]
    ),
    axis=1
)

print()
print("Rows:", len(merged))
print()

print(
    "Mean Breach Rate:",
    merged["breach"].mean()
)

print(
    "Mean Impact:",
    merged["impact"].mean()
)

merged.to_csv(
    "att_results/att_all_victims_metrics.csv",
    index=False
)