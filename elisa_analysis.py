"""
elisa_analysis.py

Reads raw OD450 ELISA plate data, calculates the assay cut-off from the
negative controls, and classifies each patient sample as Non-reactive,
Reactive, or Equivocal.

Cut-off convention used here: mean(negative controls) + 0.1
(Adjust CUTOFF_FACTOR / EQUIVOCAL_MARGIN to match your kit's insert.)
"""

import csv
from pathlib import Path

CUTOFF_FACTOR = 0.10       # added to negative control mean
EQUIVOCAL_MARGIN = 0.02    # +/- band around cut-off treated as equivocal

DATA_PATH = Path(__file__).parent / "sample_data" / "plate_results.csv"


def load_plate_data(path: Path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["od450"] = float(row["od450"])
            rows.append(row)
    return rows


def calculate_cutoff(rows):
    neg_controls = [r["od450"] for r in rows if r["sample_type"] == "control" and r["sample_id"].startswith("Neg")]
    if not neg_controls:
        raise ValueError("No negative controls found in dataset.")
    mean_neg = sum(neg_controls) / len(neg_controls)
    return round(mean_neg + CUTOFF_FACTOR, 3)


def classify(od_value: float, cutoff: float) -> str:
    if od_value >= cutoff + EQUIVOCAL_MARGIN:
        return "Reactive"
    elif od_value <= cutoff - EQUIVOCAL_MARGIN:
        return "Non-reactive"
    else:
        return "Equivocal"


def main():
    rows = load_plate_data(DATA_PATH)
    cutoff = calculate_cutoff(rows)

    print(f"Cut-off value (NC mean + {CUTOFF_FACTOR}): {cutoff}\n")
    print(f"{'Sample':<12}{'OD450':<10}{'Result'}")
    print("-" * 36)

    for row in rows:
        if row["sample_type"] != "patient":
            continue
        result = classify(row["od450"], cutoff)
        print(f"{row['sample_id']:<12}{row['od450']:<10}{result}")

    reactive = [r for r in rows if r["sample_type"] == "patient" and classify(r["od450"], cutoff) == "Reactive"]
    print(f"\n{len(reactive)} sample(s) flagged Reactive — confirmatory testing required.")


if __name__ == "__main__":
    main()
