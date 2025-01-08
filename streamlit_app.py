import streamlit as st

# Set up a simple app with 3 buttons to show/hide content
st.title("Toggle Multiple Contents Example")

# Initialize session states for each button's content visibility
if 'show_content_1' not in st.session_state:
    st.session_state.show_content_1 = False
if 'show_content_2' not in st.session_state:
    st.session_state.show_content_2 = False
if 'show_content_3' not in st.session_state:
    st.session_state.show_content_3 = False

# Button 1 to toggle content visibility
if st.button("Show/Hide Content 1"):
    st.session_state.show_content_1 = not st.session_state.show_content_1

# Button 2 to toggle content visibility
if st.button("Show/Hide Content 2"):
    st.session_state.show_content_2 = not st.session_state.show_content_2

# Button 3 to toggle content visibility
if st.button("Show/Hide Content 3"):
    st.session_state.show_content_3 = not st.session_state.show_content_3

# Conditional display for Content 1
if st.session_state.show_content_1:
    st.write("This is the content for Button 1!")
else:
    st.write("Click the button to show content 1.")

# Conditional display for Content 2
if st.session_state.show_content_2:
    st.write("This is the content for Button 2!")
else:
    st.write("Click the button to show content 2.")

# Conditional display for Content 3
if st.session_state.show_content_3:
    st.write("This is the content for Button 3!")
else:
    st.write("Click the button to show content 3.")
