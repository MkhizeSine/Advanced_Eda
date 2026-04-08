import streamlit as st
import streamlit as st
import pandas as pd

# Title
st.title("📊 EDA Workshop App")

st.write("Upload your dataset and explore it interactively.")

# File upload
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file, sep=';')

    st.subheader("📌 Data Preview")
    st.dataframe(df.head(23))

    # Info
    st.subheader("ℹ️ Data Info")
    buffer = []
    df.info(buf=buffer)
    st.text("\n".join(buffer))

    # Describe
    st.subheader("📈 Statistical Summary")
    st.write(df.describe())

    # Missing values
    st.subheader("❗ Missing Values")
    st.write(df.isnull().sum())

    # Optional: Profiling
    st.subheader("📊 Automated EDA Reports")

    if st.button("Generate YData Profiling Report"):
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, title="EDA Report", explorative=True)
        profile.to_file("eda_report.html")
        
        with open("eda_report.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=800, scrolling=True)

    if st.button("Generate Sweetviz Report"):
        import sweetviz as sv
        report = sv.analyze(df)
        report.show_html("sweetviz_report.html")

        with open("sweetviz_report.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=800, scrolling=True)

else:
    st.info("Please upload a CSV file to begin.")
