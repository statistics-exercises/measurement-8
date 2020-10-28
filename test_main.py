import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_averageVolumes(self):
        myav = averageVolumes( 10, radii )
        volumes = (4/3)*np.pi*radii*radii*radii
        for i in range(10) : 
            bav = sum( volumes[i*20:(i+1)*20] ) / 20 
            self.assertTrue( np.abs(myav[i]-bav)<1e-7, "The function called averageVolumes is not working" )
            
            
    def test_averageVolumes(self):
        myav = averageVolumesFromAverageRadii( 10, radii )
        for i in range(10) : 
            bav = sum( radii[i*20:(i+1)*20] ) / 20 
            self.assertTrue( np.abs(myav[i]-(4/3)*np.pi*bav*bav*bav)<1e-7, "The function called averageVolumesFromAverageRadii is not working" )
    
