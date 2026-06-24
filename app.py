
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(
    page_title="Retail Banking Customer Analytics Platform",
    layout="wide"
)

st.title("Retail Banking Customer Analytics Platform")
st.caption(
    "Executive Dashboard | Branch Performance | Customer Segmentation | Campaign Analytics"
)

# -----------------------------
# Connect to SQLite database
# -----------------------------

conn = sqlite3.connect("retail_banking_analytics.db")

# -----------------------------
# Load KPI Views
# -----------------------------

branch_df = pd.read_sql_query(
    "SELECT * FROM vw_branch_performance",
    conn
)

segment_df = pd.read_sql_query(
    "SELECT * FROM vw_customer_segment_kpi",
    conn
)

monthly_df = pd.read_sql_query(
    "SELECT * FROM vw_monthly_campaign_trend",
    conn
)

# -----------------------------
# Executive KPI Cards
# -----------------------------

total_customers = branch_df["total_customers"].sum()
avg_revenue = branch_df["avg_estimated_revenue"].mean()
avg_risk = branch_df["avg_risk_score"].mean()

overall_conversion = (
    branch_df["successful_campaigns"].sum()
    / total_customers
    * 100
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        f"{total_customers:,.0f}"
    )

with col2:
    st.metric(
        "Avg Revenue",
        f"${avg_revenue:,.2f}"
    )

with col3:
    st.metric(
        "Avg Risk Score",
        f"{avg_risk:.2f}"
    )

with col4:
    st.metric(
        "Conversion Rate",
        f"{overall_conversion:.2f}%"
    )

st.divider()

# -----------------------------
# Row 1
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Branch Performance by Revenue")

    fig = px.bar(
        branch_df,
        x="branch_name",
        y="avg_estimated_revenue",
        color="province",
        text="avg_estimated_revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader(
        "Subscription Rate by Customer Segment"
    )

    fig = px.bar(
        segment_df,
        x="customer_segment",
        y="subscription_rate_pct",
        text="subscription_rate_pct"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Row 2
# -----------------------------

col3, col4 = st.columns(2)

with col3:

    st.subheader(
        "Monthly Campaign Conversion Trend"
    )

    fig = px.line(
        monthly_df,
        x="month",
        y="conversion_rate_pct",
        markers=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col4:

    st.subheader(
        "Average Risk Score by Branch"
    )

    fig = px.bar(
        branch_df,
        x="branch_name",
        y="avg_risk_score",
        color="province",
        text="avg_risk_score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------------
# Tables
# -----------------------------

st.subheader("Branch KPI Table")
st.dataframe(
    branch_df,
    use_container_width=True
)

st.subheader("Customer Segment KPI Table")
st.dataframe(
    segment_df,
    use_container_width=True
)
