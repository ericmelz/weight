import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Overview", page_icon="📈")

st.markdown("# Overview")
st.sidebar.header("Overview")


@st.cache_data
def load_data():
    weight_csv_file = Path.cwd() / '..' / 'data' / 'weight.csv'
    df = pd.read_csv(weight_csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.sort_index()
    return df


df = load_data()

fig = px.line(df, x=df.index, y='Weight (lb)', title='Weight Over Time')

st.plotly_chart(fig)

if st.checkbox('Show raw data'):
    st.write(df)



