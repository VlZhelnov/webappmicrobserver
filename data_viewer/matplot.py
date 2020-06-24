import matplotlib
from matplotlib.figure import Figure

import urllib, base64
import io

def plot_page(Entry, start_time):

	interval = Entry.values_list('interval')      
	temp = Entry.values_list('temperature')
	light = Entry.values_list('illumination')

	fig = Figure(figsize=(10,10), constrained_layout=True, dpi=100)
	axs = fig.subplots(2,1)

	axs[0].plot(interval, temp, 'r-')
	axs[1].plot(interval, light, 'y-')
	axs[0].set_title('Ambient temperature')
	axs[1].set_title('Degree of illumination')
	axs[0].set_ylabel('Temperature ($^\circ$C)', color="r")
	axs[1].set_ylabel('Lighting, %', color="y")
	axs[0].set_xlabel('time (s)')
	axs[1].set_xlabel('time (s)')
        
	buf = io.BytesIO()
	fig.savefig(buf, format = 'png')
	string =  base64.b64encode(buf.getbuffer()).decode("ascii")
	return urllib.parse.quote(string)
