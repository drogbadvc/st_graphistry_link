import streamlit as st
from data_processing import load_and_process_file
from graphistry_utils import run_filters
from ui_components import main_area, render_form

# Initial configuration of the Streamlit page
st.set_page_config(layout="wide")


def main():
    st.title("Visualize internal links with Graphistry")
    st.write("""
        Download a CSV file containing the `Source` and `Target` columns 
        (or `Destination`) columns. These columns indicate the relationships between pages on the site.
    """)

    # Form rendering and value retrieval
    uploaded_file, keep_unique, submitted = render_form()

    if submitted and uploaded_file:
        try:
            # File processing and validation
            df = load_and_process_file(uploaded_file, keep_unique)

            if df is not None:
                # Converting to Pandas for Graphistry
                df_pandas = df.to_pandas()

                # Spinner during graph generation
                with st.spinner("Graph generation with Graphistry..."):
                    graph_url = run_filters(df_pandas)

                st.success("Successfully generated graph!")
                main_area(graph_url)
        except Exception as e:
            st.error(f"Error : {e}")
    elif submitted and not uploaded_file:
        st.warning("Please download a file to get started.")


if __name__ == "__main__":
    main()
