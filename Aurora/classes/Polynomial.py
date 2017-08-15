class Polynomial:
    
    def __init__(self, start, end, coefficients ):
    self.start = start
    self.end = end
    coeffiecents = coeffiecents
    
class Spline:
    
    def __init__(self, degree, polynomials):
        self.polynomials = polynomials
        self.degree = degree
        
    def evalOverInterval(start, end):
        for polynomial in self.polynomials:
            if polynomial.start == start and polynomial.end == end:
                return polynomial
        return Polynomial(start, end, [0 for i in range(self.degree)])    
    
# This functions returns the i-th spline function of degree p defined over the given knots. A spline function is a set of polynomials defined
# over small intervals called knot spans. Consider the spline s = au+b over [0,1) and a'u+b' over [1,2) and zero elsewhere.
def coxDeBoor(knots, i, p):
 
 # According to cox-de-boor recursive formula if p=0 (initial or default case) the spline will be defined as 1 over the corresponding knot span
 # [i,i+1) and zero elsewhere
  if p==0:
    return Polynomial(knots[i], knots[i+1], [1])
    
# If p>0


        
    
    
        
    
