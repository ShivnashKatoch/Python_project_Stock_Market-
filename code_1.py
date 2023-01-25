# install these two before running code 
# open this link for using code in Google Colab : https://colab.research.google.com/drive/1MNryEMXc3ACcuPGIpY7Gcb5OY5sNpv7Y?usp=sharing    
# pip install plotly
# pip install yfinance


# Raw Package (creating environment)
import numpy as nb
import pandas as pd

#Data Source(taking stock data from yahoo finance)
import yfinance as yf

#Data viz(use to plot the graph)
import plotly.graph_objs as go
def show():
  #Interval required 1 minute
  data = yf.download(tickers=stock_name, period='1d', interval='1m')

  #declare figure
  fig = go.Figure()

  #Candlestick In financial technical analysis, a candlestick pattern is a movement in prices shown graphically on a candlestick chart that some believe can predict a particular market movement
  fig.add_trace(go.Candlestick(x=data.index,
                  open=data['Open'],
                  high=data['High'],
                  low=data['Low'],
                  close=data['Close'], name = 'market data'))

  # Add titles
  fig.update_layout(
      title='live share price evolution',
      yaxis_title='Stock Price (USD per Shares)')

  # X-Axes
  fig.update_xaxes(
      rangeslider_visible=True,
      rangeselector=dict(
          buttons=list([
              dict(count=15, label="15m", step="minute", stepmode="backward"),
              dict(count=45, label="45m", step="minute", stepmode="backward"),
              dict(count=1, label="HTD", step="hour", stepmode="todate"),
              dict(count=3, label="3h", step="hour", stepmode="backward"),
              dict(step="all")
          ])
      )
  )

  #Show
  fig.show()
p=1
while p :

  print(""" ======Stock Menu=======

    1. Display all available Stocks
    2. Request any Stock
    3. Exit
            """)
  choice=int(input("Enter Choice:"))
  if choice==1:
    print("""Major Companys
      Amazon   -  amzn
      YouTube  -   you
      Apple    -  aapl
      Uber     -  uber
      Google   - googl""")
    stock_name = input('Enter the ticker of stock: ')
    show()
    
  elif choice==2:
    stock_name = input('Enter the correct ticker of stock (of your choice): ')
    show()
      
  elif choice==3: 
    break 
    print("Exiting........ ")       
  else :
    print("Wrong choice........ ")
exit()