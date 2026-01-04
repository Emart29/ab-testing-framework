# A/B Testing Analysis Framework 🧪

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)
![Scipy](https://img.shields.io/badge/Scipy-1.10+-green.svg)

A comprehensive statistical framework for analyzing A/B tests with both frequentist and Bayesian approaches. Make data-driven decisions with confidence.

## 🎯 Project Overview

This framework provides end-to-end A/B testing capabilities: from experimental design (sample size calculation) to post-test analysis (statistical significance, business impact). Built for data scientists who need rigorous statistical methods combined with intuitive visualizations.

## ✨ Key Features

### 1. **Statistical Analysis**

- Two-proportion Z-test with p-values
- 95% confidence intervals
- Effect size calculations
- Multiple testing correction awareness

### 2. **Bayesian Analysis**

- Posterior probability distributions
- P(Treatment > Control) calculation
- Credible intervals
- Monte Carlo simulations (100K iterations)

### 3. **Power Analysis**

- Pre-test sample size calculator
- Statistical power estimation
- Minimum Detectable Effect (MDE) analysis
- Test duration recommendations

### 4. **Business Impact**

- Revenue impact projections
- ROI calculations
- Risk assessment
- Actionable recommendations

### 5. **Interactive Dashboard**

- Real-time analysis
- Multiple visualization tabs
- Test simulation mode
- Sample size calculator

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Interactive web framework
- **Scipy & Statsmodels**: Statistical testing
- **Plotly**: Interactive visualizations
- **NumPy & Pandas**: Data manipulation
- **Jupyter Notebook**: Analysis documentation

## 📁 Project Structure

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

## 📊 Example Results

### Test Scenario

- **Control Group**: 10,000 users, 11.45% conversion
- **Treatment Group**: 10,000 users, 14.09% conversion
- **Absolute Lift**: 2.64 percentage points
- **Relative Lift**: 23.06%

### Statistical Results

- **P-value**: < 0.000001 (highly significant)
- **Z-statistic**: 5.59
- **Confidence Interval**: [1.72%, 3.56%]
- **Bayesian P(B>A)**: 100.0%

### Business Impact

- **Revenue Lift per User**: $3.27
- **Annual Revenue Impact**: $3.9M (for 100K monthly users)
- **Recommendation**: ✅ Launch Treatment

## 🔬 Statistical Methodology

### Frequentist Approach

1. **Hypothesis Testing**
   - H₀: p_treatment ≤ p_control
   - H₁: p_treatment > p_control
   - Significance level: α = 0.05

2. **Two-Proportion Z-Test**
   - Tests equality of proportions
   - Calculates exact p-values
   - Provides confidence intervals

### Bayesian Approach

1. **Prior Distribution**: Uniform Beta(1,1)
2. **Posterior**: Beta(successes + 1, failures + 1)
3. **Monte Carlo**: 100,000 simulations
4. **Output**: Direct probability statements

### Power Analysis

- **Cohen's h**: Effect size for proportions
- **Power**: 80% (industry standard)
- **Accounts for**: Type I and Type II errors

## 💡 Use Cases

1. **E-commerce**: Test new checkout flows
2. **SaaS Products**: Compare onboarding experiences
3. **Marketing**: Evaluate campaign effectiveness
4. **Product Features**: Validate new features
5. **Pricing**: Test pricing strategies

## 📈 Key Insights Demonstrated

### Statistical Rigor

- Proper hypothesis testing
- Multiple approaches (frequentist + Bayesian)
- Power analysis for experimental design
- Business impact quantification

### Data Science Skills

- Statistical inference
- Experimental design
- Causal reasoning
- Business translation

## 🎓 Learning Outcomes

- A/B test design and analysis
- Frequentist vs Bayesian statistics
- Sample size calculation
- Statistical power concepts
- Business metrics translation
- Interactive dashboard development

## 🔮 Future Enhancements

- [ ] Sequential testing (early stopping)
- [ ] Multi-armed bandit algorithms
- [ ] CUPED variance reduction
- [ ] Stratified analysis
- [ ] Multiple metric tracking
- [ ] Automated monitoring and alerts
- [ ] Integration with analytics platforms

## 📚 Resources & References

- **Statistical Methods**: Two-proportion Z-test, Beta-Binomial conjugacy
- **Sample Size**: GPower methodology
- **Best Practices**: Kohavi, Tang & Xu (Trustworthy Online Controlled Experiments)

## ⚠️ Important Notes

### When to Use This Framework

- ✅ Conversion rate optimization
- ✅ Click-through rate testing
- ✅ Binary outcome metrics
- ✅ Independent user assignment

### Limitations

- Assumes independent observations
- Binary outcomes only (extend for continuous)
- No correction for multiple testing (implement Bonferroni/FDR if needed)
- Requires proper randomization

## 🎯 Why This Matters for Data Scientists

A/B testing is the **gold standard** for causal inference in tech companies. This project demonstrates:

1. **Statistical Maturity**: Understanding both frequentist and Bayesian approaches
2. **Practical Application**: Sample size calculations prevent underpowered tests
3. **Business Acumen**: Translating statistics into revenue impact
4. **Communication**: Interactive dashboards for stakeholders

**Most ML models are descriptive. A/B testing is prescriptive.** This shows understanding on how to make causal claims and drive business decisions.

## 👤 Author

**[Your Name]**

- LinkedIn: [Emmanuel NWanguma](https://www.linkedin.com/in/nwangumaemmanuel)
- GitHub: [Emart29](https://github.com/Emart29)
- Email: <nwangumaemmanuel29@gmail.com>

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Statistical methodology based on industry best practices
- Inspired by experimentation platforms at major tech companies
- Built as part of a comprehensive data science portfolio

---

⭐ **If this helped you understand A/B testing, please star the repo!**

💬 **Questions? Open an issue or reach out on LinkedIn**
