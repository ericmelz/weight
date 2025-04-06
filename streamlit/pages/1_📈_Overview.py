import pandas as pd
import plotly.express as px
import streamlit as st

import util

st.set_page_config(page_title="Overview", page_icon="📈")

st.markdown("# Overview")
st.sidebar.header("Overview")


df = util.load_data()

fig = px.line(df, x=df.index, y='Weight (lb)', title='Weight Over Time')

st.plotly_chart(fig)

if st.checkbox('Show raw data'):
    st.write(df)
