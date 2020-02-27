from unittest import TestCase
import random
import math
import task


class Test(TestCase):
    def test_radius_to_area(self):
        random.seed()
        for x in range(1000):
            testInput = random.randint(0, 1000) + random.random() # set up variables
            testResult = task.radiusToArea(testInput) # call function
            self.assertEqual(testResult, math.pi * math.pow(testInput, 2)) # assert accurate performance of function
        pass
