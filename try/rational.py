
class Rational1():
    def __init__(self,num,den):   #定义有理数 num/den
        self.num=num
        self.den=den
    
    def plus(self,another):       #两有理数加法
        num=self.num*another.den+self.den*another.num
        den=self.den*another.den
        return Rational1(num,den)

    def print(self):     #打印有理数
        print(str(self.num)+"/"+str(self.den))

a=Rational1(3,5)
b=Rational1(4,7)
Rational1.print(a)
Rational1.print(b)
Rational1.print(Rational1.plus(a,b))