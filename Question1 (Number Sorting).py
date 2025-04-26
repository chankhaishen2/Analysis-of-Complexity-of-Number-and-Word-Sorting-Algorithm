# Number sorting algorithm
print('Number sorting')

# Asks the fixed length of all numbers (which will be used to check against the numbers inputted by the user)
# Note: All numbers in the list should be of the same length
while True:
    try:
        # Checks whether the length inputted is an integer
        LENGTH = int(input('Enter the fixed length of all numbers: '))

        # Checks whether the length inputted is smaller than 1
        if LENGTH < 1:
            print('The length must be at least 1.')
            continue

        break

    except:
        print('The length must be an integer.')
        continue

# Initialize an array to hold the numbers inputted by the user
numbers = []

# Asks the user to input the list of numbers to be sorted
# Note: All numbers must be positive integers with the fixed length as specified in the above input
while True:
    userInput = input('Enter "finish" if the list is finish or enter the next number in the list: ')

    # Ends the while loop if the list of numbers is finish
    if userInput.strip().lower() == 'finish':
        break

    # Checks whether the length of the input equals to the specified length
    if len(userInput) != LENGTH:
        print(f'The length of the input must be equal to the fixed length specified ({LENGTH}).')
        continue

    # Checks whether the input only consists of number
    onlyContainNumber = True

    for position in range(len(userInput)):
        if userInput[position] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('The input must only contain number.')
            onlyContainNumber = False
            break

    if not onlyContainNumber:
        continue

    numbers.append(userInput)
    print('The number is accepted.')

# Prints out the initial list of numbers (unsorted)
print('The list of numbers accepted: ')
for number in numbers:
    print(number)

# Number sorting algorithm start

# Initialize start
# Initialize 2 arrays with 10 elements (which is also an array)
array1 = [[], [], [], [], [], [], [], [], [] ,[]]
array2 = [[], [], [], [], [], [], [], [], [], []]
# Initialize end

# Iteration start

# For the first pass, need to look at the last digit (position of length - 1)
position = LENGTH - 1

# First pass start
# Pass through all number in the list of numbers inputted
for number in numbers:
    # Append the number to the corresponding cell in array 1 based on the last digit of the number
    if number[position] == '0':
        array1[0].append(number)
    elif number[position] == '1':
        array1[1].append(number)
    elif number[position] == '2':
        array1[2].append(number)
    elif number[position] == '3':
        array1[3].append(number)
    elif number[position] == '4':
        array1[4].append(number)
    elif number[position] == '5':
        array1[5].append(number)
    elif number[position] == '6':
        array1[6].append(number)
    elif number[position] == '7':
        array1[7].append(number)
    elif number[position] == '8':
        array1[8].append(number)
    else:
        array1[9].append(number)
# First pass end

# Reorder the numbers in a sorted list after the first pass if the numbers has only 1 digit (last position is 0)
if position == 0:

    # Reorder start (if length == 1)
    sortedNumbers = []

    # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell in
    # array 1
    for cellNumber in range(10):
        for number in array1[cellNumber]:
            sortedNumbers.append(number)
    # Reorder end (if length == 1)

    # Prints out the sorted list and then end
    print('The sorted list of numbers: ')
    for number in sortedNumbers:
        print(number)

else:
    # Continue for subsequent pass

    # Holds the number of passes for future reference
    numberOfPasses = 1

    while position > 0:
        # Increment number of passes (go to the next pass) and decrement position (move one position forward)
        numberOfPasses = numberOfPasses + 1
        position = position - 1

        # For the second pass (or 4th pass, 6th pass, 8th pass, ...)
        # For all passes that read from array 1 and write to array 2
        if numberOfPasses % 2 == 0:
            # Re-initialize array 2 because array 2 should be cleared because this pass should write to array 2
            array2 = [[], [], [], [], [], [], [], [], [], []]

            # Second pass (or 4th pass, 6th pass, 8th pass, ...) start
            # Reads from the first cell to the last cell in array 1
            for cellNumber in range(10):
                # Reads every number in each cell in array 1
                for number in array1[cellNumber]:
                    # Appends the number to corresponding cell in array 2 based on the second last (or 4th last,
                    # 6th last, 8th last, ...) digit of the number
                    if number[position] == '0':
                        array2[0].append(number)
                    elif number[position] == '1':
                        array2[1].append(number)
                    elif number[position] == '2':
                        array2[2].append(number)
                    elif number[position] == '3':
                        array2[3].append(number)
                    elif number[position] == '4':
                        array2[4].append(number)
                    elif number[position] == '5':
                        array2[5].append(number)
                    elif number[position] == '6':
                        array2[6].append(number)
                    elif number[position] == '7':
                        array2[7].append(number)
                    elif number[position] == '8':
                        array2[8].append(number)
                    else:
                        array2[9].append(number)
            # Second pass (or 4th pass, 6th pass, 8th pass, ...) end

        # For the third pass (or 5th pass, 7th pass, 9th pass, ...)
        # For all passes that read from array 2 and write to array 1
        else:
            # Re-initialize array 1 because array 1 should be cleared because this pass should write to array 1
            array1 = [[], [], [], [], [], [], [], [], [], []]

            # Third pass (or 5th pass, 7th pass, 9th pass, ...) start
            # Reads from the first cell to the last cell in array 2
            for cellNumber in range(10):
                # Reads every number in each cell in array 2
                for number in array2[cellNumber]:
                    # Appends the number to the corresponding cell in array 1 based on the third last (or 5th last,
                    # 7th last, 9th last, ...) digit of the number
                    if number[position] == '0':
                        array1[0].append(number)
                    elif number[position] == '1':
                        array1[1].append(number)
                    elif number[position] == '2':
                        array1[2].append(number)
                    elif number[position] == '3':
                        array1[3].append(number)
                    elif number[position] == '4':
                        array1[4].append(number)
                    elif number[position] == '5':
                        array1[5].append(number)
                    elif number[position] == '6':
                        array1[6].append(number)
                    elif number[position] == '7':
                        array1[7].append(number)
                    elif number[position] == '8':
                        array1[8].append(number)
                    else:
                        array1[9].append(number)
            # Third pass (or 5th pass, 7th pass, 9th pass, ...) end

    # Iteration end

    # Reorder start
    sortedNumbers = []

    # After the second pass (or 4th pass, 6th pass, 8th pass, ...)
    # After all passes that write to array 2
    if numberOfPasses % 2 == 0:
        # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell
        # in array 2
        for cellNumber in range(10):
            for number in array2[cellNumber]:
                sortedNumbers.append(number)

    # After the third pass (or 5th pass, 7th pass, 9th pass, ...)
    # After all passes that write to array 1 (except the first pass)
    else:
        # The list of numbers is already sorted in ascending order by reading from the first cell to the last cell
        # in array 1
        for cellNumber in range(10):
            for number in array1[cellNumber]:
                sortedNumbers.append(number)
    # Reorder end

    # Prints out the sorted list and then end
    print('The sorted list of numbers: ')
    for number in sortedNumbers:
        print(number)

# Number sorting algorithm end
