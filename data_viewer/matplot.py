from matplotlib import pyplot as plt
from datetime import timedelta as td
from datetime import datetime as dt
from django.conf import settings
import pytz
import urllib, base64
import io


def utc_to_local(utc_dt):
	utc_dt = dt.now() if utc_dt is None else utc_dt
	local_tz = pytz.timezone(settings.TIME_ZONE)
	local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
	return local_tz.normalize(local_dt) 

def plot_page(Entry, start_time):

	start_time = utc_to_local(start_time)
	interval = [start_time + td(seconds = i[0]) for i in Entry.values_list('interval')]
	temp = Entry.values_list('temperature')
	light = Entry.values_list('illumination')
	
	fig, ax1 = plt.subplots(figsize=(10,5))
	color = 'tab:red'
	ax1.set_xlabel('Time (s)')
	ax1.set_ylabel('Temperature ($^\circ$C)', color=color)
	ax1.plot_date(interval, temp, xdate=True, fmt="-", color=color)
	ax1.tick_params(axis='y', labelcolor=color)
	color = 'tab:purple'
	ax2 = ax1.twinx() 
	ax2.set_ylabel('Lighting, %', color=color)
	ax2.plot_date(interval, light, xdate=True, fmt="-", color=color)
	ax2.tick_params(axis='y',   labelcolor=color)
	ax1.grid()
	fig.tight_layout()
	buf = io.BytesIO()
	fig.savefig(buf, format = 'png')
	string =  base64.b64encode(buf.getbuffer()).decode("ascii")
	return urllib.parse.quote(string)
	
