import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,494,78,77,85,86]
# Convert the list to a numpy array
#speed = numpy.array(speed)


x = numpy.mean(speed)
y = numpy.median(speed)

# Calculate the mode using scipy.stats
mode_ = stats.mode(speed)
#standard dev
STD_DEV = numpy.std(speed)
#Variance 
variance = numpy.var(speed)


#print("Mean speed:", x)
#print("Median speed:", y)
#print("Mode speed:", mode_)
print("Standard Deviation:", STD_DEV)
print("Variance:", variance)


