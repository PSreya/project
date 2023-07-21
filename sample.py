import streamlit as st
import pandas as pd
from PIL import Image

# Title and Header
st.title('Search Engine and Dashboard')
st.header('This is a web app that allows you to search for information and view a dashboard.')

# Search Bar
st.sidebar.title('Search Bar')
query = st.sidebar.text_input('Enter your search query')

# Search Results
if query:
    results = pd.read_csv('data.csv')
    results = results[results['Title'].str.contains(query)]
    st.table(results)

# Dashboard
st.sidebar.title('Dashboard')


# Widget 1
st.sidebar.subheader('Widget 1')
text = st.sidebar.text_input('Enter some text')

# Widget 2
st.sidebar.subheader('Widget 2')
image = Image.open('image.jpg')
st.sidebar.image(image)