import random
import numpy as np
import matplotlib.pyplot as plt

# Complexity analysis of word sorting algorithm

# Function to count number of primitive operation in word sorting
# Takes 2 input, namely words and MAXIMUM_LENGTH
# words is the unsorted list of words (lower case character string) with different lengths smaller than or equal to the
# maximum length, MAXIMUM_LENGTH is the maximum length (number of characters) of each word
# Returns the number of primitive operations required to sort the list of words
def count_primitive_operation_in_word_sorting(words, MAXIMUM_LENGTH):
    # Initialize primitive operation counter
    numberOfPrimitiveOperations = 0

    # Word sorting algorithm start

    # Initialize start
    # Initialize 2 arrays with 27 elements (which is also an array)
    array1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
              []]
    array2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
              []]
    numberOfPrimitiveOperations += 2    # 2 array initialization operations
    # Initialize end

    # Iteration start

    # For the first pass, need to look at the last character (position of length - 1)
    position = MAXIMUM_LENGTH - 1
    numberOfPrimitiveOperations += 2    # 1 subtraction operation and 1 assignment operation

    # First pass start
    # Pass through all words in the list of words inputted
    for word in words:
        # Append the word to the corresponding cell in array 1 based on the last character of the word
        # If the word is shorter than the currently scanned position (length < position + 1), then append the word to
        # cell 0 (shorter strings are sorted before all longer strings)
        if len(word) < position + 1:
            array1[0].append(word)
            numberOfPrimitiveOperations += 4    # 1 function call, 1 addition, 1 comparison, 1 assignment
        elif word[position] == 'a':
            array1[1].append(word)
            numberOfPrimitiveOperations += 5    # 1 function call, 1 addition, 2 comparisons, 1 assignment
        elif word[position] == 'b':
            array1[2].append(word)
            numberOfPrimitiveOperations += 6    # 1 function call, 1 addition, 3 comparisons, 1 assignment
        elif word[position] == 'c':
            array1[3].append(word)
            numberOfPrimitiveOperations += 7    # 1 function call,  1 addition, 4 comparisons, 1 assignment
        elif word[position] == 'd':
            array1[4].append(word)
            numberOfPrimitiveOperations += 8    # 1 function call, 1 addition, 5 comparisons, 1 assignment
        elif word[position] == 'e':
            array1[5].append(word)
            numberOfPrimitiveOperations += 9    # 1 function call, 1 addition, 6 comparisons, 1 assignment
        elif word[position] == 'f':
            array1[6].append(word)
            numberOfPrimitiveOperations += 10   # 1 function call, 1 addition, 7 comparisons, 1 assignment
        elif word[position] == 'g':
            array1[7].append(word)
            numberOfPrimitiveOperations += 11   # 1 function call, 1 addition, 8 comparisons, 1 assignment
        elif word[position] == 'h':
            array1[8].append(word)
            numberOfPrimitiveOperations += 12   # 1 function call, 1 addition, 9 comparisons, 1 assignment
        elif word[position] == 'i':
            array1[9].append(word)
            numberOfPrimitiveOperations += 13   # 1 function call, 1 addition, 10 comparisons, 1 assignment
        elif word[position] == 'j':
            array1[10].append(word)
            numberOfPrimitiveOperations += 14   # 1 function call, 1 addition, 11 comparisons, 1 assignment
        elif word[position] == 'k':
            array1[11].append(word)
            numberOfPrimitiveOperations += 15   # 1 function call, 1 addition, 12 comparisons, 1 assignment
        elif word[position] == 'l':
            array1[12].append(word)
            numberOfPrimitiveOperations += 16   # 1 function call, 1 addition, 13 comparisons, 1 assignment
        elif word[position] == 'm':
            array1[13].append(word)
            numberOfPrimitiveOperations += 17   # 1 function call, 1 addition, 14 comparisons, 1 assignment
        elif word[position] == 'n':
            array1[14].append(word)
            numberOfPrimitiveOperations += 18   # 1 function call, 1 addition, 15 comparisons, 1 assignment
        elif word[position] == 'o':
            array1[15].append(word)
            numberOfPrimitiveOperations += 19   # 1 function call, 1 addition, 16 comparisons, 1 assignment
        elif word[position] == 'p':
            array1[16].append(word)
            numberOfPrimitiveOperations += 20   # 1 function call, 1 addition, 17 comparisons, 1 assignment
        elif word[position] == 'q':
            array1[17].append(word)
            numberOfPrimitiveOperations += 21   # 1 function call, 1 addition, 18 comparisons, 1 assignment
        elif word[position] == 'r':
            array1[18].append(word)
            numberOfPrimitiveOperations += 22   # 1 function call, 1 addition, 19 comparisons, 1 assignment
        elif word[position] == 's':
            array1[19].append(word)
            numberOfPrimitiveOperations += 23   # 1 function call, 1 addition, 20 comparisons, 1 assignment
        elif word[position] == 't':
            array1[20].append(word)
            numberOfPrimitiveOperations += 24   # 1 function call, 1 addition, 21 comparisons, 1 assignment
        elif word[position] == 'u':
            array1[21].append(word)
            numberOfPrimitiveOperations += 25   # 1 function call, 1 addition, 22 comparisons, 1 assignment
        elif word[position] == 'v':
            array1[22].append(word)
            numberOfPrimitiveOperations += 26   # 1 function call, 1 addition, 23 comparisons, 1 assignment
        elif word[position] == 'w':
            array1[23].append(word)
            numberOfPrimitiveOperations += 27   # 1 function call, 1 addition, 24 comparisons, 1 assignment
        elif word[position] == 'x':
            array1[24].append(word)
            numberOfPrimitiveOperations += 28   # 1 function call, 1 addition, 25 comparisons, 1 assignment
        elif word[position] == 'y':
            array1[25].append(word)
            numberOfPrimitiveOperations += 29   # 1 function call, 1 addition, 26 comparisons, 1 assignment
        else:
            array1[26].append(word)
            numberOfPrimitiveOperations += 29   # 1 function call, 1 addition, 26 comparisons, 1 assignment
    # First pass end

    # Reorder the words in a sorted list after the first pass if the words has only 1 character (last position is 0)
    if position == 0:
        numberOfPrimitiveOperations += 1    # 1 comparison operation

        # Reorder start (if length == 1)
        sortedWords = []
        numberOfPrimitiveOperations += 1    # 1 assignment operation

        # The list of words is already sorted in ascending order by reading from the first cell to the last cell in
        # array 1
        for cellNumber in range(27):
            for word in array1[cellNumber]:
                sortedWords.append(word)
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
            numberOfPrimitiveOperations += 4 # 2 assignment operations, 1 addition operation, 1 subtraction operation

            # For the second pass (or 4th pass, 6th pass, 8th pass, ...)
            # For all passes that read from array 1 and write to array 2
            if numberOfPasses % 2 == 0:
                numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

                # Re-initialize array 2 because array 2 should be cleared because this pass should write to array 2
                array2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                          [], [], [], []]
                numberOfPrimitiveOperations += 1    # 1 assignment operation

                # Second pass (or 4th pass, 6th pass, 8th pass, ...) start
                # Reads from the first cell to the last cell in array 1
                for cellNumber in range(27):
                    # Reads every word in each cell in array 1
                    for word in array1[cellNumber]:
                        # Appends the number to corresponding cell in array 2 based on the second last (or 4th last,
                        # 6th last, 8th last, ...) character of the word
                        # If the word is shorter than the currently scanned position (length < position + 1), then
                        # append the word to cell 0 (shorter strings are sorted before all longer strings)
                        if len(word) < position + 1:
                            array2[0].append(word)
                            numberOfPrimitiveOperations += 4    # 1 function call,1 addition,1 comparison,1 assignment
                        elif word[position] == 'a':
                            array2[1].append(word)
                            numberOfPrimitiveOperations += 5    # 1 function call,1 addition,2 comparisons,1 assignment
                        elif word[position] == 'b':
                            array2[2].append(word)
                            numberOfPrimitiveOperations += 6    # 1 function call,1 addition,3 comparisons,1 assignment
                        elif word[position] == 'c':
                            array2[3].append(word)
                            numberOfPrimitiveOperations += 7    # 1 function call,1 addition,4 comparisons,1 assignment
                        elif word[position] == 'd':
                            array2[4].append(word)
                            numberOfPrimitiveOperations += 8    # 1 function call,1 addition,5 comparisons,1 assignment
                        elif word[position] == 'e':
                            array2[5].append(word)
                            numberOfPrimitiveOperations += 9    # 1 function call,1 addition,6 comparisons,1 assignment
                        elif word[position] == 'f':
                            array2[6].append(word)
                            numberOfPrimitiveOperations += 10   # 1 function call,1 addition,7 comparisons,1 assignment
                        elif word[position] == 'g':
                            array2[7].append(word)
                            numberOfPrimitiveOperations += 11   # 1 function call,1 addition,8 comparisons,1 assignment
                        elif word[position] == 'h':
                            array2[8].append(word)
                            numberOfPrimitiveOperations += 12   # 1 function call,1 addition,9 comparisons,1 assignment
                        elif word[position] == 'i':
                            array2[9].append(word)
                            numberOfPrimitiveOperations += 13   # 1 function call,1 addition,10 comparisons,1 assignment
                        elif word[position] == 'j':
                            array2[10].append(word)
                            numberOfPrimitiveOperations += 14   # 1 function call,1 addition,11 comparisons,1 assignment
                        elif word[position] == 'k':
                            array2[11].append(word)
                            numberOfPrimitiveOperations += 15   # 1 function call,1 addition,12 comparisons,1 assignment
                        elif word[position] == 'l':
                            array2[12].append(word)
                            numberOfPrimitiveOperations += 16   # 1 function call,1 addition,13 comparisons,1 assignment
                        elif word[position] == 'm':
                            array2[13].append(word)
                            numberOfPrimitiveOperations += 17   # 1 function call,1 addition,14 comparisons,1 assignment
                        elif word[position] == 'n':
                            array2[14].append(word)
                            numberOfPrimitiveOperations += 18   # 1 function call,1 addition,15 comparisons,1 assignment
                        elif word[position] == 'o':
                            array2[15].append(word)
                            numberOfPrimitiveOperations += 19   # 1 function call,1 addition,16 comparisons,1 assignment
                        elif word[position] == 'p':
                            array2[16].append(word)
                            numberOfPrimitiveOperations += 20   # 1 function call,1 addition,17 comparisons,1 assignment
                        elif word[position] == 'q':
                            array2[17].append(word)
                            numberOfPrimitiveOperations += 21   # 1 function call,1 addition,18 comparisons,1 assignment
                        elif word[position] == 'r':
                            array2[18].append(word)
                            numberOfPrimitiveOperations += 22   # 1 function call,1 addition,19 comparisons,1 assignment
                        elif word[position] == 's':
                            array2[19].append(word)
                            numberOfPrimitiveOperations += 23   # 1 function call,1 addition,20 comparisons,1 assignment
                        elif word[position] == 't':
                            array2[20].append(word)
                            numberOfPrimitiveOperations += 24   # 1 function call,1 addition,21 comparisons,1 assignment
                        elif word[position] == 'u':
                            array2[21].append(word)
                            numberOfPrimitiveOperations += 25   # 1 function call,1 addition,22 comparisons,1 assignment
                        elif word[position] == 'v':
                            array2[22].append(word)
                            numberOfPrimitiveOperations += 26   # 1 function call,1 addition,23 comparisons,1 assignment
                        elif word[position] == 'w':
                            array2[23].append(word)
                            numberOfPrimitiveOperations += 27   # 1 function call,1 addition,24 comparisons,1 assignment
                        elif word[position] == 'x':
                            array2[24].append(word)
                            numberOfPrimitiveOperations += 28   # 1 function call,1 addition,25 comparisons,1 assignment
                        elif word[position] == 'y':
                            array2[25].append(word)
                            numberOfPrimitiveOperations += 29   # 1 function call,1 addition,26 comparisons,1 assignment
                        else:
                            array2[26].append(word)
                            numberOfPrimitiveOperations += 29   # 1 function call,1 addition,26 comparisons,1 assignment
                # Second pass (or 4th pass, 6th pass, 8th pass, ...) end

            # For the third pass (or 5th pass, 7th pass, 9th pass, ...)
            # For all passes that read from array 2 and write to array 1
            else:
                numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

                # Re-initialize array 1 because array 1 should be cleared because this pass should write to array 1
                array1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                          [], [], [], []]
                numberOfPrimitiveOperations += 1    # 1 assignment operation

                # Third pass (or 5th pass, 7th pass, 9th pass, ...) start
                # Reads from the first cell to the last cell in array 2
                for cellNumber in range(27):
                    # Reads every word in each cell in array 2
                    for word in array2[cellNumber]:
                        # Appends the word to the corresponding cell in array 1 based on the third last (or 5th last,
                        # 7th last, 9th last, ...) character of the word
                        # If the word is shorter than the currently scanned position (length < position + 1), then
                        # append the word to cell 0 (shorter strings are sorted before all longer strings)
                        if len(word) < position + 1:
                            array1[0].append(word)
                            numberOfPrimitiveOperations += 4    # 1 function call,1 addition, 1 comparison,1 assignment
                        elif word[position] == 'a':
                            array1[1].append(word)
                            numberOfPrimitiveOperations += 5    # 1 function call,1 addition,2 comparisons,1 assignment
                        elif word[position] == 'b':
                            array1[2].append(word)
                            numberOfPrimitiveOperations += 6    # 1 function call,1 addition,3 comparisons,1 assignment
                        elif word[position] == 'c':
                            array1[3].append(word)
                            numberOfPrimitiveOperations += 7    # 1 function call,1 addition,4 comparisons,1 assignment
                        elif word[position] == 'd':
                            array1[4].append(word)
                            numberOfPrimitiveOperations += 8    # 1 function call,1 addition,5 comparisons,1 assignment
                        elif word[position] == 'e':
                            array1[5].append(word)
                            numberOfPrimitiveOperations += 9    # 1 function call,1 addition,6 comparisons,1 assignment
                        elif word[position] == 'f':
                            array1[6].append(word)
                            numberOfPrimitiveOperations += 10   # 1 function call,1 addition,7 comparisons,1 assignment
                        elif word[position] == 'g':
                            array1[7].append(word)
                            numberOfPrimitiveOperations += 11   # 1 addition,8 comparisons,1 assignment
                        elif word[position] == 'h':
                            array1[8].append(word)
                            numberOfPrimitiveOperations += 12   # 1 function call,1 addition,9 comparisons,1 assignment
                        elif word[position] == 'i':
                            array1[9].append(word)
                            numberOfPrimitiveOperations += 13   # 1 function call,1 addition,10 comparisons,1 assignment
                        elif word[position] == 'j':
                            array1[10].append(word)
                            numberOfPrimitiveOperations += 14   # 1 function call,1 addition,11 comparisons,1 assignment
                        elif word[position] == 'k':
                            array1[11].append(word)
                            numberOfPrimitiveOperations += 15   # 1 function call,1 addition,12 comparisons,1 assignment
                        elif word[position] == 'l':
                            array1[12].append(word)
                            numberOfPrimitiveOperations += 16   # 1 function call,1 addition,13 comparisons,1 assignment
                        elif word[position] == 'm':
                            array1[13].append(word)
                            numberOfPrimitiveOperations += 17   # 1 function call,1 addition,14 comparisons,1 assignment
                        elif word[position] == 'n':
                            array1[14].append(word)
                            numberOfPrimitiveOperations += 18   # 1 function call,1 addition,15 comparisons,1 assignment
                        elif word[position] == 'o':
                            array1[15].append(word)
                            numberOfPrimitiveOperations += 19   # 1 function call,1 addition,16 comparisons,1 assignment
                        elif word[position] == 'p':
                            array1[16].append(word)
                            numberOfPrimitiveOperations += 20   # 1 function call,1 addition,17 comparisons,1 assignment
                        elif word[position] == 'q':
                            array1[17].append(word)
                            numberOfPrimitiveOperations += 21   # 1 function call,1 addition,18 comparisons,1 assignment
                        elif word[position] == 'r':
                            array1[18].append(word)
                            numberOfPrimitiveOperations += 22   # 1 function call,1 addition,19 comparisons,1 assignment
                        elif word[position] == 's':
                            array1[19].append(word)
                            numberOfPrimitiveOperations += 23   # 1 function call,1 addition,20 comparisons,1 assignment
                        elif word[position] == 't':
                            array1[20].append(word)
                            numberOfPrimitiveOperations += 24   # 1 function call,1 addition,21 comparisons,1 assignment
                        elif word[position] == 'u':
                            array1[21].append(word)
                            numberOfPrimitiveOperations += 25   # 1 function call,1 addition,22 comparisons,1 assignment
                        elif word[position] == 'v':
                            array1[22].append(word)
                            numberOfPrimitiveOperations += 26   # 1 function call,1 addition,23 comparisons,1 assignment
                        elif word[position] == 'w':
                            array1[23].append(word)
                            numberOfPrimitiveOperations += 27   # 1 function call,1 addition,24 comparisons,1 assignment
                        elif word[position] == 'x':
                            array1[24].append(word)
                            numberOfPrimitiveOperations += 28   # 1 function call,1 addition,25 comparisons,1 assignment
                        elif word[position] == 'y':
                            array1[25].append(word)
                            numberOfPrimitiveOperations += 29   # 1 function call,1 addition,26 comparisons,1 assignment
                        else:
                            array1[26].append(word)
                            numberOfPrimitiveOperations += 29   # 1 function call,1 addition,26 comparisons,1 assignment
                # Third pass (or 5th pass, 7th pass, 9th pass, ...) end

        # Iteration end

        # Reorder start
        sortedWords = []
        numberOfPrimitiveOperations += 1    # 1 assignment operation

        # After the second pass (or 4th pass, 6th pass, 8th pass, ...)
        # After all passes that write to array 2
        if numberOfPasses % 2 == 0:
            numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

            # The list of words is already sorted in ascending order by reading from the first cell to the last cell
            # in array 2
            for cellNumber in range(27):
                for word in array2[cellNumber]:
                    sortedWords.append(word)
                    numberOfPrimitiveOperations += 1    # 1 assignment operation

        # After the third pass (or 5th pass, 7th pass, 9th pass, ...)
        # After all passes that write to array 1 (except the first pass)
        else:
            numberOfPrimitiveOperations += 2    # 1 modulus operation and 1 comparison operation

            # The list of words is already sorted in ascending order by reading from the first cell to the last cell
            # in array 1
            for cellNumber in range(27):
                for word in array1[cellNumber]:
                    sortedWords.append(word)
                    numberOfPrimitiveOperations += 1    # 1 assignment operation
        # Reorder end

    # Word sorting algorithm end

    return numberOfPrimitiveOperations

# Function to randomly generate a list of words shorter than or equal than a maximum length
# Takes 2 inputs, N and MAXIMUM_LENGTH
# N is the number of words in the list, MAXIMUM_LENGTH is the maximum length (number of characters) in each word
# Returns a list of words (an array of string with only lower case letter)
def generate_random_list_of_words(N, MAXIMUM_LENGTH):
    # Initialize an empty list of words
    words = []

    # An array of the permitted letters to choose from (used when string generation)
    # The permitted letters are all lower case letters only
    permittedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Generate N words
    for _ in range(N):
        # Randomly decide the length (number of characters) of the word
        length = random.randint(1, MAXIMUM_LENGTH)

        # Initialize a variable to store the word
        word = ''

        # Generate a number with length number of characters
        for _ in range(length):
            # Generate a random number from 0 to 25 (decide which alphabet from permittedLetters is chosen)
            indexOfChosenLetter = random.randint(0, 25)

            # The character of the current position
            character = permittedLetters[indexOfChosenLetter]

            # Append the character to word
            word = word + character

        # Append the word to the main list
        words.append(word)

    return words

# Experiment start
# Maximum number of characters (maximum length) = 10 (Fixed variable)
MAXIMUM_LENGTH = 10

# Generate a random list of 100 words with maximum 10 characters
words_N100 = generate_random_list_of_words(100, MAXIMUM_LENGTH)

# Generate a random list of 200 words with maximum 10 characters
words_N200 = generate_random_list_of_words(200, MAXIMUM_LENGTH)

# Generate a random list of 300 words with maximum 10 characters
words_N300 = generate_random_list_of_words(300, MAXIMUM_LENGTH)

# Generate a random list of 400 words with maximum 10 characters
words_N400 = generate_random_list_of_words(400, MAXIMUM_LENGTH)

# Generate a random list of 500 words with maximum 10 characters
words_N500 = generate_random_list_of_words(500, MAXIMUM_LENGTH)

# Generate a random list of 600 words with maximum 10 characters
words_N600 = generate_random_list_of_words(600, MAXIMUM_LENGTH)

# Generate a random list of 700 words with maximum 10 characters
words_N700 = generate_random_list_of_words(700, MAXIMUM_LENGTH)

# Generate a random list of 800 words with maximum 10 characters
words_N800 = generate_random_list_of_words(800, MAXIMUM_LENGTH)

# Generate a random list of 900 words with maximum 10 characters
words_N900 = generate_random_list_of_words(900, MAXIMUM_LENGTH)

# Generate a random list of 1000 words with maximum 10 characters
words_N1000 = generate_random_list_of_words(1000, MAXIMUM_LENGTH)

# Array of N (Manipulated variable)
array_N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Initialize array of number of primitive operations (Observed variable)
array_numberOfPrimitiveOperations = []

# Count the number of primitive operations for sorting 100 words
numberOfPrimitiveOperations_N100 = count_primitive_operation_in_word_sorting(words_N100, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N100)

# Count the number of primitive operations for sorting 200 words
numberOfPrimitiveOperations_N200 = count_primitive_operation_in_word_sorting(words_N200, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N200)

# Count the number of primitive operations for sorting 300 words
numberOfPrimitiveOperations_N300 = count_primitive_operation_in_word_sorting(words_N300, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N300)

# Count the number of primitive operations for sorting 400 words
numberOfPrimitiveOperations_N400 = count_primitive_operation_in_word_sorting(words_N400, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N400)

# Count the number of primitive operations for sorting 500 words
numberOfPrimitiveOperations_N500 = count_primitive_operation_in_word_sorting(words_N500, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N500)

# Count the number of primitive operations for sorting 600 words
numberOfPrimitiveOperations_N600 = count_primitive_operation_in_word_sorting(words_N600, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N600)

# Count the number of primitive operations for sorting 700 words
numberOfPrimitiveOperations_N700 = count_primitive_operation_in_word_sorting(words_N700, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N700)

# Count the number of primitive operations for sorting 800 words
numberOfPrimitiveOperations_N800 = count_primitive_operation_in_word_sorting(words_N800, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N800)

# Count the number of primitive operations for sorting 900 words
numberOfPrimitiveOperations_N900 = count_primitive_operation_in_word_sorting(words_N900, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N900)

# Count the number of primitive operations for sorting 1000 words
numberOfPrimitiveOperations_N1000 = count_primitive_operation_in_word_sorting(words_N1000, MAXIMUM_LENGTH)
array_numberOfPrimitiveOperations.append(numberOfPrimitiveOperations_N1000)
# Experiment end

# Print the fixed variable, the manipulated variable and the observed variable
print(f'Fixed variable: Maximum number of characters (MAXIMUM_LENGTH): {MAXIMUM_LENGTH}')
print(f'Manipulated variable: Number of words (N): {array_N}')
print(f'Observed variable: Number of primitive operations: {array_numberOfPrimitiveOperations}')

# Plot the graph of number of primitive operations vs number of words (N)
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
plt.title('Graph of Number of Primitive Operations vs N for Word Sorting Algorithm')

plt.show()
