from src.analyzer import run_analysis

def main():
    print("=" * 58)
    print("          STOCK MARKET DATA ANALYZER")
    print("=" * 58)
    print("This educational tool studies historical stock prices.")
    ticker = input("\nEnter stock symbol (example: RELIANCE.NS or AAPL): ").strip().upper()
    if not ticker:
        print("No symbol entered. Exiting.")
        return

    start = input("Start date (YYYY-MM-DD, press Enter for 1 year ago): ").strip() or None
    end = input("End date (YYYY-MM-DD, press Enter for today): ").strip() or None

    try:
        result = run_analysis(ticker=ticker, start=start, end=end)
        print("\nANALYSIS COMPLETE")
        print("-" * 58)
        for key, value in result["summary"].items():
            print(f"{key}: {value}")
        print("\nFiles saved inside the 'outputs' folder.")
        print("Open outputs/charts to see your charts.")
    except Exception as exc:
        print(f"\nSomething went wrong: {exc}")
        print("Check your internet connection, stock symbol, and dates.")
        print("You can also use the sample CSV file explained in README.md.")

if __name__ == "__main__":
    main()
