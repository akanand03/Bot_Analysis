import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Chatbot Performance Dashboard",
    page_icon="💬",
    layout="wide"
)

# Dashboard title
st.title("Chatbot Performance Dashboard")
st.markdown("March 2025 Analysis | Total Conversations: 47")

# Data
resolution_data = [
    {"name": "Bot Resolved", "value": 55.3, "count": 26},
    {"name": "Human Handover", "value": 44.7, "count": 21},
]

common_intents_data = [
    {"name": "Ticket Status", "count": 8},
    {"name": "Document Upload", "count": 7},
    {"name": "Business Types", "count": 5},
    {"name": "Refund Request", "count": 4},
    {"name": "Company Name", "count": 4},
    {"name": "Other", "count": 19},
]

issue_types_data = [
    {"name": "Document Upload Issues", "count": 9},
    {"name": "Callback Requests", "count": 8},
    {"name": "Technical Glitches", "count": 6},
    {"name": "Refund Requests", "count": 5},
    {"name": "Status Inquiries", "count": 11},
    {"name": "Other", "count": 8},
]

weekly_trends_data = [
    {"week": "Week 1", "botResolved": 52, "humanHandover": 48},
    {"week": "Week 2", "botResolved": 54, "humanHandover": 46},
    {"week": "Week 3", "botResolved": 55, "humanHandover": 45},
    {"week": "Week 4", "botResolved": 57, "humanHandover": 43},
]

# Create DataFrames
resolution_df = pd.DataFrame(resolution_data)
common_intents_df = pd.DataFrame(common_intents_data)
issue_types_df = pd.DataFrame(issue_types_data)
weekly_trends_df = pd.DataFrame(weekly_trends_data)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Issue Analysis", "Trends", "Recommendations"])

# Tab 1: Overview
with tab1:
    # KPI metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Bot Resolution Rate",
            value="55.3%",
            delta="26 out of 47 conversations"
        )
        
    with col2:
        st.metric(
            label="Human Handover Rate",
            value="44.7%",
            delta="21 out of 47 conversations"
        )
        
    with col3:
        st.metric(
            label="Avg. Response Time",
            value="12s",
            delta="3s faster than industry avg"
        )
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Resolution Breakdown")
        resolution_fig = px.pie(
            resolution_df, 
            values='value', 
            names='name',
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(resolution_fig, use_container_width=True)
    
    with col2:
        st.subheader("Common Intents")
        intents_fig = px.bar(
            common_intents_df,
            x='name',
            y='count',
            color='count',
            color_continuous_scale=px.colors.sequential.Blues
        )
        intents_fig.update_layout(xaxis_title="", yaxis_title="Count")
        st.plotly_chart(intents_fig, use_container_width=True)

# Tab 2: Issue Analysis
with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Issues Leading to Human Handover")
        issues_bar_fig = px.bar(
            issue_types_df,
            y='name',
            x='count',
            color='count',
            orientation='h',
            color_continuous_scale=px.colors.sequential.Oranges
        )
        issues_bar_fig.update_layout(yaxis_title="", xaxis_title="Count")
        st.plotly_chart(issues_bar_fig, use_container_width=True)
    
    with col2:
        st.subheader("Issue Distribution")
        issues_pie_fig = px.pie(
            issue_types_df, 
            values='count', 
            names='name',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(issues_pie_fig, use_container_width=True)
    
    st.subheader("Issue Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Document Upload Issues (19.1%)")
        st.markdown("Users struggle with district selection, PAN/Aadhar uploads, and property document requirements.")
        
        st.markdown("##### Callback Requests (17.0%)")
        st.markdown("Users frequently request callbacks that are promised but not delivered within expected timeframes.")
    
    with col2:
        st.markdown("##### Technical Glitches (12.8%)")
        st.markdown("Users report UI issues, such as director count requirements not reflecting properly.")
        
        st.markdown("##### Refund Requests (10.6%)")
        st.markdown("All refund requests currently require human intervention, with no automated handling.")

# Tab 3: Trends
with tab3:
    st.subheader("Weekly Resolution Trends")
    trends_fig = go.Figure()
    trends_fig.add_trace(go.Scatter(
        x=weekly_trends_df['week'], 
        y=weekly_trends_df['botResolved'],
        mode='lines+markers',
        name='Bot Resolved (%)',
        line=dict(color='royalblue', width=3)
    ))
    trends_fig.add_trace(go.Scatter(
        x=weekly_trends_df['week'], 
        y=weekly_trends_df['humanHandover'],
        mode='lines+markers',
        name='Human Handover (%)',
        line=dict(color='orange', width=3)
    ))
    trends_fig.update_layout(
        yaxis_range=[40, 60],
        xaxis_title="",
        yaxis_title="Percentage (%)"
    )
    st.plotly_chart(trends_fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Working Hours Analysis")
        st.markdown("**Within Working Hours: 62%**")
        st.progress(0.62)
        st.markdown("**Outside Working Hours: 38%**")
        st.progress(0.38)
        st.caption("Bot resolution rate drops by 18% outside of working hours due to lack of available human agents for complex queries.")
    
    with col2:
        st.subheader("User Satisfaction Analysis")
        st.markdown("**Bot Only Resolution: 78%**")
        st.progress(0.78)
        st.markdown("**Human Handover - Satisfied: 65%**")
        st.progress(0.65)
        st.markdown("**Human Handover - No Response: 35%**")
        st.progress(0.35)
        st.caption("Data suggests that improving agent response rates after handover would significantly boost overall satisfaction.")

# Tab 4: Recommendations
with tab4:
    recommendations = [
        {
            "title": "Document Upload Improvement",
            "description": "Enhance document upload flow with visual guides and better error messaging.",
            "impact": "High",
            "effort": "Medium",
            "priority": 1
        },
        {
            "title": "Status-Based Responses",
            "description": "Customize responses based on specific application status rather than generic messages.",
            "impact": "High",
            "effort": "Low",
            "priority": 2
        },
        {
            "title": "Proactive Service Updates",
            "description": "Implement proactive updates for long processes to reduce \"what's next\" queries.",
            "impact": "Medium",
            "effort": "Medium",
            "priority": 3
        },
        {
            "title": "Technical Issue Detection",
            "description": "Add pattern recognition for common technical problems with specific solutions.",
            "impact": "Medium",
            "effort": "High",
            "priority": 4
        },
        {
            "title": "Improved Callback Integration",
            "description": "Better integrate callback system with bot to set realistic expectations and follow-ups.",
            "impact": "High",
            "effort": "High",
            "priority": 5
        }
    ]
    
    for rec in recommendations:
        with st.expander(f"Priority {rec['priority']}: {rec['title']}"):
            st.markdown(rec["description"])
            col1, col2 = st.columns(2)
            col1.metric("Impact", rec["impact"])
            col2.metric("Effort", rec["effort"])

# Bottom summary
st.divider()
st.subheader("Bot Performance Summary")

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Strengths")
    strengths = [
        "Strong intent recognition for common queries",
        "Clear process guidance with timelines",
        "Effective ticketing system integration",
        "Ability to handle multiple sequential questions",
        "Business hours awareness"
    ]
    for strength in strengths:
        st.markdown(f"- {strength}")

with col2:
    st.markdown("##### Challenges")
    challenges = [
        "Document upload guidance needs improvement",
        "Refund requests require full human intervention",
        "Callback requests often go unfulfilled",
        "Technical glitch responses are too generic",
        "Follow-up question handling is weak"
    ]
    for challenge in challenges:
        st.markdown(f"- {challenge}")

st.markdown("##### Target Metrics (Next Quarter)")
col1, col2, col3 = st.columns(3)
col1.metric("Bot Resolution", "65%", "+9.7%")
col2.metric("Response Time", "8s", "-4s")
col3.metric("Satisfaction", "85%", "+12%")