# Graphistry + Screaming Frog Visualization Tool

This project provides an interactive tool for visualizing relationships between entities using [Graphistry](https://hub.graphistry.com/). It is designed for CSV data exported from Screaming Frog, containing `Source` and `Target` columns, it leverages Streamlit for a user-friendly web interface.

---

## Features

- Upload and process CSV files with `Source` and `Target` (or `Destination`) columns.
- Visualize relationships using Graphistry.
- Filter and display unique links.
- Scalable processing for large datasets with Polars or Pandas.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/drogbadvc/st_graphistry_link.git
   cd graphistry-project
   ```

2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   ```
   
## Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```
2. Open your browser and go to http://localhost:8501.

3. Upload a CSV file and generate a Graphistry visualization.

## Project Structure

* main.py: The main Streamlit app.
* graphistry_utils.py: Helper functions for Graphistry visualization.
* data_processing.py: Functions for cleaning and validating CSV data.
* ui_components.py: Streamlit UI elements.
* requirements.txt: Dependencies for the project.