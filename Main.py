import streamlit as st
from datetime import datetime
from datetime import date

now = datetime.now()

year = now.year
month = now.month
day = now.day

st.title("How long you live, yes?")

year_born = st.text_input("Enter Year of birth")
month_born = st.text_input("Enter Month of birth")
day_born = st.text_input("Enter Day of birth")

if year_born != "" and month_born != "" and day_born != "":
    today = date(year=year, month=month, day=day)
    given_date = date(year=int(year_born), month=int(month_born), day=int(day_born))
    diff = today - given_date
    st.write(diff.days)



