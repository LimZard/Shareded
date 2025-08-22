# Skibidi clock


import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from datetime import time

st_autorefresh(interval=1000, key="refresh")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/AOW7Ii6.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* transparent header */
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

now = datetime.now()

year = now.year
month = now.month
day = now.day

finnish_hour = now.hour
finnish_minute = now.minute
finnish_second = now.second

finnish_time = time(finnish_hour, finnish_minute, finnish_second)

with st.container():
    st.write("---")
    left, middle, right = st.columns(3)
    with middle:
        st.markdown(
            f"<h8    style='font-size:64px;'>{finnish_time}</h1>",
            unsafe_allow_html=True
        )
    with middle:
        st.text(f"{day}/{month}/{year}")





