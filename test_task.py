from unittest import TestCase
import random
import math
import task


class Test(TestCase):
    def test_radius_to_area(self):
        random.seed()
        for x in range(1000):
            testInput = random.randint(0, 1000) + random.random()  # set up variables
            testResult = task.radiusToArea(testInput)  # call function
            self.assertEqual(testResult, math.pi * math.pow(testInput, 2))  # assert accurate performance of function
        pass

    def test_first_last(self):
        random.seed()

        # test length of 0
        testList = []
        self.assertListEqual(task.firstLast(testList), testList)

        # test length of 1
        testList = ['a']
        self.assertListEqual(task.firstLast(testList), testList)

        # test random length greater than 1
        testList = []
        for x in range(1000):
            listLen = random.randint(2, 1000)
            for x in range(listLen):
                testList.append(random.randint(0, 1000))
            listCopy = testList.copy()
            del listCopy[1:len(testList) - 1]
            self.assertListEqual(task.firstLast(testList), listCopy)
        pass
