# Retail Banking Customer Analytics

Live Demo

https://retail-banking-customer-analytics.streamlit.app

## Project Overview

This project demonstrates the design and implementation of an end-to-end Retail Banking Customer Analytics Platform using Python, SQL, Machine Learning, and Streamlit.

The solution transforms raw banking campaign data into business-ready insights through data engineering, data modeling, SQL analytics, executive dashboards, and predictive analytics.

The project simulates how a Canadian retail bank could leverage customer, campaign, and economic data to improve marketing effectiveness, customer segmentation, and subscription conversion rates.

---

## Business Problem

Retail banks invest significant resources in marketing campaigns to promote products such as term deposits and savings products.

The objective of this project is to:

* Understand customer behavior and subscription patterns
* Identify high-value customer segments
* Analyze branch-level performance
* Measure campaign effectiveness
* Predict which customers are most likely to subscribe to a banking product

---

## Solution Architecture

### Step 1 — Data Preparation Layer

* Data quality assessment
* Missing value handling
* Feature engineering
* Customer segmentation
* Risk score creation
* Revenue estimation

### Step 2 — Data Modeling Layer

Created a normalized SQLite database including:

* Customers
* Branches
* Financial Profiles
* Campaign Contacts
* Campaign Outcomes
* Economic Indicators

### Step 3 — SQL Analytics Layer

Developed reusable SQL KPI views for:

* Branch Performance Analysis
* Customer Segmentation Analysis
* Campaign Conversion Trends

### Step 4 — Dashboard & Visualization Layer

Built an interactive Streamlit dashboard featuring:

* Executive KPI Cards
* Branch Performance Dashboard
* Customer Segmentation Dashboard
* Campaign Analytics Dashboard
* Interactive Plotly Visualizations

### Step 5 — Predictive Analytics Layer

Developed a Random Forest classification model to predict customer subscription likelihood.

Model Performance:

* Accuracy: 92%
* ROC-AUC: 0.95
* Precision (Subscribed Customers): 69%
* Recall (Subscribed Customers): 49%

Key predictive drivers included:

* Call Duration
* Estimated Revenue
* Euribor Rate
* Employment Indicators
* Customer Segment
* Customer Age

### Step 6 — Deployment & Project Packaging Layer

* GitHub Repository
* Streamlit Application
* Project Documentation
* Cloud Deployment

---

## Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Database

* SQLite

### Analytics

* SQL
* Scikit-Learn

### Visualization

* Plotly
* Streamlit
* Matplotlib

---

## Dashboard Features

### Executive KPIs

* Total Customers
* Average Revenue
* Average Risk Score
* Conversion Rate

### Branch Analytics

* Branch Performance by Revenue
* Branch Risk Analysis

### Customer Analytics

* Customer Segment Performance
* Subscription Rate Analysis

### Campaign Analytics

* Monthly Conversion Trends
* Campaign Success Metrics

---

## Machine Learning Results

The predictive model successfully identified customer subscription behavior using demographic, financial, campaign, segmentation, and economic features.

Feature importance analysis revealed that customer engagement duration, estimated revenue, economic indicators, and customer segments were among the strongest drivers of subscription likelihood.

---

## Future Enhancements

* Hyperparameter tuning
* Model monitoring
* Cloud database integration
* Real-time data refresh
* Advanced customer lifetime value modeling
* Multi-product recommendation engine

---

## Author

Mahdieh Ghafourian (Aylin)

Toronto, Ontario

Master of Information Systems & Technology, York University
