import streamlit as st

# Set page configuration
st.set_page_config(page_title='Search Engine Web Page')

# Homepage content
def home():
    st.title('Welcome to the Search Engine Web Page')
    st.write('Use the search box below to find information.')

# Search engine content
def search():
    st.subheader('Search Here')
    search_query = st.text_input('Enter your search query:')
    if search_query:
        # Perform search operation here and display the results
        # For demonstration purposes, we'll just display the search query
        st.write(f'Search results for: {search_query}')

# Sidebar with navigation
st.sidebar.title('Navigation')
nav_options = ['Home', 'Search']
selected_nav = st.sidebar.radio('Go to:', nav_options)

# Display content based on selected navigation option
if selected_nav == 'Home':
    home()
elif selected_nav == 'Search':
    search()
