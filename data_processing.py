import polars as pl
import streamlit as st


def clean_column_names(df):
    """
    Replaces spaces or invalid characters with underscores in column names.
    """
    return df.rename({col: col.replace(' ', '_').replace('.', '_') for col in df.columns})


def validate_columns(df):
    """
    Checks that the necessary columns are present and returns the appropriate DataFrame.
    """
    if 'Source' not in df.columns:
        st.error("The file must contain a `Source` column.")
        return None

    if 'Target' not in df.columns and 'Destination' not in df.columns:
        st.error("The file must contain a `Target` or `Destination` column..")
        return None

    # Rename columns to match Graphistry's expectations
    if 'Target' in df.columns:
        df = df.rename({'Source': 'source', 'Target': 'target'})
    else:
        df = df.rename({'Source': 'source', 'Destination': 'target'})
    return df


@st.cache_data
def load_and_process_file(file, keep_unique):
    """
    Loads a CSV file, optimizes processing of critical columns,
    and applies a unique filter if necessary.
    """
    # Initial file loading with Polars
    df = pl.read_csv(file, low_memory=True)

    # Cleaning column names
    df = clean_column_names(df)

    # Column validation
    df = validate_columns(df)
    if df is None:
        raise ValueError("The file does not contain the required columns.")

    # Transformation into lazy mode for optimization
    lazy_df = df.lazy()

    # Apply sorting to the 'source' column to speed up queries
    lazy_df = lazy_df.sort('source')

    # If requested, apply filter to display unique links only
    if keep_unique:
        lazy_df = lazy_df.unique(subset=['source', 'target'])

    # Execute deferred operations and convert to normal DataFrame
    optimized_df = lazy_df.collect()

    return optimized_df
