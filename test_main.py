import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_func(self) : 
        for n in range(5) : 
            nn=10*n
            for i in range(1,9):
                p, mean_suc, mean_fail = i*0.1, 0, 0 
                for i in range(100) : 
                   nsuc, nfail = repeated_trials(nn,0.5)
                   self.assertTrue( nsuc+nfail==nn, "the number of sucesses+number of failures is not equal to the total number of trials performed" )
                   mean_suc = mean_suc + nsuc
                   mean_fail = mean_fail + nfail 

                mean_suc, mean_fail = mean_suc / 100, mean_fail / 100
                var = nn*p*(1-p)
                bar = np.sqrt(var/100)*st.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean_suc - nn*p )<bar, "you appear to be counting the number of sucesses incorrectly" )
                self.assertTrue( np.fabs( mean_fail - nn*p )<bar, "you appear to be counting the number of failures incorrectly" )
