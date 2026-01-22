# A/B Testing Framework — Decision-Focused Experimentation

## Problem
Product and business teams run experiments but often struggle to answer the only question that matters:

**Should we ship this change, or not?**

Many A/B test analyses stop at p-values, ignoring power, risk asymmetry, and business impact—leading to false launches or missed wins.

---

## What this project demonstrates
This project implements a **decision-oriented A/B testing framework** that combines frequentist and Bayesian methods to support **causal decision-making under uncertainty**.

The focus is not statistical novelty, but **trustworthy experimentation**.

---

## Decisions this framework supports
- Whether an observed lift is statistically and practically meaningful
- Whether a test was sufficiently powered to justify a conclusion
- The probability that treatment outperforms control (Bayesian)
- The expected revenue impact and downside risk of shipping
- When *not* to act due to noise or insufficient evidence

---

## Analytical approach

### Experimental design
- Pre-test power analysis and sample size estimation
- Minimum Detectable Effect (MDE) calculation
- Test duration recommendations based on traffic assumptions

### Frequentist analysis
- Two-proportion Z-test for binary outcomes
- Confidence intervals around lift estimates
- Explicit hypothesis formulation (H₀ / H₁)
- Clear decision thresholds (α = 0.05)

### Bayesian analysis
- Beta-Binomial conjugate model
- Posterior distributions for control and treatment
- Monte Carlo simulation (100,000 iterations)
- Direct probability statements:  
  **P(Treatment > Control)**

### Business translation
- Revenue impact estimation
- ROI approximation
- Explicit risk discussion (false positives vs false negatives)

---

## What this framework **does**
- Produces statistically defensible experiment conclusions
- Quantifies uncertainty rather than hiding it
- Translates statistical output into business decisions
- Allows comparison of frequentist vs Bayesian interpretations

## What this framework **does NOT do**
- Perform sequential testing or early stopping
- Correct automatically for multiple simultaneous tests
- Handle non-binary outcome metrics
- Replace domain judgment or product context

---

## Example: Experiment outcome

**Test scenario**
- Control: 10,000 users, 11.45% conversion
- Treatment: 10,000 users, 14.09% conversion

**Results**
- Absolute lift: +2.64 pp  
- Relative lift: +23.06%  
- P-value: < 0.000001  
- 95% CI: [1.72%, 3.56%]  
- Bayesian P(Treatment > Control): ~100%

**Business interpretation**
The observed lift is unlikely to be due to chance and is large enough to justify launch, assuming no unmeasured negative externalities.

**Decision**
✅ Ship treatment, monitor post-launch metrics.

---

## Why this matters for Data Science
Most machine learning models are **descriptive**.  
A/B testing is **prescriptive**.

This project demonstrates:
- Causal reasoning
- Experimental design discipline
- Comfort with uncertainty
- Translation of statistics into executive decisions

These skills are central to Data Scientist roles in product-driven organizations.

---

## Project structure

```text
ab-testing-framework/
│
├── data/
│   └── ab_test_data.csv          # Synthetic test data
│
├── notebooks/
│   └── 01_ab_testing_analysis.ipynb  # Complete analysis
│
├── models/
│   ├── test_results.json         # Saved analysis results
│   └── ab_test_report.png        # Summary report
│
├── app.py                         # Streamlit dashboard
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository

```bash
git clone https://github.com/Emart29/ab-testing-framework.git
cd ab-testing-framework
```

1. Install dependencies

```bash
pip install -r requirements.txt
```

1. Run the application

```bash
streamlit run app.py
```

1. Open your browser and navigate to `http://localhost:8501`

## 👤 Author

**[Emmanuel Nwanguma]**
Data Scientist focused on experimentation, forecasting, and decision-making under uncertainty.

- LinkedIn: [Emmanuel NWanguma](https://www.linkedin.com/in/nwangumaemmanuel)
- GitHub: [Emart29](https://github.com/Emart29)
- Email: <nwangumaemmanuel29@gmail.com>


