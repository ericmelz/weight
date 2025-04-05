import streamlit as st

st.set_page_config(
    page_title="Eric's Weight",
    page_icon="👋"
)

st.write("# Eric's Weight 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This site shows some fun facts about Eric's weight.
    * **📈 Overview** - shows historic weight
    * **📉 Weight Loss** - shows visualizations of attempted weight loss episodes 
    * **📊 Distribution** - shows some interactive weight distribution visualizations

    Questions? Contact <eric@emelz.com>
    
    Enjoy!
    """
)
