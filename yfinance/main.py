from yfinanceFunc import yfinanceFunc


if __name__ == '__main__':
    spy = yfinanceFunc('SPY')
    spy.price_volumn_chart_plot()
    print()
