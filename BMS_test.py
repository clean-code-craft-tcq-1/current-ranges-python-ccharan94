import unittest
import BMSMonitoring

class test_bms_ranges(unittest.TestCase):
  def test_sequence_count(self):
    self.assertTrue(BMSMonitoring.getSequenceCount([3, 3, 5, 4, 10, 11, 12]) == { "3-5" : "4", "10-12" : "3" }
  
  def test_valid_input(self)
    self.assertTrue(BMSMonitoring.isValidInput([]) == True )

if __name__ =='__main__':
  unittest.main()