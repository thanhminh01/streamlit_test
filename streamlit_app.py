import streamlit as st

# Initialize session states for each button's content visibility
if 'show_analysis_1' not in st.session_state:
    st.session_state.show_analysis_1 = False
if 'show_analysis_2' not in st.session_state:
    st.session_state.show_analysis_2 = False
if 'show_analysis_3' not in st.session_state:
    st.session_state.show_analysis_3 = False
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Function to display analysis buttons and content
def display_analysis():
    # Buttons to toggle analysis visibility after form submission
    if st.button("Show/Hide Analysis for Document 1"):
        st.session_state.show_analysis_1 = not st.session_state.show_analysis_1
    
    if st.button("Show/Hide Analysis for Document 2"):
        st.session_state.show_analysis_2 = not st.session_state.show_analysis_2
    
    if st.button("Show/Hide Analysis for Document 3"):
        st.session_state.show_analysis_3 = not st.session_state.show_analysis_3

    # Conditional display for Document 1 analysis
    if st.session_state.show_analysis_1:
        st.write("Document 1 Analysis: The thematic analysis for this document reveals several core themes...")
    else:
        st.write("Click the button to show the analysis for Document 1.")

    # Conditional display for Document 2 analysis
    if st.session_state.show_analysis_2:
        st.write("Document 2 Analysis: In-depth analysis uncovers significant themes and patterns...")
    else:
        st.write("Click the button to show the analysis for Document 2.")

    # Conditional display for Document 3 analysis
    if st.session_state.show_analysis_3:
        st.write("Document 3 Analysis: Key themes identified in this research highlight several trends...")
    else:
        st.write("Click the button to show the analysis for Document 3.")

# Main logic
if not st.session_state.submitted:
    st.write("Please click submit to view the thematic analysis of the documents.")

    # Create a placeholder for the submit button
    submit_button_placeholder = st.empty()
    if submit_button_placeholder.button("Submit"):
        st.session_state.submitted = True
        submit_button_placeholder.empty()  # Remove only the button after it's clicked

# After form submission, display analysis
if st.session_state.submitted:
    display_analysis()