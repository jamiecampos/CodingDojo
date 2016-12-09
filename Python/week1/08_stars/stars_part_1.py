# Create a function called  draw_stars() that takes a list of numbers and prints
#out  *. For example:
#
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following in when invoked:
# ****
# ******
# *
# ***
# *****
# *******
# *************************

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(x):
    for i in range(0,len(x)):
        stars = x[i] * "*"
        print stars

draw_stars(x)
