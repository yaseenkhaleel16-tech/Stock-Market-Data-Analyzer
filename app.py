import streamlit as st
from src.analyzer import run_analysis

st.set_page_config(page_title="Stock Market Data Analyzer", page_icon="📈", layout="wide")
st.title("📈 Stock Market Data Analyzer")
st.caption("Educational tool for historical stock-market data analysis.")
ticker = st.text_input("Stock symbol", "RELIANCE.NS").strip().upper()
start = st.text_input("Start date (YYYY-MM-DD)", "")
end = st.text_input("End date (YYYY-MM-DD)", "")

if st.button("Analyze stock", type="primary"):
    if not ticker:
        st.error("Please enter a stock symbol.")
    else:
        try:
            with st.spinner("Collecting and analyzing stock data..."):
                result = run_analysis(ticker, start or None, end or None)
            df = result["data"]
            st.success("Analysis completed.")
            cols = st.columns(3)
            cols[0].metric("Latest close", f'{df["close"].iloc[-1]:.2f}')
            cols[1].metric("Highest close", f'{df["close"].max():.2f}')
            cols[2].metric("Lowest close", f'{df["close"].min():.2f}')
            st.subheader("Closing price and moving averages")
            chart_df = df.set_index("date")[["close", "sma20", "sma50"]]
            st.line_chart(chart_df)
            st.subheader("Daily returns")
            st.bar_chart(df.set_index("date")[["daily_return"]])
            st.subheader("Analysis summary")
            st.dataframe(df.tail(10), use_container_width=True)
            st.info("CSV, text report, and PNG charts have been saved in the outputs folder.")
        except Exception as exc:
            st.error(f"Could not complete analysis: {exc}")
            st.write("Check your stock symbol, date format, and internet connection.")
st.warning("For learning purposes only. This project does not provide investment advice.")
