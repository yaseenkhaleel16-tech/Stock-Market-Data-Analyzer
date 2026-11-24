# Stock Market Data Analyzer

A beginner-friendly Python project that downloads historical stock prices (when internet access is available), calculates basic indicators, creates charts, and writes a report.

## Features
- Yahoo Finance historical data using `yfinance`
- Included sample CSV fallback
- Data cleaning with Pandas
- Daily percentage returns
- 20-day and 50-day simple moving averages
- 20-day rolling volatility
- Highest and lowest closing-price summary
- PNG charts, analyzed CSV, and text report
- Optional Streamlit dashboard

## 1. Install Python
Install Python 3.11 or newer from https://www.python.org/downloads/.
On Windows, tick **Add Python to PATH** during installation.

## 2. Extract the ZIP
Right-click `Stock-Market-Data-Analyzer.zip` and choose **Extract All**.
Open the extracted `Stock-Market-Data-Analyzer` folder.

## 3. Open in VS Code
Install Visual Studio Code from https://code.visualstudio.com/.
Open VS Code → File → Open Folder → select the extracted project folder.

## 4. Open the terminal
In VS Code choose Terminal → New Terminal.

## 5. Create a virtual environment (Windows)
```powershell
py -m venv .venv
.venv\Scripts\activate
```
If `py` does not work, try `python` instead.

## 6. Install project libraries
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Wait until installation finishes.

## 7. Run the Python program
```powershell
python main.py
```
Enter a symbol, for example:
- `RELIANCE.NS` (Reliance Industries, NSE)
- `TCS.NS` (Tata Consultancy Services, NSE)
- `AAPL` (Apple, US market)

For the date prompts, press Enter to use the default one-year period.

## 8. Run the interactive dashboard (optional)
```powershell
streamlit run app.py
```
Your browser should open the dashboard. If it does not, copy the local URL printed in the terminal into your browser.

## 9. Find your results
After a successful run, open:
- `outputs/` — analyzed CSV and text report
- `outputs/charts/` — closing-price, moving-average, and daily-return charts

## CSV fallback
If Yahoo Finance cannot be reached, the program uses `data/sample_stock.csv`. This is a small demonstration dataset, not live market data. To use your own CSV, replace it while keeping columns named `Date`, `Open`, `High`, `Low`, `Close`; `Volume` is optional.

## Common problems
- **'python' is not recognized:** reinstall Python and select Add Python to PATH, then reopen VS Code.
- **No module named ...:** activate `.venv` and run `pip install -r requirements.txt`.
- **No data found:** check the ticker spelling, internet connection, and date range. Try `RELIANCE.NS` or the included CSV fallback.
- **PowerShell blocks activation:** run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again. This changes the policy only for the current terminal session.

## Important
This is an educational project for learning Python and historical data analysis. It is not financial advice and should not be used alone to make investment decisions.
