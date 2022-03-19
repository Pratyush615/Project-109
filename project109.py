from turtle import st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

print("mean: ",mean)
print("median: ",median)
print("mode: ",mode)
print("standard deviation: ",std_dev)

first_stdev_start,first_stdev_end = mean-std_dev, mean+std_dev
second_stdev_start,second_stdev_end = mean-(2*std_dev),mean+(2*std_dev)
third_stdev_start,third_stdev_end = mean-(3*std_dev),mean+(3*std_dev)

fig = ff.create_distplot([data],["reading scores"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.025],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.025],mode="lines",name="1std dev start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.025],mode="lines",name="1std dev end"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.025],mode="lines",name="2std dev start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.025],mode="lines",name="2std dev end"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.025],mode="lines",name="3std dev start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.025],mode="lines",name="3std dev end"))
fig.show()

data_within_1_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
data_within_2_stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
data_within_3_stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print("{}% of data lies within 1 standard deviation".format(len(data_within_1_stdev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(data_within_2_stdev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(data_within_3_stdev)*100.0/len(data)))