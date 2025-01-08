import streamlit as st

# Set up a simple app with a button to show/hide content
st.title("Toggle Content Example")

# Create a button that toggles the visibility of the content
if 'show_content' not in st.session_state:
    st.session_state.show_content = False  # Initial state is False (hidden)

# Button to toggle the content visibility
if st.button("Show/Hide Content"):
    st.session_state.show_content = not st.session_state.show_content

# Show content based on the button state
if st.session_state.show_content:
    st.write("This is the content that can be toggled!")
else:
    st.write("Click the button to show the content.")
