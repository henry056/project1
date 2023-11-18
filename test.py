import streamlit as st
import pandas as pd
data=pd.read_csv('train.csv', sep='delimiter')
st.title("타이타닉 생존자 예측")
