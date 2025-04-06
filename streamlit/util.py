from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    weight_csv_file = Path.cwd() / '..' / 'data' / 'weight.csv'
    df = pd.read_csv(weight_csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.sort_index()
    df['Year'] = df.index.year
    df['Day of Year'] = df.index.dayofyear
    return df
