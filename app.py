import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from statsmodels.stats.power import zt_ind_solve_power
import json

# Page config
st.set_page_config(
    page_title="A/B Testing Framework",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3rem; font-weight: bold; color: #1f77b4;}
    .sub-header {font-size: 1.5rem; color: #555;}
    .metric-card {background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🧪 A/B Testing Analysis Framework</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Statistical experimentation platform for data-driven decisions</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Test Configuration")

# Mode selection
mode = st.sidebar.radio(
    "Select Mode",
    ["📊 Analyze Existing Test", "🎲 Simulate New Test", "📐 Sample Size Calculator"]
)

if mode == "📊 Analyze Existing Test":
    st.header("📊 Analyze Existing A/B Test")
    
    # Load pre-existing data
    @st.cache_data
    def load_data():
        return pd.read_csv('data/ab_test_data.csv')
    
    df = load_data()
    
    # Display data overview
    with st.expander("📋 View Raw Data", expanded=False):
        st.dataframe(df.head(100))
        st.write(f"Total rows: {len(df):,}")
    
    # Calculate metrics
    control_data = df[df['group'] == 'A (Control)']
    treatment_data = df[df['group'] == 'B (Treatment)']
    
    control_conv = control_data['converted'].mean()
    treatment_conv = treatment_data['converted'].mean()
    
    absolute_lift = treatment_conv - control_conv
    relative_lift = (absolute_lift / control_conv) * 100
    
    # KPI Cards
    st.subheader("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Control Conversion", f"{control_conv*100:.2f}%")
    with col2:
        st.metric("Treatment Conversion", f"{treatment_conv*100:.2f}%")
    with col3:
        st.metric("Absolute Lift", f"{absolute_lift*100:.2f}pp", 
                 delta=f"{absolute_lift*100:.2f}pp")
    with col4:
        st.metric("Relative Lift", f"{relative_lift:.1f}%", 
                 delta=f"{relative_lift:.1f}%")
    
    # Statistical Test
    st.subheader("📊 Statistical Significance Test")
    
    conversions = np.array([treatment_data['converted'].sum(), control_data['converted'].sum()])
    nobs = np.array([len(treatment_data), len(control_data)])
    
    z_stat, p_value = proportions_ztest(conversions, nobs, alternative='larger')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Two-Proportion Z-Test")
        st.write(f"**Z-statistic:** {z_stat:.4f}")
        st.write(f"**P-value:** {p_value:.6f}")
        st.write(f"**Significance level (α):** 0.05")
        
        if p_value < 0.05:
            st.success("✅ **STATISTICALLY SIGNIFICANT!** Treatment is better than Control.")
        else:
            st.warning("⚠️ **Not significant.** Difference might be due to chance.")
    
    with col2:
        # Confidence intervals
        control_ci = proportion_confint(control_data['converted'].sum(), 
                                       len(control_data), alpha=0.05, method='normal')
        treatment_ci = proportion_confint(treatment_data['converted'].sum(), 
                                         len(treatment_data), alpha=0.05, method='normal')
        
        st.markdown("### 95% Confidence Intervals")
        st.write(f"**Control:** [{control_ci[0]*100:.2f}%, {control_ci[1]*100:.2f}%]")
        st.write(f"**Treatment:** [{treatment_ci[0]*100:.2f}%, {treatment_ci[1]*100:.2f}%]")
        
        diff_se = np.sqrt((control_conv * (1 - control_conv) / len(control_data)) + 
                         (treatment_conv * (1 - treatment_conv) / len(treatment_data)))
        diff_ci_lower = absolute_lift - 1.96 * diff_se
        diff_ci_upper = absolute_lift + 1.96 * diff_se
        
        st.write(f"**Lift:** [{diff_ci_lower*100:.2f}%, {diff_ci_upper*100:.2f}%]")
    
    # Visualization
    st.subheader("📊 Visualizations")
    
    tab1, tab2, tab3 = st.tabs(["Conversion Comparison", "Bayesian Analysis", "Revenue Impact"])
    
    with tab1:
        # Conversion rate comparison
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Control',
            x=['Control'],
            y=[control_conv * 100],
            marker_color='#3498db',
            text=[f'{control_conv*100:.2f}%'],
            textposition='outside'
        ))
        
        fig.add_trace(go.Bar(
            name='Treatment',
            x=['Treatment'],
            y=[treatment_conv * 100],
            marker_color='#e74c3c',
            text=[f'{treatment_conv*100:.2f}%'],
            textposition='outside'
        ))
        
        fig.update_layout(
            title='Conversion Rate Comparison',
            yaxis_title='Conversion Rate (%)',
            showlegend=False,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Bayesian analysis
        st.markdown("### Bayesian Posterior Analysis")
        
        control_successes = control_data['converted'].sum()
        control_failures = len(control_data) - control_successes
        treatment_successes = treatment_data['converted'].sum()
        treatment_failures = len(treatment_data) - treatment_successes
        
        # Monte Carlo simulation
        np.random.seed(42)
        n_sim = 100000
        
        control_samples = np.random.beta(control_successes + 1, control_failures + 1, n_sim)
        treatment_samples = np.random.beta(treatment_successes + 1, treatment_failures + 1, n_sim)
        
        prob_treatment_better = (treatment_samples > control_samples).mean()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("P(Treatment > Control)", f"{prob_treatment_better*100:.2f}%")
            
            if prob_treatment_better > 0.95:
                st.success("✅ **Strong evidence** that Treatment is better")
            elif prob_treatment_better > 0.90:
                st.info("✅ **Good evidence** that Treatment is better")
            else:
                st.warning("⚠️ **Weak evidence**")
        
        with col2:
            expected_lift = (treatment_samples - control_samples).mean()
            lift_ci = np.percentile(treatment_samples - control_samples, [2.5, 97.5])
            
            st.write(f"**Expected Lift:** {expected_lift*100:.2f}pp")
            st.write(f"**95% Credible Interval:** [{lift_ci[0]*100:.2f}%, {lift_ci[1]*100:.2f}%]")
        
        # Plot distributions
        lift_samples = treatment_samples - control_samples
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=lift_samples * 100,
            nbinsx=50,
            name='Lift Distribution',
            marker_color='purple',
            opacity=0.7
        ))
        
        fig.add_vline(x=0, line_dash="dash", line_color="red", 
                     annotation_text="No difference")
        fig.add_vline(x=expected_lift*100, line_color="green", 
                     annotation_text="Expected lift")
        
        fig.update_layout(
            title='Distribution of Lift (Bayesian Posterior)',
            xaxis_title='Lift (percentage points)',
            yaxis_title='Frequency',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Business Impact Analysis")
        
        control_revenue = control_data['revenue'].mean()
        treatment_revenue = treatment_data['revenue'].mean()
        revenue_lift = treatment_revenue - control_revenue
        
        monthly_users = st.number_input("Monthly Users", value=100000, step=10000)
        
        monthly_impact = revenue_lift * monthly_users
        annual_impact = monthly_impact * 12
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Revenue per User Lift", f"${revenue_lift:.2f}")
        with col2:
            st.metric("Monthly Revenue Impact", f"${monthly_impact:,.0f}")
        with col3:
            st.metric("Annual Revenue Impact", f"${annual_impact:,.0f}")
        
        # Impact visualization
        metrics = ['Conversion Lift', 'Revenue Lift', 'Monthly Impact', 'Annual Impact']
        values = [expected_lift*100, revenue_lift, monthly_impact, annual_impact]
        
        fig = go.Figure(go.Bar(
            x=metrics,
            y=values,
            marker_color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c'],
            text=[f'{expected_lift*100:.2f}pp', f'${revenue_lift:.2f}', 
                  f'${monthly_impact:,.0f}', f'${annual_impact:,.0f}'],
            textposition='outside'
        ))
        
        fig.update_layout(
            title='Business Impact Summary',
            yaxis_title='Value',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Final Recommendation
    st.subheader("💡 Final Recommendation")
    
    if p_value < 0.05 and prob_treatment_better > 0.95:
        st.success(f"""
        ### ✅ LAUNCH TREATMENT TO 100% OF USERS
        
        **Reasoning:**
        - Statistical significance: P-value = {p_value:.6f} (highly significant)
        - Bayesian confidence: {prob_treatment_better*100:.1f}% probability Treatment is better
        - Business impact: ${annual_impact:,.0f} estimated annual revenue increase
        - Risk: Very low
        
        **Action Items:**
        1. Roll out Treatment to all users
        2. Monitor metrics for 2 weeks post-launch
        3. Set up alerts for any unexpected drops
        4. Document learnings for future tests
        """)
    else:
        st.warning("⚠️ **CONTINUE TESTING** - Insufficient evidence to make a decision")

elif mode == "🎲 Simulate New Test":
    st.header("🎲 Simulate A/B Test")
    
    st.write("Generate synthetic A/B test data with custom parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        n_users = st.number_input("Users per group", value=10000, step=1000)
        control_rate = st.slider("Control conversion rate (%)", 0.0, 50.0, 12.0) / 100
    
    with col2:
        lift = st.slider("Expected lift (percentage points)", 0.0, 10.0, 2.0) / 100
        treatment_rate = control_rate + lift
        st.write(f"Treatment rate: {treatment_rate*100:.2f}%")
    
    if st.button("🎲 Generate Test Data"):
        np.random.seed(42)
        
        # Generate data
        control_conv = np.random.binomial(1, control_rate, n_users)
        treatment_conv = np.random.binomial(1, treatment_rate, n_users)
        
        # Run analysis
        conversions = np.array([treatment_conv.sum(), control_conv.sum()])
        nobs = np.array([n_users, n_users])
        
        z_stat, p_value = proportions_ztest(conversions, nobs, alternative='larger')
        
        st.success("✅ Test data generated!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Control Conversion", f"{control_conv.mean()*100:.2f}%")
        with col2:
            st.metric("Treatment Conversion", f"{treatment_conv.mean()*100:.2f}%")
        with col3:
            st.metric("P-value", f"{p_value:.4f}")
        
        if p_value < 0.05:
            st.success("✅ Result is statistically significant!")
        else:
            st.warning("⚠️ Result is NOT statistically significant. Need more users or larger effect size.")

else:  # Sample Size Calculator
    st.header("📐 Sample Size Calculator")
    
    st.write("Calculate the required sample size for your A/B test")
    
    col1, col2 = st.columns(2)
    
    with col1:
        baseline_rate = st.slider("Baseline conversion rate (%)", 0.0, 50.0, 12.0) / 100
        mde = st.slider("Minimum Detectable Effect (pp)", 0.5, 10.0, 1.5) / 100
    
    with col2:
        alpha = st.select_slider("Significance level (α)", 
                                 options=[0.01, 0.05, 0.10], value=0.05)
        power = st.select_slider("Statistical power", 
                                options=[0.70, 0.80, 0.90, 0.95], value=0.80)
    
    # Calculate
    def cohens_h(p1, p2):
        return 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))
    
    effect_size = abs(cohens_h(baseline_rate, baseline_rate + mde))
    
    required_n = zt_ind_solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1.0,
        alternative='two-sided'
    )
    
    st.subheader("📊 Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sample Size per Group", f"{int(np.ceil(required_n)):,}")
    with col2:
        st.metric("Total Sample Size", f"{int(np.ceil(required_n)) * 2:,}")
    with col3:
        daily_traffic = st.number_input("Daily traffic", value=1000, step=100)
        test_days = int(np.ceil((required_n * 2) / daily_traffic))
        st.metric("Test Duration", f"{test_days} days")
    
    # Visualization
    st.subheader("📈 Sample Size for Different MDEs")
    
    mde_range = np.arange(0.005, 0.05, 0.005)
    sample_sizes = []
    
    for mde_val in mde_range:
        es = abs(cohens_h(baseline_rate, baseline_rate + mde_val))
        n = zt_ind_solve_power(effect_size=es, alpha=alpha, power=power, ratio=1.0, alternative='two-sided')
        sample_sizes.append(n)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=mde_range * 100,
        y=sample_sizes,
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Sample Size Requirements vs Minimum Detectable Effect',
        xaxis_title='Minimum Detectable Effect (%)',
        yaxis_title='Required Sample Size per Group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.subheader("📚 About")
st.sidebar.info("""
**A/B Testing Framework**

This tool helps you:
- Analyze A/B test results
- Calculate statistical significance
- Perform Bayesian analysis
- Estimate business impact
- Calculate sample sizes

Built for data scientists who make data-driven decisions.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("Built by Emmanuel Nwanguma")
