# Write a class called Investment with ﬁelds called principal and interest. 
# The constructor should set the values of those ﬁelds. 
# There should be a method called value_after that returns the value of the investment after n years.
#  The formula for this is p(1+i)n, where p is the principal, and i is the interest rate. 
# It should also use the special method __str__ so that printing the object will result in something like below:

#Principal - $1000.00, Interest rate - 5.12%


class Investment:
    def __init__(self,principal,interest,years):
        self.principal=principal
        self.interest=interest
        self.years=years
   
    def value_after(self):
       
        return self.principal*(self.interest+1)*self.years
    def __str__(self):
        return f'Principal- $',self.principal, 'Interest rate',self.interest, '%'


p=float(input('$'))
i=float(input('%'))
y=int(input())

val= Investment(p,i,y)
print(val.__str__())
#print(val.value_after)
