import matplotlib.pyplot as plt
import numpy as np

def averageVolumes( nblocks, data ) :
  # You should add code here to calcualte the block 
  # averages from the data points in data.  Each 
  # even value in the output array should be an esimtate
  # of V.  The odd elements of data should be estimates of V'
  averages = np.zeros( nblocks )
  
def averageVolumesFromAverageRadii( nblocks, data ) :
  # You should add code here to calcualte the block 
  # averages from the data points in data.  Each 
  # even value in the output array should be an esimtate
  # of V.  The odd elements of data should be estimates of V'
  averages = np.zeros( nblocks )
  
# The code from here on does not need to be modified.  It 
# just uses your function to calculate some block averges for the volume and 
# then plots these values on a graph.  Estimates of V are shown in blue, while
# estimates of V' are shown in red.
radii = np.loadtxt("bubbles.dat)
plt.plot( np.linspace(1,10,10), averageVolumes(10,radii), 'bo' )
plt.plot( np.linspace(1,10,10), averageVolumesFromAverageRadii(10,radii), 'ro' )
plt.savefig("averages.png")
