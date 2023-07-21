import streamlit as st

# Custom CSS styles using HTML and Markdown
custom_css = """
<style>
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}
.container {
    display: flex;
    flex-direction: row;
}
.search-bar {
    padding: 8px;
    border: none;
    border-radius: 5px;
    width: 300px;
    font-size: 16px;
    margin-right: 20px;
}
.dashboard {
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.filter {
    margin-bottom: 20px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    # Set a title for the app
    st.title("Webpage with Search and Dashboard")

    # Search Bar on the right side
    search_query = st.text_input("Search:", value="", max_chars=50, key="search")

    # Dashboard Content
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<div class='dashboard'>", unsafe_allow_html=True)
    st.write("This is the dashboard content.")
    # Add filters, attributes, and other dashboard content here
    # For example, add a filter
    st.markdown("<div class='filter'>", unsafe_allow_html=True)
    st.write("Filter by:")
    filter_option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"Selected option: {filter_option}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Add more filters, attributes, and visualizations here
    st.markdown("</div>", unsafe_allow_html=True)

    # Add any additional content or widgets on the right side
    # For example, add a placeholder image
    st.image("placeholder_image.png", caption="Placeholder Image", use_column_width=False)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
