import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv

st.title("📊 EDA App")

# Upload file
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# Optional: load default file
if uploaded_file is None:
    st.info("Using default dataset (Book2.csv)")
    try:
        df = pd.read_csv("Book2.csv", sep=';')
    except:
        st.warning("No default file found. Please upload one.")
        st.stop()
else:
    df = pd.read_csv(uploaded_file, sep=';')

# Show data
st.subheader("Preview")
st.dataframe(df.head())

# Info
st.subheader("Info")
st.write(df.describe())

# Missing values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Reports
st.subheader("Reports")

if st.button("Generate YData Report"):
    profile = ProfileReport(df, explorative=True)
    profile.to_file("report.html")
    st.success("Report generated: report.html")

if st.button("Generate Sweetviz Report"):
    report = sv.analyze(df)
    report.show_html("sweetviz.html")
    st.success("Report generated: sweetviz.html")
