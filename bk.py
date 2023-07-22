import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title='Search Engine and Dashboard')

# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    .stButton {
        background-color: #74b9ff !important;
        color: #ffffff !important;
    }
    .stTextInput div[contenteditable="true"] {
        background-color: #74b9ff !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample data for the dashboard
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [30, 40, 50, 20]
})

# Homepage content
def home():
    st.title('Welcome to the Search Engine Web Page')
    st.write('Use the search box below to find information.')

# Search engine content
def search():
    st.subheader('Search Here')
    search_query = st.text_input('Enter your search query:')
    if st.button('Search'):
        # Perform search operation here and display the results
        # For demonstration purposes, we'll just display the search query
        st.write(f'Search results for: {search_query}')

# Dashboard content
def dashboard():
    st.subheader('Dashboard')
    st.write('Here is a simple chart for demonstration purposes:')
    sns.barplot(data=data, x='Category', y='Value')
    plt.xlabel('Category')
    plt.ylabel('Value')
    st.pyplot()

# Sidebar with navigation
st.sidebar.title('Navigation')
nav_options = ['Home', 'Search', 'Dashboard']
selected_nav = st.sidebar.radio('Go to:', nav_options)

# Display content based on selected navigation option
if selected_nav == 'Home':
    home()
elif selected_nav == 'Search':
    search()
elif selected_nav == 'Dashboard':
    dashboard()
