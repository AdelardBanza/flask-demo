import Quandl
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Spectral6, RdYlGn4

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  # Read the query string to get the name of the object
  if "symbol" not in request.args:
      # When the symbol is missing return the empty template
      return render_template('index.html')

  # Getting a list of the attributes to show
  features =request.args.getlist('features')

  # Symbol to query
  stock_name = request.args["symbol"]
  quandl_stock_name = "WIKI/{}".format(stock_name)

  # Requesting data from Quandl using the authtoken

  # Creating bokeh graphs
  p = figure(x_axis_type="datetime", plot_width=700)

  # Show plots
  for i_f, f in enumerate(features):
      p.line(dat.index, dat[f], line_width=2, color=RdYlGn4[i_f], legend=f)

  # Graph components
  script, div = components(p)

  # Variables to include in the template
  return render_template('index.html', stock_name = stock_name, dat_script = script, dat_div = div)

if __name__ == '__main__':
  app.run(debug=True)
