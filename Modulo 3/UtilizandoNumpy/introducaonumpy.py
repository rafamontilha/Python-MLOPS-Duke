import numpy as np
# Creating an array from list
array_from_list = np.array([1, 2, 3, 2, 6, 1])
# Creating an array from tuple
array_from_tuple = np.array((1, 2, 3, 2, 6, 1))
print(f'Array from list: {array_from_list}')
print(f'Array from tuple: {array_from_tuple}')

# Creating an integer array without specifying dtype
array_1 = np.array([1, 2, 3])
# Creating an integer array with setting dtype to 1-byte integer
array_2 = np.array([1, 2, 3], dtype=np.int8)
print(f'First array dtype: {array_1.dtype}')
print(f'Second array dtype: {array_2.dtype}')

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f'2-dimensional array: \n{array_2d}')

#creating an array with random values
np.random.rand(3,4)
print(f'Random 3x4 array: \n{np.random.rand(3,4)}')

#creating an array with ones like a function
array_ones = np.ones((2, 3))
print(f'Array of ones: \n{array_ones}')
array_zeros = np.zeros((2, 3))
print(f'Array of zeros: \n{array_zeros}')

#a simple sequence of numbers
array_sequence = np.arange(0, 10, 2)
print(f'Array sequence: {array_sequence}')

#using linspace to create an array of 5 numbers between 0 and 1
array_linspace = np.linspace(0, 1, 5)
print(f'Array created with linspace: {array_linspace}')

# Creating an array of integers from 0 to 11 exclusive with step=1
array_1 = np.arange(11)
print(array_1)
# Creating an array of integers from 1 to 11 exclusive with step=1
array_2 = np.arange(1, 11)
print(array_2)
# Creating an array of integers from 0 to 11 exclusive with step=2
array_3 = np.arange(0, 11, 2)
print(array_3)

# Generating 5 equally spaced values between 0 and 1 (inclusive)
array_inclusive = np.linspace(0, 1, 5)
print('Endpoint = True:', array_inclusive)
# Generating 5 equally spaced values between 0 and 1 (exclusive)
array_exclusive = np.linspace(0, 1, 5, endpoint=False)
print('Endpoint = False:', array_exclusive)

# Create an array of even numbers from 2 to 21 exclusive
even_numbers = np.arange(2, 21, 2)
# Create an array of 10 equally spaced numbers between 5 and 6 exclusive
samples = np.linspace(5, 6, 10, endpoint=False)
print(even_numbers)
print(samples)

#Funções de criação de arrays eye()

identity_matrix = np.eye(3)
print(f'Identity matrix: \n{identity_matrix}')
identity_matrix = np.eye(2)
print(f'2x2 identity matrix:\n{identity_matrix}')
# Creating a 4x3 matrix with np.eye()
rectangular_matrix = np.eye(4, 3, dtype=np.int8)
print(f'4x3 matrix:\n{rectangular_matrix}')

# Create 5x2 array with ones for elements with equal row index and column index
matrix = np.eye(5, 2, dtype=np.int8)
print(matrix)

# Сreate an array of fours of size 5
array_fours_1d = np.full(5, 4)
# Сreate an array of fives of shape 4x2
array_fives_2d = np.full((4, 2), 5)
print(f'1D fours array: {array_fours_1d}')
print(f'2D fives array:\n{array_fives_2d}')

# Create an array of zeros of size 5
zeros_array_1d = np.zeros(5)
# Create an array of zeros of shape 2x4
zeros_array_2d = np.zeros((2,4))
# Create an array of ones of size 3
ones_array_1d = np.ones(3)
# create an array of ones of shape 2x3
ones_array_2d = np.ones((2,3))
# Create an array of sevens of shape 2x2
sevens_array_2d = np.full((2,2), 7)
print(f'1D zeros array: {zeros_array_1d}, 1D ones array: {ones_array_1d}')
print(f'2D zeros array:\n{zeros_array_2d}')
print(f'2D ones array:\n{ones_array_2d}')
print(f'2D sevens array:\n{sevens_array_2d}')

# Generating a random number
random_number = np.random.rand()
print(random_number)
# Generating a random 1D array with 5 elements
random_array = np.random.rand(5)
print(random_array)
# Generating a random 2D array (matrix) of shape 4x3
random_matrix = np.random.rand(4, 3)
print(random_matrix)
# Generate a 1D array of random floats in [0, 1) with 4 elements
random_float_array = np.random.rand(4)
print(random_float_array)

# Generating a random integer from 0 to 3 exclusive
random_integer = np.random.randint(3)
print(random_integer)
# Generating a 1D array of random integers in [0, 5) with 4 elements
random_int_array = np.random.randint(5, size=4)
print(random_int_array)
# Generating a 1D array of random integers in [2, 5) with 4 elements
random_int_array_2 = np.random.randint(2, 5, size=4)
print(random_int_array_2)
# Generating a random 2D array of random integers in [1, 6) of shape 4x2
random_int_matrix = np.random.randint(1, 6, size=(4, 2))
print(random_int_matrix)

# Generate a 2D array of random integers in [10, 21) of shape 3x2
random_int_matrix_2 = np.random.randint(10, 21, size=(3, 2))
print(random_int_matrix_2)

array = np.array([9, 6, 4, 8, 10])
# Accessing the first element (positive index)
print(f'The first element (positive index): {array[0]}')
# Accessing the first element (negative index)
print(f'The first element (negative index): {array[-5]}')
# Accessing the last element (positive index)
print(f'The last element (positive index): {array[4]}')
# Accessing the last element (negative index)
print(f'The last element (negative index): {array[-1]}')
# Accessing the third element (positive index)
print(f'The third element (positive index): {array[2]}')
# Accessing the third element (negative index)
print(f'The third element (negative index): {array[-3]}')

# Creating a 5x5 matrix representing stock prices
stock_prices = np.array([
    [150, 130, 140, 150, 160],
    [210, 220, 230, 240, 250],
    [310, 320, 330, 340, 350],
    [410, 420, 430, 440, 450],
    [510, 520, 530, 540, 550]
])
# Retrieve all the stock prices of the first company over five days with a positive index
first_company_prices = stock_prices[0]
# Retrieve the stock price of the third company on the second day with positive indices
third_company_second_day_price = stock_prices[2,1]
# Retrieve the stock price of the last company on the last day with negative indices
last_company_last_day_price = stock_prices[-1,-1]
print(first_company_prices)
print(third_company_second_day_price)
print(last_company_last_day_price)

array = np.array([5, 10, 2, 8, 9, 1, 0, 4])
print(f'Initial array: {array}')
# Slicing from the first element to the last element inclusive with step=2
print(array[::2])
# Slicing from the element at index 4 to the element at index 2 exclusive (step=-1)
print(array[4:2:-1])
# Slicing from the last element to the first element inclusive (reversed array)
print(array[::-1])
# Slicing from the first element to the last inclusive (the same as our array)
print(array[:])

# Sales data for the past week (Monday to Sunday)
weekly_sales = np.array([150, 200, 170, 180, 160, 210, 190])
# Create a slice of weekly_sales with every second day's sales starting from the second day
sales_slice = weekly_sales[1::2]
print(sales_slice)

array_2d = np.array([
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12]
])

# Initial Array
print("Initial array_2d:\n", array_2d)
# Rows from index 1 to the end
print("\narray_2d[1:]:\n", array_2d[1:])
# All rows, first column only
print("\narray_2d[:, 0]:\n", array_2d[:, 0])
# Subarray: rows from 1 to end, columns from 1 to second-to-last
print("\narray_2d[1:, 1:-1]:\n", array_2d[1:, 1:-1])
# All rows except the last, every second column
print("\narray_2d[:-1, ::2]:\n", array_2d[:-1, ::2])
# Third row (index 2) reversed
print("\narray_2d[2, ::-1]:\n", array_2d[2, ::-1])

# Scores of three students in three subjects
student_scores = np.array([[85, 92, 78], [88, 75, 83], [90, 88, 91]])
# Create a slice of student_scores with the scores of the first student in the last two subjects
first_student_last_two_subjects = student_scores[0, 1:]
print(first_student_last_two_subjects)

# Temperatures in three cities (Berlin, Madrid, New York) over three days
# (Monday, Tuesday, Wednesday)
# Each row corresponds to a city, and each column corresponds to a day
# For example, temperatures[0, 1] gives the temperature in Berlin on Tuesday

temperatures = np.array([
   [25, 28, 26],  # Berlin
   [30, 32, 31],  # Madrid
   [22, 21, 23]   # New York
])

#find the temperature on tuesday and wednesday in berlin and wednesday in madrid
print (temperatures[0, 1:]) # Berlin on Tuesday and Wednesday
print (temperatures[1, 2]) # Madrid on Wednesday