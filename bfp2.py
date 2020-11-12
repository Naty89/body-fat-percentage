"""
This is a class that tells you what your body percentage is
and what category you are in.
It also tells the how many pounds you need to loose to go down a category
and it tells you how much you need to lose to get a six pack
Another thing is it tells you how much you need to workout and for how long you need
to work out for
It will also tell you what kind of diet you should and it would show links that lead you
to some recipes

"""

from math import log10
import pandas as pd


class BodyInfo:
    """
    waist, neck, and hip should be in inches
    height in inches
    weight should be in pounds
    gender should be written in male or female

    """

    def __init__(self, weight, height, gender, age, neck, waist, hip):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.neck = neck
        self.waist = waist
        self.hip = hip

    """
    This method calculates 
    your body fat percentage
    using the U.S Navy method
    """

    def US_Navy_Method(self):
        if self.gender.lower() == 'male':
            return round(86.010 * log10(self.waist - self.neck) - 70.041 * log10(self.height) + 36.76, 1)
        return round(163.205 * log10(self.waist + self.hip - self.neck) - 97.684 * log10(self.height) - 78.387, 1)

    """
    This method calculates your
    body fat percentage using
    the BMI(Body Mass Index) method
    """

    def BMI_Method(self):
        BMI = (self.weight / self.height ** 2) * 703
        if self.gender.lower() == 'male':
            return 1.20 * BMI + 0.23 * self.age - 16.2
        return 1.20 * BMI + 0.23 * self.age - 5.4

    """
    This shows you the body fat 
    categories, and which one your in
    """

    def Body_Fat_Category(self):
        """
        This part of the code figures out the body fat
        percantage using the navy method
        """
        BFP = round(self.US_Navy_Method(), 1)
#         if self.gender.lower() == 'male':
#             BFP = round(86.010 * log10(self.waist - self.neck) - 70.041 * log10(self.height) + 36.76)
#         else:
#             BFP = round(163.205 * log10(self.waist + self.hip - self.neck) - 97.684 * (log10(self.height)) - 78.387)
        """
        This makes a dictionary of the category
        and the body percentage associated with it.
        """
        df = pd.read_csv('BFP_Catergories.csv')
        print(df)
        female = {}
        male = {}
        for i in range(len(df.Description)):
            female[df.Description[i]] = df.Women[i].replace('%', '').replace('+', '').split('-')
        for i in range(len(df.Description)):
            male[df.Description[i]] = df.Men[i].replace('%', '').replace('+', '').split('-')

        """
        This tells what category you are in 
        """
        if self.gender.lower() == 'male':
            for key, value in male.items():
                if BFP > int(value[0]) and BFP < int(value[-1]):
                    return('You are in the {} category'.format(BFP))
        if self.gender.lower() == 'female':
            for key, value in female.items():
                if BFP > int(value[0]) and BFP < int(value[-1]):
                    return('You are in the {} category'.format(key))

   
