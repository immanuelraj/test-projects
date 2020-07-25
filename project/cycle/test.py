import unittest
from cycle.models import Frame, HandleBarWithBrake, Seating

class CycleTests(unittest.TestCase):

    def test_func_1(self):
        frame = Frame.object.create(model_no = 1234, price_from='2014-01-31' , price_to='2015-01-31' , price = 24.45)
        frame.model_no = 24224
        self.assertEqual(frame.model_no, 24224)

    def test_func_2(self):
        handle_bar_with_brake = HandleBarWithBrake.object.create(model_no = 1234, price_from='2014-01-31' , price_to='2015-01-31' , price = 24.45)
        handle_bar_with_brake.price_from = '2013-01-31'
        self.assertEqual(handle_bar_with_brake.price_from, '2013-01-31')

    def test_func_3(self):
        seating = Seating.object.create(model_no = 1234, price_from='2014-01-31' , price_to='2015-01-31' , price = 24.45)
        seating.price_to = '2016-01-31'
        self.assertEqual(seating.price_to, '2016-01-31')

if __name__ == "__main__":
    unittest.main()