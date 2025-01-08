import streamlit as st

# Set up a simple app with 3 buttons to show/hide document analysis results
st.title("Thematic Analysis of Research Articles")

# Initialize session states for each button's content visibility
if 'show_analysis_1' not in st.session_state:
    st.session_state.show_analysis_1 = False
if 'show_analysis_2' not in st.session_state:
    st.session_state.show_analysis_2 = False
if 'show_analysis_3' not in st.session_state:
    st.session_state.show_analysis_3 = False

# Button 1 to toggle analysis visibility for Document 1
if st.button("Show/Hide Analysis for Document 1"):
    st.session_state.show_analysis_1 = not st.session_state.show_analysis_1

# Button 2 to toggle analysis visibility for Document 2
if st.button("Show/Hide Analysis for Document 2"):
    st.session_state.show_analysis_2 = not st.session_state.show_analysis_2

# Button 3 to toggle analysis visibility for Document 3
if st.button("Show/Hide Analysis for Document 3"):
    st.session_state.show_analysis_3 = not st.session_state.show_analysis_3

# Conditional display for Document 1 analysis
if st.session_state.show_analysis_1:
    # Replace with actual analysis result for Document 1
    st.write("Document 1 Analysis: The thematic analysis for this document reveals several core themes...")
else:
    st.write("Click the button to show the analysis for Document 1.")

# Conditional display for Document 2 analysis
if st.session_state.show_analysis_2:
    # Replace with actual analysis result for Document 2
    st.write("Document 2 Analysis: In-depth analysis uncovers significant themes and patterns...")
else:
    st.write("Click the button to show the analysis for Document 2.")

# Conditional display for Document 3 analysis
if st.session_state.show_analysis_3:
    # Replace with actual analysis result for Document 3
    st.write("Document 3 Analysis: Key themes identified in this research highlight several trends...")
else:
    st.write("Click the button to show the analysis for Document 3.")
