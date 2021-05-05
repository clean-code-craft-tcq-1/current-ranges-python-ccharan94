import unittest
import BMSMonitoring

class test_bms_ranges(unittest.TestCase):
  def test_sequence_count(self): #passing test
    self.assertTrue(BMSMonitoring.getRangeCount([3, 3, 5, 4, 10, 11, 12]) == { "3-5" : "4", "10-12" : "3" } )
  
  def test_valid_input(self):    #failing test
    self.assertTrue(BMSMonitoring.isValidInput("3,3,5,4,10,11,12") == True ) #Passes even though string is passed instead of list

if __name__ =='__main__':
  unittest.main()
