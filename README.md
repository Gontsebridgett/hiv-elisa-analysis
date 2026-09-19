# HIV Antibody Detection by ELISA — Protocol & Result Analysis

An indirect ELISA (Enzyme-Linked Immunosorbent Assay) workflow for detecting HIV-specific
antibodies in serum samples, paired with a Python script that calculates the assay
cut-off value and classifies plate results automatically from raw OD450 readings.

## Overview

ELISA is an immunoassay technique used to detect antigens or antibodies in a sample via
antibody–antigen binding linked to an enzyme reporter. In this indirect format, HIV
antigens (e.g. gp41, gp120, p24) are immobilised on a microplate. If HIV-specific
antibodies are present in a patient's serum, they bind the antigen; a secondary
HRP-conjugated anti-human IgG then binds the patient antibody, and a chromogenic
substrate (TMB) produces a colour change proportional to antibody concentration,
read as optical density (OD) at 450 nm.

## Principle

1. **Coating** — HIV antigen bound to the microplate well surface
2. **Blocking** — non-specific binding sites saturated with BSA/blocking buffer
3. **Sample incubation** — patient serum antibodies bind immobilised antigen (if present)
4. **Secondary antibody** — HRP-conjugated anti-human IgG binds captured antibody
5. **Substrate development** — TMB produces colour proportional to bound antibody
6. **Stop & read** — reaction stopped, absorbance read at 450 nm

## Materials & Reagents

- 96-well microplate pre-coated with HIV antigen
- Patient serum samples, positive control, negative control
- Wash buffer (PBS + 0.05% Tween-20)
- Blocking buffer (PBS + 1–5% BSA)
- HRP-conjugated anti-human IgG secondary antibody
- TMB substrate and stop solution (2M H2SO4)
- Microplate reader (450 nm)

## Method (Summary)

| Step | Action | Time/Temp |
|---|---|---|
| 1 | Coat plate with antigen | Overnight, 4°C |
| 2 | Wash ×3 | — |
| 3 | Block | 1 hr, 37°C |
| 4 | Add samples/controls | 1 hr, 37°C |
| 5 | Wash ×3–5 | — |
| 6 | Add secondary antibody | 30–60 min, 37°C |
| 7 | Wash ×3–5 | — |
| 8 | Add TMB substrate | 10–15 min, dark |
| 9 | Stop reaction | — |
| 10 | Read OD450 | Within 30 min |

## Result Interpretation

Cut-off (CO) = mean OD of negative control + fixed factor (per kit protocol, e.g. +0.1)

| OD Result | Interpretation |
|---|---|
| OD < Cut-off | Non-reactive (negative) |
| OD ≥ Cut-off | Reactive — requires confirmatory testing |
| OD near cut-off | Equivocal — repeat testing |

> A reactive ELISA result is a **screening** result only — confirmatory testing
> (e.g. Western blot) is required before any diagnostic conclusion.

## Analysis Script

`elisa_analysis.py` reads raw OD450 plate data from `sample_data/plate_results.csv`,
calculates the cut-off value from the negative controls, classifies every sample as
Non-reactive / Reactive / Equivocal, and prints a summary table.

### Usage

```bash
pip install -r requirements.txt
python elisa_analysis.py
```

### Sample output

```
Cut-off value (NC mean + 0.1): 0.245

Sample     OD450    Result
--------------------------------
Patient_1  0.112    Non-reactive
Patient_2  0.891    Reactive
Patient_3  0.238    Equivocal
...
```

## Repository Structure

```
hiv-elisa-analysis/
├── README.md
├── elisa_analysis.py
├── requirements.txt
└── sample_data/
    └── plate_results.csv
```

## Disclaimer

This repository is for educational and portfolio purposes, based on standard
laboratory protocol structure. It is not intended for, and must not be used in,
actual clinical diagnosis.
