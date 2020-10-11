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

    """
    This method calculates the amount of 
    pounds you need to lose to go down a category.
    
    I am going to be using three function inside
    this method so that it is more organized
    the three functions will one that finds what category
    your in, secong will find what category is down and BFP
    to be in that category, the third one calculates the how
    pounds you need to lose.
    """
    def Pounds_To_Lose(self):

        """
        This function tells you what category your
        are in
        """
        def category_in():
            """
            This part of the code calls out the US_Navy_Method method
            to get the BFP
            """
            BFP = round(self.US_Navy_Method(), 1)
            """
            This makes a dictionary of the category
            and the body percentage associated with it.
            """
            df = pd.read_csv('BFP_Catergories.csv')
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
                        return(key)
            if self.gender.lower() == 'female':
                for key, value in female.items():
                    if BFP > int(value[0]) and BFP < int(value[-1]):
                        return(key)

        """
        This function tells you what category is below.
        Example:
        If you are in the Fitness category then the category
        below you is Athelete category.
        """
        def category_below():
            """
            This makes a dictionary of the category
            and the body percentage associated with it.
            """
            df = pd.read_csv('BFP_Catergories.csv')
            female = {}
            male = {}
            for i in range(len(df.Description)):
                female[df.Description[i]] = df.Women[i].replace('%', '').replace('+', '').split('-')
            for i in range(len(df.Description)):
                male[df.Description[i]] = df.Men[i].replace('%', '').replace('+', '').split('-')

            y = list(female.keys())
            x = list(male.keys())
            if self.gender == 'male':
                for i in range(len(x)):
                    if x[i] == category_in():
                        return int(male[x[i-1]][-1])
            else:
                for i in range(len(y)):
                    if y[i] == category_in():
                        return int(female[y[i-1]][-1])


        """
        This tells you how many pounds you need to loose 
        to go down a category.
        """
        def pounds_to_lose():
            pre_bfp = round(self.US_Navy_Method(), 1)
            af_bfp = round(self.US_Navy_Method(), 1)
            cb = category_below()
            if self.gender.lower() == 'male':
                if pre_bfp <= 5:
                    "You shouldn't be losing any more weight."
                else:
                    while af_bfp > cb:
                        af_bfp -= 0.2
                    return "You have to lose {} pounds".format(round(round(round(pre_bfp-round(af_bfp, 1), 1)/0.2)*0.8))
            else:
                if pre_bfp <= 13:
                    "You shouldn't be losing any more weight."
                else:
                    while af_bfp > cb:
                        af_bfp -= 0.2
                    return "You have to lose {} pounds".format(round(round(round(pre_bfp-round(af_bfp, 1), 1)/0.2)*0.8))



        return(pounds_to_lose())
        
        

x = BodyInfo(146, 65.5, 'male', 40, 12.5, 36.5, 36.5)
print(x.Pounds_To_Lose())
