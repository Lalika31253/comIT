# Operator Overloading
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)

from math import gcd

class Fraction:

  def __init__(self, num, den):
    common = gcd(abs(num), abs(den))
    self.num = num // common
    self.den = den // common

  def __add__(self, other):
      if isinstance(other, Fraction):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
      
  def __sub__(self, other):
     if isinstance(other, Fraction):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
     
  def __mul__(self, number):
     if isinstance(number, Fraction):
        return Fraction(self.num * number.num, self.den * number.den)
     return Fraction(self.num * number, self.den)
  
  def __truediv__(self, number):
     if isinstance(number, Fraction):
        return Fraction(self.num * number.den, self.den * number.num) 
     return Fraction(self.num, self.den * number)   
        

  def __str__(self):
        return f"{self.num}/{self.den}"


fraction1 = Fraction(1, 3)
fraction2 = Fraction(1, 6)

result1 = fraction1 + fraction2
result2 = fraction1 - fraction2
result3 = fraction1 * 2 + fraction2 
result4 = fraction1 + fraction2 / 3  

print(result1)  # 1/2
print(result2)  # 1/6
print(result3)  # 5/6
print(result4)  #7/18

