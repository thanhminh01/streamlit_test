import streamlit as st

# Initialize session states for each button's content visibility
if 'show_analysis_1' not in st.session_state:
    st.session_state.show_analysis_1 = False
if 'show_analysis_2' not in st.session_state:
    st.session_state.show_analysis_2 = False
if 'show_analysis_3' not in st.session_state:
    st.session_state.show_analysis_3 = False

# Create a form for the query input
submitted = False
with st.form(key='analysis_form'):
    query = st.text_input("Enter a search query (default: 'Prompt Engineering'):") or "Prompt Engineering"
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        submitted = True

# Show/hide content based on whether form was submitted
if submitted:
    # Show the buttons to toggle analysis visibility
    if st.button("Show/Hide Analysis for Document 1"):
        st.session_state.show_analysis_1 = not st.session_state.show_analysis_1
    
    if st.button("Show/Hide Analysis for Document 2"):
        st.session_state.show_analysis_2 = not st.session_state.show_analysis_2
    
    if st.button("Show/Hide Analysis for Document 3"):
        st.session_state.show_analysis_3 = not st.session_state.show_analysis_3

    # Display the analysis or a prompt based on the toggle state
    if st.session_state.show_analysis_1:
        st.write("Document 1 Analysis: The thematic analysis for this document reveals several core themes...")
    else:
        st.write("Click the button to show the analysis for Document 1.")

    if st.session_state.show_analysis_2:
        st.write("Document 2 Analysis: In-depth analysis uncovers significant themes and patterns...")
    else:
        st.write("Click the button to show the analysis for Document 2.")

    if st.session_state.show_analysis_3:
        st.write("Document 3 Analysis: Key themes identified in this research highlight several trends...")
    else:
        st.write("Click the button to show the analysis for Document 3.")
