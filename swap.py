def swap_var(var_x,var_y):
    return var_y,var_x
x = 5
y = 10
x, y = swap_var(x, y)
print("x  swapping:", x)
print("y  swapping:", y)
