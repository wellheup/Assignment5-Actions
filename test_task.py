from unittest import TestCase
import random
import math
import task
import datetime
from datetime import date


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

    def test_time_span(self):
        random.seed()
        for x in range(10):
            testDates = []
            for y in range(2):  # make 2 random dates
                testYear = (random.randint(datetime.MINYEAR, datetime.MAXYEAR))
                testMonth = random.randint(1, 12)
                testDay = 0
                if [1, 3, 5, 7, 8, 10, 12].count(testMonth) > 0:  # months w/ 31
                    testDay = random.randint(1, 31)
                elif [4, 6, 9, 10].count(testMonth) > 0:
                    testDay = random.randint(1, 31)
                else:
                    testDay = random.randint(1, 28)
                testDates.append(date(testYear, testMonth, testDay))
            testDelta = abs(testDates[0] - testDates[1])
            self.assertTrue(task.timeSpan(testDates[0], testDates[1]) == testDelta.days)
        pass
