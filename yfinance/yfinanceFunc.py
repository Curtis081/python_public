import yfinance as yf
from matplotlib import pyplot as plt


class yfinanceFunc:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.stock_ticker = yf.Ticker(self.stock_id)

    def price_volumn_chart_plot(self):
        history_data = self.stock_ticker.history(period="max")
        plt.rc('figure', figsize=(18, 8))
        fig, axes = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 1]})
        fig.tight_layout(pad=3)

        date = history_data.index
        close = history_data['Close']
        vol = history_data['Volume']

        plot_price = axes[0]
        plot_price.plot(date, close, color='blue', linewidth=2, label='Price')
        plot_vol = axes[1]
        plot_vol.bar(date, vol, width=15, color='red')
        plt.show()
