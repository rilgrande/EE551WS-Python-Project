import numpy as np # for importing and analyzing
import matplotlib.pyplot as plt # for plotting

# load the sample data file
data_file = np.loadtxt('data_file.txt', delimiter=',') # importing the data from file into python

time = data_file[:,0] # first column, all of the rows and first column, pulling out all time data
time = time - time[0] # a djusting time to subtract the first time value (0 index)
time_minutes = time/60.0 # converting time to minutes

sensors = data_file[:,1:5] # pulling out the good sensor data in columns 2-5 only
# filters out 'bad' sensor data from the data set


# calculate the average of the sensor readings for second sensor argument
average = np.mean(sensors,axis=1) # over the 2nd dimension, don't trust one individual sensor


# exporting the data
# stack time and avg as column vectors
reformatted_data = np.vstack((time,sensors.T,average)) # vertically stacked/columns (time column, sensor value column, average column)
# .T transposes the column data into row form, stacked on top of each other in rows

reformatted_data = reformatted_data.T # inverted again into 3 columns (time, sensor, average)

np.savetxt('export_from_python.txt',reformatted_data,delimiter=',') # save as a new text file




# everything above was manipulating the raw sensor data and exporting the new file



# generate a figure
plt.figure(1)
plt.plot(time_minutes,sensors[:,1],'co') # cyan circles for the second sensor
plt.plot(time_minutes,average,'m.') # magenta dots, utilizing the minutes adjusted time variable

# add text labels to the plot
plt.legend(['Sensor 2','Average Sensors 1-4'])
plt.title('ESM Sensor Data')
plt.xlabel('Time (min)')
plt.ylabel('Sensor Values')

# save the figure as a PNG file
plt.savefig('my_Python_plot.png')
# show the figure on the screen (pauses execution until closed)
plt.show()
