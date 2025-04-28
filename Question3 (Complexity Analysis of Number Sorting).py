import random
import matplotlib.pyplot as plt
import numpy as np

# Complexity analysis of number sorting algorithm

# Function to count number of primitive operations in number sorting
# Takes 2 input, namely numbers and LENGTH
# numbers is the unsorted list of positive integer with fixed length (an array of type string), LENGTH is the fixed
# length (number of digits) of each number
# Returns the number of primitive operations required to sort the list of numbers
def count_primitive_operation_in_number_sorting(numbers, LENGTH):
    # Initialize primitive operation counter
    numberOfPrimitiveOperations = 0

    # Number sorting algorithm start

    # Initialize start
    # Initialize 2 arrays with 10 elements (which is also an array)
    array1 = [[], [], [], [], [], [], [], [], [], []]
    array2 = [[], [], [], [], [], [], [], [], [], []]
    numberOfPrimitiveOperations += 2    # 2 array initialization operations
    # Initialize end

    # Iteration start

    # For the first pass, need to look at the last digit (position of length - 1)
    position = LENGTH - 1
    numberOfPrimitiveOperations += 2    # 1 subtraction operation and 1 assignment operation

    # First pass start
    # Pass through all number in the list of numbers inputted
    for number in numbers:
        # Append the number to the corresponding cell in array 1 based on the last digit of the number
        if number[position] == '0':
            array1[0].append(number)
            numberOfPrimitiveOperations += 2    # 1 comparison operation and 1 assignment operation
        elif number[position] == '1':
            array1[1].append(number)
            numberOfPrimitiveOperations += 3    # 2 comparison operations and 1 assignment operation
        elif number[position] == '2':
            array1[2].append(number)
            numberOfPrimitiveOperations += 4    # 3 comparison operations and 1 assignment operation
        elif number[position] == '3':
            array1[3].append(number)
            numberOfPrimitiveOperations += 5    # 4 comparison operations and 1 assignment operation
        elif number[position] == '4':
            array1[4].append(number)
            numberOfPrimitiveOperations += 6    # 5 comparison operations and 1 assignment operation
        elif number[position] == '5':
            array1[5].append(number)
            numberOfPrimitiveOperations += 7    # 6 comparison operations and 1 assignment operation
        elif number[position] == '6':
            array1[6].append(number)
            numberOfPrimitiveOperations += 8    # 7 comparison operations and 1 assignment operation
        elif number[position] == '7':
            array1[7].append(number)
            numberOfPrimitiveOperations += 9    # 8 comparison operations and 1 assignment operation
        elif number[position] == '8':
            array1[8].append(number)
            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
        else:
            array1[9].append(number)
            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
    # First pass end

    # Reorder the numbers in a sorted list after the first pass if the numbers has only 1 digit (last position is 0)
    if position == 0:
        numberOfPrimitiveOperations += 1    # 1 comparison operation

        # Reorder start (if length == 1)
        sortedNumbers = []
        numberOfPrimitiveOperations += 1    # 1 assignment operation

        # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell in
        # array 1
        for cellNumber in range(10):
            for number in array1[cellNumber]:
                sortedNumbers.append(number)
                numberOfPrimitiveOperations += 1    # 1 assignment operation
        # Reorder end (if length == 1)

    else:
        numberOfPrimitiveOperations += 1    # 1 comparison operation

        # Continue for subsequent pass

        # Holds the number of passes for future reference
        numberOfPasses = 1
        numberOfPrimitiveOperations += 1    # 1 assignment operation

        while position > 0:
            numberOfPrimitiveOperations += 1    # 1 comparison operation

            # Increment number of passes (go to the next pass) and decrement position (move one position forward)
            numberOfPasses = numberOfPasses + 1
            position = position - 1
            numberOfPrimitiveOperations += 4 # 2 assignment operation, 1 addition operation and 1 subtraction operation

            # For the second pass (or 4th pass, 6th pass, 8th pass, ...)
            # For all passes that read from array 1 and write to array 2
            if numberOfPasses % 2 == 0:
                numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

                # Re-initialize array 2 because array 2 should be cleared because this pass should write to array 2
                array2 = [[], [], [], [], [], [], [], [], [], []]
                numberOfPrimitiveOperations += 1    # 1 assignment operation

                # Second pass (or 4th pass, 6th pass, 8th pass, ...) start
                # Reads from the first cell to the last cell in array 1
                for cellNumber in range(10):
                    # Reads every number in each cell in array 1
                    for number in array1[cellNumber]:
                        # Appends the number to corresponding cell in array 2 based on the second last (or 4th last,
                        # 6th last, 8th last, ...) digit of the number
                        if number[position] == '0':
                            array2[0].append(number)
                            numberOfPrimitiveOperations += 2    # 1 comparison operation and 1 assignment operation
                        elif number[position] == '1':
                            array2[1].append(number)
                            numberOfPrimitiveOperations += 3    # 2 comparison operations and 1 assignment operation
                        elif number[position] == '2':
                            array2[2].append(number)
                            numberOfPrimitiveOperations += 4    # 3 comparison operations and 1 assignment operation
                        elif number[position] == '3':
                            array2[3].append(number)
                            numberOfPrimitiveOperations += 5    # 4 comparison operations and 1 assignment operation
                        elif number[position] == '4':
                            array2[4].append(number)
                            numberOfPrimitiveOperations += 6    # 5 comparison operations and 1 assignment operation
                        elif number[position] == '5':
                            array2[5].append(number)
                            numberOfPrimitiveOperations += 7    # 6 comparison operations and 1 assignment operation
                        elif number[position] == '6':
                            array2[6].append(number)
                            numberOfPrimitiveOperations += 8    # 7 comparison operations and 1 assignment operation
                        elif number[position] == '7':
                            array2[7].append(number)
                            numberOfPrimitiveOperations += 9    # 8 comparison operations and 1 assignment operation
                        elif number[position] == '8':
                            array2[8].append(number)
                            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
                        else:
                            array2[9].append(number)
                            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
                # Second pass (or 4th pass, 6th pass, 8th pass, ...) end

            # For the third pass (or 5th pass, 7th pass, 9th pass, ...)
            # For all passes that read from array 2 and write to array 1
            else:
                numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

                # Re-initialize array 1 because array 1 should be cleared because this pass should write to array 1
                array1 = [[], [], [], [], [], [], [], [], [], []]
                numberOfPrimitiveOperations += 1    # 1 assignment operation

                # Third pass (or 5th pass, 7th pass, 9th pass, ...) start
                # Reads from the first cell to the last cell in array 2
                for cellNumber in range(10):
                    # Reads every number in each cell in array 2
                    for number in array2[cellNumber]:
                        # Appends the number to the corresponding cell in array 1 based on the third last (or 5th last,
                        # 7th last, 9th last, ...) digit of the number
                        if number[position] == '0':
                            array1[0].append(number)
                            numberOfPrimitiveOperations += 2    # 1 comparison operation and 1 assignment operation
                        elif number[position] == '1':
                            array1[1].append(number)
                            numberOfPrimitiveOperations += 3    # 2 comparison operations and 1 assignment operation
                        elif number[position] == '2':
                            array1[2].append(number)
                            numberOfPrimitiveOperations += 4    # 3 comparison operations and 1 assignment operation
                        elif number[position] == '3':
                            array1[3].append(number)
                            numberOfPrimitiveOperations += 5    # 4 comparison operations and 1 assignment operation
                        elif number[position] == '4':
                            array1[4].append(number)
                            numberOfPrimitiveOperations += 6    # 5 comparison operations and 1 assignment operation
                        elif number[position] == '5':
                            array1[5].append(number)
                            numberOfPrimitiveOperations += 7    # 6 comparison operations and 1 assignment operation
                        elif number[position] == '6':
                            array1[6].append(number)
                            numberOfPrimitiveOperations += 8    # 7 comparison operations and 1 assignment operation
                        elif number[position] == '7':
                            array1[7].append(number)
                            numberOfPrimitiveOperations += 9    # 8 comparison operations and 1 assignment operation
                        elif number[position] == '8':
                            array1[8].append(number)
                            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
                        else:
                            array1[9].append(number)
                            numberOfPrimitiveOperations += 10   # 9 comparison operations and 1 assignment operation
                # Third pass (or 5th pass, 7th pass, 9th pass, ...) end

        # Iteration end

        # Reorder start
        sortedNumbers = []
        numberOfPrimitiveOperations += 1    # 1 assignment operation

        # After the second pass (or 4th pass, 6th pass, 8th pass, ...)
        # After all passes that write to array 2
        if numberOfPasses % 2 == 0:
            numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

            # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell
            # in array 2
            for cellNumber in range(10):
                for number in array2[cellNumber]:
                    sortedNumbers.append(number)
                    numberOfPrimitiveOperations += 1    # 1 assignment operation

        # After the third pass (or 5th pass, 7th pass, 9th pass, ...)
        # After all passes that write to array 1 (except the first pass)
        else:
            numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

            # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell
            # in array 1
            for cellNumber in range(10):
                for number in array1[cellNumber]:
                    sortedNumbers.append(number)
                    numberOfPrimitiveOperations += 1    # 1 assignment operation
        # Reorder end

    # Number sorting algorithm end

    return numberOfPrimitiveOperations

# Function to randomly generate a list of numbers with a fixed length
# Takes 2 inputs, N and LENGTH
# N is the number of numbers in the list, LENGTH is the fixed length (number of digits) in each number
# Returns a list of numbers (in an array of type string)
def generate_random_list_of_numbers(N, LENGTH):
    # Initialize an empty list of numbers
    numbers = []

    # Generate N numbers
    for _ in range(N):
        #Initialize a variable to store the number
        number = ''

        # Generate a number with LENGTH number of digits
        for _ in range(LENGTH):
            # Generate a random integer ranged from 0 to 9
            digit = random.randint(0, 9)

            # Convert the integer to string
            digitStr = str(digit)

            # Append the digit to number
            number = number + digitStr

        # Append the number to the main list
        numbers.append(number)

    return numbers

# Experiment start
# Number of digits (length) = 5 (Fixed variable)
LENGTH = 5

# Generate a random list of 50 numbers with 5 digits
numbers_N50 = generate_random_list_of_numbers(50, LENGTH)

# Generate a random list of 100 numbers with 5 digits
numbers_N100 = generate_random_list_of_numbers(100, LENGTH)

# Generate a random list of 150 numbers with 5 digits
numbers_N150 = generate_random_list_of_numbers(150, LENGTH)

# Generate a random list of 200 numbers with 5 digits
numbers_N200 = generate_random_list_of_numbers(200, LENGTH)

# Generate a random list of 250 numbers with 5 digits
numbers_N250 = generate_random_list_of_numbers(250, LENGTH)

# Generate a random list of 300 numbers with 5 digits
numbers_N300 = generate_random_list_of_numbers(300, LENGTH)

# Generate a random list of 350 numbers with 5 digits
numbers_N350 = generate_random_list_of_numbers(350, LENGTH)

# Generate a random list of 400 numbers with 5 digits
numbers_N400 = generate_random_list_of_numbers(400, LENGTH)

# Generate a random list of 450 numbers with 5 digits
numbers_N450 = generate_random_list_of_numbers(450, LENGTH)

# Generate a random list of 500 numbers with 5 digits
numbers_N500 = generate_random_list_of_numbers(500, LENGTH)

# Array of N (Manipulated variable)
array_N = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Initialize array of number of primitive operations (Observed variable)
array_numberOfPrimitiveOperations = []

# Count the number of primitive operations for sorting 50 numbers
numberOfPrimitiveOperations_N50 = count_primitive_operation_in_number_sorting(numbers_N50, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N50)

# Count the number of primitive operations for sorting 100 numbers
numberOfPrimitiveOperations_N100 = count_primitive_operation_in_number_sorting(numbers_N100, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N100)

# Count the number of primitive operations for sorting 150 numbers
numberOfPrimitiveOperations_N150 = count_primitive_operation_in_number_sorting(numbers_N150, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N150)

# Count the number of primitive operations for sorting 200 numbers
numberOfPrimitiveOperations_N200 = count_primitive_operation_in_number_sorting(numbers_N200, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N200)

# Count the number of primitive operations for sorting 250 numbers
numberOfPrimitiveOperations_N250 = count_primitive_operation_in_number_sorting(numbers_N250, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N250)

# Count the number of primitive operations for sorting 300 numbers
numberOfPrimitiveOperations_N300 = count_primitive_operation_in_number_sorting(numbers_N300, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N300)

# Count the number of primitive operations for sorting 350 numbers
numberOfPrimitiveOperations_N350 = count_primitive_operation_in_number_sorting(numbers_N350, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N350)

# Count the number of primitive operations for sorting 400 numbers
numberOfPrimitiveOperations_N400 = count_primitive_operation_in_number_sorting(numbers_N400, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N400)

# Count the number of primitive operations for sorting 450 numbers
numberOfPrimitiveOperations_N450 = count_primitive_operation_in_number_sorting(numbers_N450, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N450)

# Count the number of primitive operations for sorting 500 numbers
numberOfPrimitiveOperations_N500 = count_primitive_operation_in_number_sorting(numbers_N500, LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N500)
# Experiment end

# Print the fixed variable, the manipulated variable and the observed variable
print(f'Fixed variable: Number of digits (LENGTH): {LENGTH}')
print(f'Manipulated variable: Number of numbers (N): {array_N}')
print(f'Observed variable: Number of primitive operations: {array_numberOfPrimitiveOperations}')

# Plot the graph of number of primitive operations vs number of numbers (N)
# The manipulated variable (x)
N = np.array(array_N)

# The observed variable (y)
numberOfPrimitiveOperations = np.array(array_numberOfPrimitiveOperations)

# Plot the line
plt.plot(N, numberOfPrimitiveOperations)

# Specify the label of the x-axis
plt.xlabel('N')

# Specify the label of the y-axis
plt.ylabel('Number of primitive operations')

# Specify the title of the graph
plt.title('Graph of Number of Primitive Operations vs N for Number Sorting Algorithm')

plt.show()
