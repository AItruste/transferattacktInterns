#!/usr/bin/env python3
"""Deep analysis of all baseline files for observations.md"""
import pandas as pd
import json

print("=" * 70)
print("SECTION 1: SUBSET INPUT PAIRS ANALYSIS")
print("=" * 70)
df = pd.read_csv("docs/subset_input_pairs.csv")
print(f"Total pairs: {len(df)}")
print(f"\nBy attack_type:")
print(df["attack_type"].value_counts().to_string())
print(f"\nBy dataset:")
print(df["dataset"].value_counts().to_string())
print(f"\nBy attack_type × dataset:")
print(df.groupby(["attack_type", "dataset"]).size().to_string())
print(f"\nRow IDs: {sorted(df['row_id'].tolist())}")
print(f"\nSample img1 paths:")
for _, r in df.head(3).iterrows():
    print(f"  row_id={r['row_id']}: {r['img1'].split('/')[-1]}")

print("\n" + "=" * 70)
print("SECTION 2: THRESHOLDS ANALYSIS")
print("=" * 70)
with open("core/verification_thresholds.json") as f:
    thresholds = json.load(f)
print(f"Models with thresholds: {list(thresholds.keys())}")
datasets = ["lfw_pairs", "celeba_pairs", "vggface2_pairs"]
print(f"\nThreshold values (FAR=0.001):")
print(f"{'Model':<15} {'lfw_pairs':>12} {'celeba_pairs':>14} {'vggface2_pairs':>16} {'GAR_lfw':>10} {'GAR_celeba':>12} {'GAR_vgg':>10}")
for model in thresholds:
    row = []
    gar_row = []
    for ds in datasets:
        if ds in thresholds[model]:
            row.append(f"{thresholds[model][ds]['threshold']:.6f}")
            gar_row.append(f"{thresholds[model][ds]['GAR']:.4f}")
        else:
            row.append("N/A")
            gar_row.append("N/A")
    print(f"{model:<15} {row[0]:>12} {row[1]:>14} {row[2]:>16} {gar_row[0]:>10} {gar_row[1]:>12} {gar_row[2]:>10}")

print("\n" + "=" * 70)
print("SECTION 3: RAW SIMILARITIES DEEP ANALYSIS")
print("=" * 70)
raw = pd.read_csv("results_baseline/subset_raw_similarities_long.csv")
print(f"Total rows: {len(raw)}")
print(f"Unique row_ids: {sorted(raw['row_id'].unique())}")
print(f"Unique attacker_models: {sorted(raw['attacker_model'].unique())}")
print(f"Unique victim_models: {sorted(raw['victim_model'].unique())}")
print(f"Unique attack_methods: {sorted(raw['attack_method'].unique())}")
print(f"Unique variants: {sorted(raw['variant'].unique())}")

# Clean similarities analysis
clean = raw[raw["attack_method"] == "clean"]
print(f"\nClean similarity rows: {len(clean)}")
print(f"\nClean similarity stats by victim model:")
for vm in sorted(clean["victim_model"].unique()):
    sub = clean[clean["victim_model"] == vm]["similarity"]
    print(f"  {vm:<15}: mean={sub.mean():.4f}, min={sub.min():.4f}, max={sub.max():.4f}, std={sub.std():.4f}")

# Clean similarities: impersonation vs dodging
print(f"\nClean similarity by attack_type (across all victims):")
for at in ["impersonation_attack", "dodging_attack"]:
    sub = clean[clean["attack_type"] == at]["similarity"]
    print(f"  {at:<25}: mean={sub.mean():.4f}, min={sub.min():.4f}, max={sub.max():.4f}")

print("\n" + "=" * 70)
print("SECTION 4: ATTACK EVAL LONG DEEP ANALYSIS")
print("=" * 70)
ev = pd.read_csv("results_baseline/subset_attack_eval_long.csv")
print(f"Total eval rows: {len(ev)}")

# Breach rate by attacker
print(f"\nBreach rate by attacker model (across all attacks):")
for am in sorted(ev["attacker_model"].unique()):
    sub = ev[ev["attacker_model"] == am]
    print(f"  {am:<15}: {100*sub['breach'].mean():.2f}% ({sub['breach'].sum()}/{len(sub)})")

# Breach rate by victim
print(f"\nBreach rate by victim model (across all attacks):")
for vm in sorted(ev["victim_model"].unique()):
    sub = ev[ev["victim_model"] == vm]
    print(f"  {vm:<15}: {100*sub['breach'].mean():.2f}% ({sub['breach'].sum()}/{len(sub)})")

# Breach rate by dataset
print(f"\nBreach rate by dataset:")
for ds in sorted(ev["dataset"].unique()):
    sub = ev[ev["dataset"] == ds]
    print(f"  {ds:<15}: {100*sub['breach'].mean():.2f}% ({sub['breach'].sum()}/{len(sub)})")

# Best and worst attacker-victim pairs
print(f"\nTop 5 attacker→victim pairs (highest breach rate):")
av = ev.groupby(["attacker_model", "victim_model"]).agg(
    breach_rate=("breach", "mean"), impact=("impact", "mean"), n=("breach", "size")
).reset_index().sort_values("breach_rate", ascending=False)
for _, r in av.head(5).iterrows():
    print(f"  {r['attacker_model']:<15} → {r['victim_model']:<15}: {100*r['breach_rate']:.1f}% breach, {r['impact']:.4f} impact (n={r['n']})")

print(f"\nBottom 5 attacker→victim pairs (lowest breach rate):")
for _, r in av.tail(5).iterrows():
    print(f"  {r['attacker_model']:<15} → {r['victim_model']:<15}: {100*r['breach_rate']:.1f}% breach, {r['impact']:.4f} impact (n={r['n']})")

# Impact analysis
print(f"\nMean impact by attack × goal:")
ig = ev.groupby(["attack_type", "attack_method"]).agg(
    impact_mean=("impact", "mean"), impact_std=("impact", "std")
).reset_index().sort_values(["attack_type", "impact_mean"], ascending=[True, False])
for _, r in ig.iterrows():
    print(f"  {r['attack_type']:<25} {r['attack_method']:<18}: mean={r['impact_mean']:.4f}, std={r['impact_std']:.4f}")

# Most breached individual pairs
print(f"\nMost consistently breached row_ids (across all attacker-victim-attack combos):")
rb = ev.groupby("row_id").agg(
    breach_rate=("breach", "mean"), attack_type=("attack_type", "first"), dataset=("dataset", "first")
).sort_values("breach_rate", ascending=False)
for rid, r in rb.head(5).iterrows():
    print(f"  row_id={rid} ({r['attack_type']}, {r['dataset']}): {100*r['breach_rate']:.1f}% breached")

print(f"\nLeast breached row_ids:")
for rid, r in rb.tail(5).iterrows():
    print(f"  row_id={rid} ({r['attack_type']}, {r['dataset']}): {100*r['breach_rate']:.1f}% breached")

print("\n" + "=" * 70)
print("SECTION 5: ATTACKER-VICTIM SUMMARY HIGHLIGHTS")
print("=" * 70)
avs = pd.read_csv("results_baseline/subset_attacker_victim_summary.csv")
# For each attacker, which victim is easiest/hardest?
for am in sorted(avs["attacker_model"].unique()):
    sub = avs[avs["attacker_model"] == am]
    best = sub.groupby("victim_model")["breach_rate_pct"].max()
    print(f"\n{am} as attacker:")
    print(f"  Easiest victim: {best.idxmax()} ({best.max():.1f}%)")
    print(f"  Hardest victim: {best.idxmin()} ({best.min():.1f}%)")
