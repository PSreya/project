import streamlit as st

# Set page configuration with custom background color (light blue)
st.set_page_config(
    page_title='Search Engine Web Page',
    layout='wide',
    initial_sidebar_state='auto',
    background_color='#e1f3ff'  # Light blue color
)

# Homepage content with colorful header
def home():
    st.title('🌈 Welcome to the Colorful Search Engine Web Page 🌈')
    st.write('Use the search box below to find information.')

# Search engine content
def search():
    st.subheader('Search Here')
    search_query = st.text_input('Enter your search query:')
    if search_query:
        # Perform search operation here and display the results
        # For demonstration purposes, we'll just display the search query
        st.write(f'Search results for: {search_query}')

# Colorful sidebar with navigation
st.sidebar.title('🎨 Navigation')
nav_options = ['🏠 Home', '🔍 Search']
selected_nav = st.sidebar.radio('Go to:', nav_options)

# Display content based on selected navigation option
if selected_nav == '🏠 Home':
    home()
elif selected_nav == '🔍 Search':
    search()
