import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Don"],
    "Age": [25, 30, 35, 34],
    "City": ["New York", "Los Angeles", "Chicago", "Santiago"]
}
df = pd.DataFrame(data)

# Custom CSS for styling the table
table_style = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            font-size: 16px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
    </style>
"""

# Convert DataFrame to HTML and display in Streamlit
table_html = df.to_html(index=False, escape=False)

st.markdown(table_style + table_html, unsafe_allow_html=True)
