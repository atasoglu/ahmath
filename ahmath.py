"""
__doc__
version 0.1
29.10.19
ahmath -- easy, simple, effective math and diff. equations tools
"""
from matplotlib.pyplot import plot, title, xlabel, ylabel, legend, show

class basic:
    # basic tools
    
    pi = 3.141592653589793
    e = 2.718281828459045
    
    def __init__(self):
        pass
    
    @classmethod
    def sum(self, *args):
        if len(args) == 1:
            res = 0
            for i in args[0]: res += i
            return res
        elif len(args) > 1:
            return self.sum(args)
        else:
            return None

    @classmethod
    def fact(self, x):
        if x > 1:
            return x * self.fact(x-1)
        else:
            return 1

    @classmethod
    def deg_to_rad(self, degree):

        if type(degree) is int or type(degree) is float:
            return (self.pi / 180) * degree

        elif type(degree) is list:
            return [self.deg_to_rad(deg) for deg in degree]

        else:
            return None

    @classmethod
    def rad_to_deg(self, radian):

        if type(radian) is int or type(radian) is float:
            return (180 / self.pi) * radian

        elif type(radian) is list:
            return [self.rad_to_deg(rad) for rad in radian]

        else:
            return None
        
    @classmethod
    def diff(self, x):
        return [x[i] - x[i-1] for i in range(1, len(x))]
    
    @classmethod
    def dy(self, y, x):
        dy = self.diff(y)
        dx = self.diff(x)
        return [y/x for y, x in zip(dy, dx)]
    
    @classmethod
    def dydx(self, y, x):
        dy, dx = [], x[:-1]
        y = self.diff(y)
        x = self.diff(x)
        for Y, X in zip(y, x):
            dy.append(Y/X)
        return dy, dx
    
    @classmethod
    def intg(self, x0, x1, equation = None):
        pass    
    
    @classmethod
    def arange(self, start, end, step):
        if end > start:
            arr = [start]
            while  arr[-1] + step <= end:
                arr.append(arr[-1] + step)
            return arr
        else:
            return None
            
    
class ahmath(basic):
    def __init__(self):
        pass

    @classmethod
    def taylor(self, initc = [0, 0, 0] , h = 0.1, iteration = 100, equation = lambda x,y: None):
        # initc = initial conditions of [x0, y0, y'0]
        """
        y = []
        xi = initc[0]
        yi = initc[1]
        dyi = initc[2]
        for i in range(iteration):
            if i == 0:
                y.append(equation(xi, yi))
        """
        pass
    
    @classmethod
    def euller(self, initc = [0, 0] , h = 0.1, iteration = 100, equation = None):
        # initc: initial conditions of [x0, y0]
        y = [initc[1]]
        xi = initc[0]
        for i in range(iteration):
            y.append(y[i] + equation(xi, y[i]) * h)
            xi += h
        return y
    
    @classmethod
    def runge_kutta(self, initc = [0, 0], h = 0.1, iteration = 100, equation = None):
        # initc: initial conditions of [x0, y0]
        y = [initc[1]]
        xi = initc[0]
        for i in range(iteration):
            k = [1, 2, 2, 1]
            k[0] = k[0] * h * equation(xi, y[i])
            k[1] = k[1] * h * equation(xi + h/2, y[i] + k[0]/2)
            k[2] = k[2] * h * equation(xi + h/2, y[i] + k[1]/2)
            k[3] = k[3] * h * equation(xi + h, y[i] + k[2])
            y.append(y[i] + super().sum(k) / 6)
            xi += h
        return y
    
class Taylor:
    def __init__(self):
        pass

class Euller:
    
    def __init__(self, dy = [], dx = [], h = 0.1, iteration = 0):
        self.set_dydx(dy, dx, h, iteration)
        self.y = []
        
        
    def solve(self, y0 = 0):
        self.y.append(y0)
        for i in range(self.iteration-1):
            self.y.append(self.y[-1] + self.dy[i] * self.h)

    def draw(self, **kwargs):
        if len(kwargs) < 1:
            kwargs.update({'color':'r', 'label':'solution', 'title':'euller method'})
        else:
            kwargs
        plot(self.dx[:self.iteration],
             self.y, 
             color = kwargs['color'], 
             label = kwargs['label'])
        title(kwargs['title'])
        xlabel('x-axis')
        ylabel('y-axis')
        legend()
        show()
    
    # getters ...
    def get_x(self):
        return self.dx
    
    def get_y(self):
        return self.y
    
    # setters ...
    def set_dydx(self, dy, dx, h, iteration):
        self.dy = dy
        self.dx = dx
        self.h = h
        if iteration is 0 or iteration > len(dy):
            self.iteration = len(dy)
        else:
            self.iteration = iteration                

class Runge_Kutta(basic):
    
    def __init__(self, dy = [], dx = [], h = 0.1, iteration = 0):
        self.set_dydx(dy, dx, h, iteration)
        self.y = []
        
    def solve(self, y0):
        pass
        
    def draw(self, **kwargs):
        pass
    
    # setters ...
    def set_dydx(self, dy, dx, h, iteration):
        self.dy = dy
        self.dx = dx
        self.h = h
        if iteration is 0 or iteration > len(dy):
            self.iteration = len(dy)
        else:
            self.iteration = iteration
            
    # getters ...
    def get_y(self):
        return self.y