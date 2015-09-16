from collections import OrderedDict
import datetime
from bokeh.charts import TimeSeries, output_file, show
now = datetime.datetime.now()
print type(now)
delta = datetime.timedelta(minutes=1)
dts = [now + delta*i for i in range(5)]
print dts
xyvalues = OrderedDict({'Date': dts})
print xyvalues
y_python = xyvalues['python'] = [2, 3, 7, 5, 26]
y_pypy = xyvalues['pypy'] = [12, 33, 47, 15, 126]
y_jython = xyvalues['jython'] = [22, 43, 10, 25, 26]

ts = TimeSeries(xyvalues, index='Date', title="TimeSeries", legend="top_left",
                ylabel='Languages')

output_file('timeseries.html')
show(ts)
2015-08-21 18:08:06.667000