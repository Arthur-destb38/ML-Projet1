"""Script minimal pour télécharger des historiques depuis Yahoo Finance et sauver en CSV.
Usage:
    python scripts/fetch_yahoo.py --tickers AAPL MSFT SPY --start 2015-01-01 --end 2025-01-01 --interval 1d

Le script crée un dossier `data/raw` et télécharge chaque ticker en `<ticker>.csv`.
"""




import argparse
import os
from pathlib import Path
import yfinance as yf
import pandas as pd
from datetime import date



DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_ticker(ticker: str, start: str, end: str, interval: str):
    print(f"Downloading {ticker} {start} -> {end} interval={interval}")
    obj = yf.Ticker(ticker)
    df = obj.history(start=start, end=end, interval=interval, auto_adjust=False)
    if df.empty:
        print(f"Warning: no data for {ticker}")
        return
    # ensure datetime index
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    out = DATA_DIR / f"{ticker}.csv"
    df.to_csv(out)
    print(f"Saved {out} rows={len(df)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", nargs='+', default=["SPY"],
                        help="Tickers à télécharger (par ex. SPY AAPL).")
    parser.add_argument("--tickers-file", default=None,
                        help="Fichier texte avec un ticker par ligne.")
    parser.add_argument("--start", default="2000-01-01")
    parser.add_argument("--end", default=date.today().isoformat())
    parser.add_argument("--interval", default="1d", choices=["1d","1wk","1mo","1m","5m","15m","1h"]) 
    args = parser.parse_args()
    tickers = args.tickers
    if args.tickers_file:
        p = Path(args.tickers_file)
        if p.exists():
            tickers = [line.strip() for line in p.read_text().splitlines() if line.strip()]
        else:
            print(f"Tickers file {args.tickers_file} not found, using --tickers/defaults")
    for t in tickers:
        fetch_ticker(t, args.start, args.end, args.interval)
