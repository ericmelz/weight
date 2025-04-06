import pandas as pd
import plotly.express as px
import streamlit as st

import util

st.set_page_config(page_title="Weight Loss", page_icon="📉")

st.markdown("# Weight Loss")
st.sidebar.header("Weight Loss")

df = util.load_data()

df_2024 = df[df['Year'] == 2024].copy()
df_2025 = df[df['Year'] == 2025].copy()
df_2024['Label'] = '2024'
df_2025['Label'] = '2025'

combined_df = pd.concat(([df_2024, df_2025]))


fig = px.line(combined_df, x='Day of Year', y='Weight (lb)', color='Label', title='Weight in 2024 vs 2025')

st.plotly_chart(fig)

if st.checkbox('Show raw data'):
    st.caption('2024')
    st.write(df_2024['Weight (lb)'])
    st.caption('2025')
    st.write(df_2025['Weight (lb)'])

