import streamlit as st
import pandas as pd
import sweetviz as sv

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 Exploratory Data Analysis App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';')

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head(20))

    # Summary statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    # Missing values
    st.subheader("Missing Values")
    missing = df.isnull().sum()
    st.dataframe(missing)

    # Bar chart (Streamlit built-in)
    st.subheader("Missing Values Bar Chart")
    st.bar_chart(missing)

    # Correlation (Streamlit built-in)
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        st.subheader("Correlation Table")
        st.dataframe(numeric_df.corr())

    # Sweetviz Report
    st.subheader("📈 Sweetviz Report")

    if st.button("Generate Sweetviz Report"):
        with st.spinner("Generating report..."):
            report = sv.analyze(df)

            # Save report to temp file
            tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
            report.show_html(tmp_file.name)

            # Read and display
            with open(tmp_file.name, 'r', encoding='utf-8') as f:
                html_data = f.read()

            components.html(html_data, height=800, scrolling=True)

            # Clean up temp file
            os.unlink(tmp_file.name)

else:
    st.info("Please upload a CSV file to begin analysis.")
