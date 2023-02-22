import streamlit as st
import pandas as pd

st.title("Esto es el titulo")

st.write("Esto es un texto")

st.write("más texto...")

st.write("mucho más texto...")

df = pd.read_csv('data/addresses.csv')

df
