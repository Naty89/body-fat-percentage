import pandas as pd
import math
class BodyFatPercentage():


	#height in inches
	#weight in pounds
	#gender should be male or female
	#waist circumference in inches
	#neck circumference in inches
	#hip cirumference in inches
	def __init__(self, height, weight, gender, age, waist, neck, hip):
		self.height = height
		self.weight = weight
		self.gender = gender
		self.age = age
		self.waist = waist
		self.hip = hip

	def FatPercentage(self):
		#BMI = Body Mass Index
		BMI = (((self.weight-20)/self.height**2)*703)
		if self.gender.lower() == 'male':
			return "{}%".(str(round((86.010 * math.log10(self.waist-self.neck)) - 70.041 * (math.log10(self.height)+30.30))))
		else:
			return "{}%".format(str(round((163.205 * math.log10(self.waist+self.hip)) - self.neck - 97.684 * math.log10(self.height)-104.912)))

	def IdealBodyFatChart(self):
		if self.gender.lower() == 'female':
			return pd.read_csv('bodydatawomen.csv') 
		else:
			return pd.read_csv('bodydatamen.csv')

	# def CaloriestoBurn(self):
	# 	def analayze_dict(self): 
	# 		if self.gender.lower() == 'male':
	# 			df = pd.read_csv('bodydatamen.csv')
	# 		else:
	# 			df = pd.read_csv('bodydatawomen.csv')

	# 		count = 0
	# 		dicti = {}
	# 		for i in range(df.shape[0]):
	# 			dicti[count] = [int(i) for i in df.iloc[count,1].replace('%','').replace('>','').split('-')]
	# 			count += 1
	# 		return dicti

	# 	def category_down(self):
	# 		if self.gender.lower()=='male':
	# 			b = round((1.20 * ((self.weight)/self.height**2)*703) + (0.23 * self.age)-16.2)
	# 		else:
	# 			b = round((1.20 * ((self.weight)/self.height**2)*703) + (0.23 * self.age)-5.4)
	# 		for i in analayze_dict().values():
	# 			if i[0] <= b and i[-1] >= b:
	# 				p = [k for k in analayze_dict() if analayze_dict()[k] == i]
	# 			else:
	# 				p = [4]
	# 		return analayze_dict()[p[0]-1][-1]

	# 	def amount_of_pounds(self):
	# 		x = 0
	# 		if self.gender.lower() == 'male':
	# 			e = round((1.20* ((self.weight)/self.height**2)*703) + (0.23 * self.age)-16.2)
	# 			for i in range(self.weight):
	# 				if e == category_down():
	# 					return x
	# 				x += 4
	# 				e = round((1.20* ((self.weight-x)/self.height**2)*703) + (0.23 * self.age)-16.2)
	# 		else:
	# 			e = round((1.20* ((self.weight)/self.height**2)*703) + (0.23 * self.age)-5.4)
	# 			for i in range(self.weight):
	# 				if e == category_down():
	# 					return x
	# 				x += 4
	# 				e = round((1.20* ((self.weight-x)/self.height**2)*703) + (0.23 * self.age)-5.4)
	# 	return amount_of_pounds()

	# # def Diet_Exercise(self):
	# # passdef


x = BodyFatPercentage(65,136, 'Male', 15, 32, 13, 31)

print(x.FatPercentage())
print(x.IdealBodyFatChart())
