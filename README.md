# Block average volumes

In the last exercise you should have seen that all the estimates of the average radius were different so we are still sampling a random variable when we calculate a mean.  With this in mind lets now use what we have learned to sample our two measures for the average volume of the bubbles:

![](https://render.githubusercontent.com/render/math?math=V=\frac{1}{n}\sum_{i=1}^n\frac{4}{3}\pi\R^3\qquad\textrm{and}\qquad\V'=\frac{4}{3}\pi\left(\frac{1}{n}\sum_{i=1}^{n}R_i\right)^3)

__To complete this exercise I want you to use the block averaging technique that you learned about in the previous exercise to calculate ten estimates for V and ten estimates for V'__.  You will need to complete two functions that are similar to the `blockAverages` function that you wrote for the previous task. Both of these function takes two arguments in input:

1. `nblocks` - is the number of averages that you want to calculate from the data set.  In other words, this is the number of blocks that you want to divide your data set into.
2. `data` - is a NumPy array that contains the data set from which the block averages are calculated.

The first of these functions `averageVolumes` should return a NumPy array with `nblocks` elements.  The zeroth element of this array should contain an estimate for V that is computed from the first `len(data)/nblocks`  data points of `data`.  The second element of this array will then contain an estimate for V that is computed from the second `len(data)/nblocks`  data points of `data` and so on. 

The second of these functions `averageVolumesFromAverageRadii` should return a NumPy array with `nblocks` elements.  The zeroth element of this array should contain an estimate for V' that is computed from the first `len(data)/nblocks`  data points of `data`.  The second element of this array will then contain an estimate for V' that is computed from the second `len(data)/nblocks`  data points of `data` and so on.   

If you complete the exercise correctly a graph showing the various estimates of V and V' that you obtained will be generated.  The estimates of V are shown in blue, while the estimates of V' are shown in red.  Given the graph do you think that the same distribution is being sampled by both expressions?
