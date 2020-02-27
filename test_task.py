from unittest import TestCase
import random
import math
import task
import datetime


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
        for x in range(1000):
            testDates = []
            for y in range(2): # make 2 random dates
                testDates.append(datetime.date(1, 1, 1))
                testDates[0].replace(year = random.randint(datetime.MINYEAR, datetime.MAXYEAR))
                testDates[0].replace(month = random.randint(1, 12))
                if [1, 3, 5, 7, 8, 10, 12].count(testDates[0].month) > 0: # months w/ 31
                    testDates[0].replace(day = random.randint(1, 31))
                elif [4, 6, 9, 10].count(testDates[0].month) > 0:
                    testDates[0].replace(day=random.randint(1, 31))
                else:
                    testDates[0].replace(day=random.randint(1, 28))
            self.assertTrue(task.timeSpan(testDates[0], testDates[1]) == (testDates[0] - testDates[1]).days)
        pass
