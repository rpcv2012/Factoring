from fractions import gcd

#useful:
#sys.path.append('FactoringTemp')
#import FactoringTemp
#from FactoringTemp.factors import factors

#import factors
#from factors import factors

#sys.path.append('numbertheory/factoringprimesperfect')

#generates the factors of a number n
def factors(n):
     i = 1
     for i in range (1, n):
                    lst = range (1,n+1)
                    lst = filter(lambda i:gcd (i,n) == i,lst)
     return (lst)
 
