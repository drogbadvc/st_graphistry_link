import streamlit as st
import streamlit.components.v1 as components


def render_form():
    """
    Displays file upload form and options.
    Returns input values.
    """
    with st.form("file_upload_form"):
        uploaded_file = st.file_uploader("Download a CSV file", type="csv")
        keep_unique = st.checkbox("Show only unique links", value=False)
        submitted = st.form_submit_button(label="Generate graph")
    return uploaded_file, keep_unique, submitted


def main_area(graph_url):
    """
        Displays the iframe with the generated graphic.
    """
    components.iframe(src=graph_url, height=1000, scrolling=True)
