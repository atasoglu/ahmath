from basic import *
import matplotlib.pyplot as plt

# sum
print(
    'sum([0, 1, 2, ..., 10]) =',
    sum( list( range(0, 11) )),
)

# fact
print(
    'fact(5) = 5! =',
    fact(5)
)

# power
print(
    'pow(2, 4) = 2^4 =',
    pow(2, 4) 
)

# deg_to_rad(float)
print(
    'deg_to_rad(60) => 60 deg =',
    deg_to_rad(60), 'rad',
)

# deg_to_rad(list)
print(
    'deg_to_rad([30, 60, 90]) => [30, 60, 90] deg =',
    deg_to_rad([30, 60, 90]), 'rad'
)

# rad_to_deg(float)
print(
    'rad_to_deg(3.1415) => 3.1415 rad =',
    rad_to_deg(3.1415), 'deg',
)

# rad_to_deg(list)
print(
    'rad_to_deg([0.1, 0.2, 0.3]) => [0.1, 0.2, 0.3] rad =',
    rad_to_deg([0.1, 0.2, 0.3]), 'deg'
)

# arange
print(
    'arange(0, 10, 0.5) = [0, 0.5, 1, 1.5, ..., 9.5] =',
    arange(0, 10, 0.5)
)

fig, plots = plt.subplots(nrows=1, ncols=3)
my_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(
    'my_list =', my_list
)

# diff
print(
    'diff( my_list ) = ',
    diff( my_list )
)

plots[0].grid(True)
plots[0].plot(my_list, 'b-^', label='my_list')
plots[0].plot( diff(my_list), 'r-*', label='diff(my_list)' )
plots[0].legend()

# dy
print(
    'dy(my_list, 5) = ',
    dy( my_list, 2 )
)

plots[1].grid(True)
plots[1].plot(my_list, 'b-^', label='my_list')
plots[1].plot( dy(my_list, 2), 'r-*', label='dy(my_list, 2)' )
plots[1].legend()



# dydx
print(
    'dydx(my_list, list( range( len( my_list ) ) ) = ',
    dydx( my_list, list( range( len(my_list) ) ) )
)


_dy, _dx = dydx(my_list, list(range(len(my_list))))

plots[2].grid(True)
plots[2].plot(my_list, 'b-^', label='my_list')
plots[2].plot( _dx, _dy, 'r-*', label='dydx')
plots[2].legend()


plt.tight_layout()
plt.show()





