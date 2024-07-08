import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Sales Dashboard")

options = ["Region","Segment"]
selected_option = st.selectbox("", options)

#Read the Data
data = pd.read_csv("sales_data.csv", low_memory=False, na_filter = False, encoding='latin-1')

# Data aggregation based on user selection
if selected_option == "Segment":
    group_col = "Segment"
else: 
    group_col = "Region"

#Group the data by Selected_option
data = data.groupby(selected_option).sum()["Sales"].reset_index()

# Create bar chart
fig = px.bar(data, group_col, "Sales",color_discrete_sequence =['red'])
config = {'displayModeBar': False}
st.plotly_chart(fig, config=config)
