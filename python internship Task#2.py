# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:56:06 2025

@author: SOFTLINK COMPUTERS
"""

import requests
import json

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, shares, purchase_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'purchase_price': purchase_price}
        print(f"Added {shares} shares of {symbol} at ${purchase_price} per share.")
    
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] > shares:
                self.portfolio[symbol]['shares'] -= shares
                print(f"Removed {shares} shares of {symbol}.")
            else:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
        else:
            print(f"Stock {symbol} not found in portfolio.")
    
    def get_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        try:
            return float(data['Global Quote']['05. price'])
        except KeyError:
            print("Error retrieving stock price. Check API limits or symbol.")
            return None
    
    def portfolio_value(self):
        total_value = 0.0
        for symbol, details in self.portfolio.items():
            stock_price = self.get_stock_price(symbol)
            if stock_price:
                total_value += stock_price * details['shares']
        return total_value
    
    def show_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol, details in self.portfolio.items():
            current_price = self.get_stock_price(symbol)
            if current_price:
                print(f"{symbol}: {details['shares']} shares, Purchase Price: ${details['purchase_price']}, Current Price: ${current_price}")
        print(f"Total Portfolio Value: ${self.portfolio_value():.2f}\n")

# Example Usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    portfolio = StockPortfolio(API_KEY)
    
    portfolio.add_stock("AAPL", 10, 150)
    portfolio.add_stock("TSLA", 5, 700)
    portfolio.show_portfolio()
    
    portfolio.remove_stock("AAPL", 5)
    portfolio.show_portfolio()
