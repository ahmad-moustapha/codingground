class Polynomial:
    
    def __init__(self, start, end, coefficients ):
        self.start = start
        self.end = end
        self.coefficients = coefficients
    
    def __str__(self):
        return 'Ploynomial: ' + str(self.coefficients) + ' Non-Zero over: (' + str(self.start) + ', ' + str(self.end) + ')'  
    
class Spline:
    
    def __init__(self, degree, polynomials):
        self.polynomials = polynomials
        self.degree = degree
        
    def evalOverInterval(self, start, end):
        for polynomial in self.polynomials:
            if polynomial.start == start and polynomial.end == end:
                return polynomial
        return Polynomial(start, end, [0 for i in range(self.degree+1)]) 
    
    def __str__(self):
        return 'Spline of degree ' + str(self.degree) + ':\n' + str(map(str,self.polynomials))
    
# This functions returns the i-th spline function of degree p defined over the given knots. A spline function is a set of polynomials defined
# over small intervals called knot spans. Consider the spline s = au+b over [0,1) and a'u+b' over [1,2) and zero elsewhere.
def coxDeBoor(knots, i, p):
 
 # According to cox-de-boor recursive formula if p=0 (initial or default case) the spline will be defined as 1 over the corresponding knot span
 # [i,i+1) and zero elsewhere
    if p==0:
        polynomials = [Polynomial(knots[i], knots[i+1], [1])]
        return Spline(0,polynomials)
    
# If p>0

# Repeated Expressions used in calculation, this ease readibility

    R1 = 1.0/(knots[i+p]-knots[i])
    R2 = 1.0/(knots[i+p+1]-knots[i+1])
    UR1 = R1*knots[i]
    UR2 = R2*knots[i+p+1]
    
# According to cox-de-boor a spline of degree p is non-zero over p+1 knot span [i,i+1), ... , [i+p, i+p+1)
# Initilize the polynomials array of the new spline - each polynomial corresponds to a knot span  
    polynomials = [None]*(p+1)   
    
# A spline function in cox-de-boor algo depends on the two previous splines with degree p-1 and index i and i+1    
    prevSpline1 = coxDeBoor(knots,i,p-1)
    prevSpline2 = coxDeBoor(knots,i+1,p-1)
    
# Loop over the knot spans of the spline
    for iter1 in range(0,p+1):

    # Get the polynomial functions corresponding to the splines at  intervals [(i,i+1),...,(i+p,i+p+1)]
        prevSplinePoly1 = prevSpline1.evalOverInterval(knots[i+iter1], knots[i+iter1+1])
        prevSplinePoly2 = prevSpline2.evalOverInterval(knots[i+iter1], knots[i+iter1+1])
        
    # Get the coefficients of the functions
        prevSplineCoef1 = prevSplinePoly1.coefficients
        prevSplineCoef2 = prevSplinePoly2.coefficients
        
    # Initilize the coeffiecient array of the polynomial function of the new spline over the interval (i+iter1,i+iter1+1)
    # A polynomial with degree p have p+1 coefficients
        coefficients = [None]*(p+1)
    
    # Calculate the highest degree of the new spline - it depends on the highest degree coefficient of the previous splines
        coefficients[p] = R1*prevSplineCoef1[prevSpline1.degree] - R2*prevSplineCoef2[prevSpline2.degree]
    
    # Calculate the lowest degree which depends on the lowest degree of the previous spline polynomial function
        coefficients[0] = -UR1*prevSplineCoef1[0] + UR2*prevSplineCoef2[0]
    
    # Calculate the rest of the coefficients where a coefficient k in the new function depends on the coefficients k-1 and k of
    # the previous splines.
        for iter2 in range(1,p):
        
            coefficients[iter2] = R1*prevSplineCoef1[iter2-1] - R2*prevSplineCoef2[iter2-1] - UR1*prevSplineCoef1[iter2] + UR2*prevSplineCoef2[iter2]
    
        polynomials[iter1] = Polynomial(knots[i+iter1], knots[i+iter1+1], coefficients)
    return Spline(p,polynomials)
 
def splineBasis(interval, degree, Knots=null, nbasis):
    # TODO validate input
    
    if isnull(knots):
        nknots = nbasis+degree+1
        lowerBound = interval[0]
        upperBound = interval[1]
        knots=[lowerBound + x*(upperBound-lowerBound)/nknots for x in range(nknots+1)]
    
    
    
    
s = coxDeBoor([0,1,2,3],0,2)
print(s)
