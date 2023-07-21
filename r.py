import streamlit as st

# Create a search bar
st.sidebar.title("Search")
st.sidebar.text_input("Enter your search query")

# Create a home dashboard
st.title("Home Dashboard")
st.write("This is the home dashboard.")

# Add some styles to your app
st.set_page_config(page_title="My Search Engine", page_icon="https://www.google.com/favicon.ico")

# Set the background color of the app
st.markdown("""
<style>
body {
  background-color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

