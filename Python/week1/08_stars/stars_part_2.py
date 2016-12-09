# Modify the function above. Allow a list containing integers and strings to be
#passed to the  draw_stars() function. When a string is passed, instead of
#displaying *, display the first letter of the string according to the example
#below. You may use the .lower() string method for this part.
#
# For example:
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(x):
    for i in range(0,len(x)):
        if type(x[i]) is int:
            stars = x[i] * "*"
            print stars
        else:
            word_len = len(x[i])
            letter = x[i][0]
            print (letter.lower() * word_len)

draw_stars(x)
