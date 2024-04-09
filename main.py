import stock_query
import date
import graph

while True:
    print("Stock Data Visualizer")
    print("--------------------------- \n")

    stock_symbol = input("Enter the stock symbol you are looking for: ").upper()
    chart_type = stock_query.get_chart_type()
    time_series = stock_query.get_time_series()
    start, end = date.main()
    data = stock_query.get_stock_data(time_series, stock_symbol)

    if data is not None:
        graph.generate_graph(data, chart_type, time_series, start, end, stock_symbol)

    response = input("Would you like to view more stock data? Press 'y' to continue: ")
    if response != 'y':
        break
