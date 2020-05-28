import matplotlib
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure

import urllib, base64
import datetime, time
import numpy as np
import io

def plot_page(Entry, start_time):

	interval = list(start_time + i[0] for i in Entry.values_list('interval'))      
	temp = Entry.values_list('temperature')
	light = Entry.values_list('illumination')

	fig = Figure(figsize=(10,10), constrained_layout=True, dpi=100)
	axs = fig.subplots(2,1)

	axs[0].plot_date(interval, temp, 'r-', xdate=True, tz='Europe/Moscow')
	axs[1].plot_date(interval, light, 'y-', xdate=True, tz='Europe/Moscow')
	axs[0].set_title('Ambient temperature') 
	axs[1].set_title('Degree of illumination')
      
	buf = io.BytesIO()
	fig.savefig(buf, format = 'png')
	string =  base64.b64encode(buf.getbuffer()).decode("ascii")
	return urllib.parse.quote(string)
