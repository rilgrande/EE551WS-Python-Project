# EE551WS-Python-Project
Sensor Data Analysis, Manipulation, Export, and Plotting

Roger Il Grande

This project serves to provide an understanding of fundamental data analysis tools available in Python. The problem at hand to solve represents one very common to industry: data coming in from external sensors in an unorganized and un-readable format. Python is very useful for manipulating this type of data and plotting it into simple visual representations.

In my example, I obtained a sensor data file from the Internet (representative of any type of sensor with arbitrary units, txt format) which I reorganized and plotted using the matplotlib and numpy packages. Matplotlib includes several functions to produce scatter plots, bar charts, histograms, etc. Numpy facilitates indexing and sorting of arrays (including multidimensional arrays), performing mathematical operations with arrays, and creating new arrays.

Walking through my code, we begin with importing the two packages mentioned above. Next, we import the sensor data file stored within the same directory as the .py file. We then extract the desired data by column. This step is particularly important for the bigger picture of this exercise – some sensor data may not be applicable to the mission at hand, or may be known to be inaccurate based on the conditions. Both the desired time periods and associated data are extracted in this case, with the average being calculated for the sensor data. The next step is to export the data into a reorganized txt file, with transposed columns to better lay out the data. We then save the data into a new file using the numpy function savetxt.

At this point, the remaining code uses the matplotlib functions to plot the sensor values, and export the plot as a png image. In addition to png file formats, the savefig function also supports formats such as eps, pdf, and svg. The data used in this project shows that the selected sensor (sensor 2) reads discrete values (cyan color) at short time intervals, while the average sensor values (magenta) are spread across a range from approximately 360 to 390 units. There were several useful tutorials and videos I used to help me better understand this project.
