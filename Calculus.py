import math


def f1(x):
    return math.sin(x) / x
# test: lim(f1, 0) expected limit: 1
# f1(0) crashes with ZeroDivisionError


def f2(x):
    if x == 1:
        return 5
    return x + 1
# test: lim(f2, 1) expected limit: 2 (f2(1) is 5, which should be ignored


def f3(x):
    return abs(x) / x   # -1 for x < 0, +1 for x > 0
# test: lim(f3, 0)  no limit 

def f4(x):
    return 1 / x
# test: lim(f4, 0)  no finite limi

def lim(func, a):
    left_approaches = a - 0.001
    right_approaches = a + 0.001

    try:
        left_limit = func(left_approaches)
        right_limit = func(right_approaches)
        # Replace Code with Loops soon
        if math.isclose(left_limit, right_limit, abs_tol=0.01): # Approximation Fix
            limit = (left_limit + right_limit) / 2
            return "The Limit is " + str(limit)
        else:
            return ("The Left Limit is " + str(left_limit) + "\n" # Incase of left_limit != right_limit
                    "The Right Limit is " + str(right_limit) + "\n"
                    "No General Limit")
    except ZeroDivisionError:
        return "PlaceHolder"


print(lim(f1, 0))
print(lim(f2, 1))
print(lim(f3, 0))
print(lim(f4, 0))
print(lim(lambda x: x / 2 + 0.25, 1))   # true limit is 0.75
print("test")


# Next Steps: Replace the classical limit approximation with a loop approximation for greater accuracy and handling for Vertical Asymptote functions.
