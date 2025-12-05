import yfinance as yf
import pandas as pd
import time
from datetime import datetime

TICKER = "CL=F"
CHECK_INTERVAL = 60  # Check every 60 seconds

print(f"--- Starting Sentinel for {TICKER} ---")
print("Press Ctrl+C to stop.")

def analyze_market():
    # 1. Get Data
    # auto_adjust=True helps clean up the data format
    df = yf.download(TICKER, period="5d", interval="15m", progress=False, auto_adjust=True)
    
    # 2. Fix Data Structure (The "Patch")
    # If yfinance returns multi-level columns, we flatten them
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 3. Calculate Volatility
    # We use .item() to ensure we get a single float value, not a Series
    last_close = df['Close'].iloc[-1]
    
    # Calculate Returns
    df['Returns'] = df['Close'].pct_change()
    volatility = df['Returns'].rolling(window=5).std().iloc[-1]
    
    # 4. Timestamp
    now = datetime.now().strftime("%H:%M:%S")
    
    # 5. The "Quant" Report
    # We force conversion to float just to be 100% safe
    print(f"[{now}] Price: ${float(last_close):.2f} | Volatility: {float(volatility):.5f}")

    # 6. Simple Alert Logic
    if float(volatility) > 0.002:
        print(f"🚨 VOLATILITY SPIKE DETECTED! ({volatility:.5f})")

while True:
    try:
        analyze_market()
        time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print(f"Error fetching data: {e}")
        time.sleep(CHECK_INTERVAL)