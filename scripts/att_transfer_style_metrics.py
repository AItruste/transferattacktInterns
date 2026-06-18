import pandas as pd
import json

scores = pd.read_csv(
    "att_results/att_transfer_style_scores.csv"
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
    [
        "row_id",
        "attacker_model",
        "victim_model",
        "dataset",
        "attack_type",
        "similarity"
    ]
].rename(
    columns={"similarity": "clean_similarity"}
)

merged = scores.merge(
    clean,
    on=[
        "row_id",
        "attacker_model",
        "victim_model",
        "dataset",
        "attack_type"
    ]
)

def success(sim, threshold, attack_type):
    if attack_type == "impersonation_attack":
        return int(sim >= threshold)
    else:
        return int(sim < threshold)

def impact(clean_sim, adv_sim, attack_type):
    if attack_type == "impersonation_attack":
        return adv_sim - clean_sim
    else:
        return clean_sim - adv_sim

merged["threshold"] = merged.apply(
    lambda r:
    thresholds[r["victim_model"]][r["dataset"]]["threshold"],
    axis=1
)

merged["breach"] = merged.apply(
    lambda r:
    success(
        r["similarity"],
        r["threshold"],
        r["attack_type"]
    ),
    axis=1
)

merged["impact"] = merged.apply(
    lambda r:
    impact(
        r["clean_similarity"],
        r["similarity"],
        r["attack_type"]
    ),
    axis=1
)

merged.to_csv(
    "att_results/att_transfer_style_metrics.csv",
    index=False
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