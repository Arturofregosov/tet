import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Sales Dashboard")

options = ["Segment","Region","Sub-Category"]
selected_option = st.selectbox("", options)

#Read the Data
data = pd.read_csv("sales_data.csv", low_memory=False, na_filter = False, encoding='latin-1')

# Data aggregation based on user selection
if selected_option == "Segment":
    group_col = "Segment"
elif selected_option == "Region":
    group_col = "Region"
else: 
    group_col = "Sub-Category"

#Group the data by Selected_option
data = data.groupby(selected_option).sum()["Sales"].reset_index()

# Create bar chart
fig = px.bar(data, group_col, "Sales",color_discrete_sequence =['green']).update_xaxes(tickfont_family="Arial Black")
config = {'displayModeBar': False}
st.plotly_chart(fig, config=config)

#Treemap 
#Read the Data
df = pd.read_csv("sales_data.csv", low_memory=False, na_filter = False, encoding='latin-1')

#plot
st.plotly_chart(px.treemap(df,path = ["Product Name"], values = "Sales",color = "Product Name",title="Sales by Product"), config = config)

#Sales by Order Date
df = pd.read_csv("sales_data.csv",encoding="latin-1")
df["Order Date"] = pd.to_datetime(df["Order Date"], format='%m/%d/%y',errors='coerce')
df = df.groupby("Order Date").sum()["Sales"].reset_index()
st.plotly_chart(px.line(df,"Order Date","Sales",template="simple_white", title="Sales by Order Date").update_xaxes(tickfont_family="Arial Black"), config=config)
