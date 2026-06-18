import pandas as pd
import json

scores = pd.read_csv(
    "att_results/att_arcface_scores.csv"
)

with open("core/verification_thresholds.json") as f:
    thresholds = json.load(f)

clean = pd.read_csv(
    "results_baseline/subset_raw_similarities_long.csv"
)

clean = clean[
    (clean["attack_method"] == "clean")
    &
    (clean["victim_model"] == "ArcFace")
]

clean = clean[
    ["row_id", "similarity"]
].rename(
    columns={"similarity": "clean_similarity"}
)
clean = clean.drop_duplicates(subset=["row_id"])

merged = scores.merge(
    clean,
    on="row_id"
)

merged["threshold"] = merged["dataset"].apply(
    lambda d: thresholds["ArcFace"][d]["threshold"]
)

merged["breach"] = (
    merged["similarity"] >= merged["threshold"]
).astype(int)

merged["impact"] = (
    merged["similarity"]
    - merged["clean_similarity"]
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

print()
print(
    merged[
        [
            "row_id",
            "similarity",
            "clean_similarity",
            "threshold",
            "breach",
            "impact"
        ]
    ].head()
)

merged.to_csv(
    "att_results/att_arcface_metrics.csv",
    index=False
)
merged.to_csv(
    "att_results/att_arcface_metrics.csv",
    index=False
)