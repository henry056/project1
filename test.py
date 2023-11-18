import streamlit as st
import pandas as pd
data=pd.read_csv('경찰청_범죄 발생 지역별 통계_20151231.csv')
st.title("지역별 범죄에 대한 조사")
