import streamlit as st

# Set page configuration
st.set_page_config(page_title='Search Engine Web Page')

# Custom primary colors
primary_bg_color = '#74b9ff'  # Light blue
primary_text_color = '#FF6600'  

# Homepage content with primary color header
def home():
    st.title('Welcome to the Search Engine Web Page')
    st.write('Use the search box below to find information.')

# Search engine content
def search():
    st.subheader('Search Here')
    search_query = st.text_input('Enter your search query:', key='search_box')
    search_btn = st.button('Search', key='search_button', on_click=search_results)
    if search_query and search_btn:
        # Perform search operation here and display the results
        # For demonstration purposes, we'll just display the search query
        st.write(f'Search results for: {search_query}')

# Function to handle search button click
def search_results():
    st.experimental_rerun()

# Apply Bulma CSS styles using st.markdown
bulma_css = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css">
<style>
.stButton {{
    background-color: {primary_bg_color} !important;
    color: {primary_text_color} !important;
}}
.stTextInput div[contenteditable="true"] {{
    color: {primary_text_color} !important;
    background-color: {primary_bg_color} !important;
}}
</style>
"""
st.markdown(bulma_css.format(primary_bg_color=primary_bg_color, primary_text_color=primary_text_color), unsafe_allow_html=True)

# Sidebar with navigation
st.sidebar.title('Navigation')
nav_options = ['Home', 'Search']
selected_nav = st.sidebar.radio('Go to:', nav_options)

# Display content based on selected navigation option
if selected_nav == 'Home':
    home()
elif selected_nav == 'Search':
    search()
