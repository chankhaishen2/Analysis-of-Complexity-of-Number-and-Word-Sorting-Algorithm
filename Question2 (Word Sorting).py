# Word sorting algorithm

print('Word sorting')

# Asks the maximum length of all words (which will be used to check against the words inputted by the user)
# Note: All words in the list should be shorter than or equal to the maximum length and longer than or equal to 1
while True:
    try:
        # Checks whether the length inputted is an integer
        MAXIMUM_LENGTH = int(input('Enter the maximum length of all words: '))

        # Checks whether the length inputted is smaller than 1
        if MAXIMUM_LENGTH < 1:
            print('The maximum length must be at least 1.')
            continue

        break

    except:
        print('The maximum length must be an integer.')
        continue

# Initialize an array to hold the words inputted by the user
words = []

# Asks the user to input the list of words to be sorted
# Note: All words must consist of lower case characters only and of the length shorter than or equal to the
# maximum length as specified in the above input and longer than or equal to 1
while True:
    userInput = input('Enter "0" if the list is finish or enter the next word in the list: ')

    # Ends the while loop if the list of words is finish
    if userInput.strip() == '0':
        break

    # Checks whether the length of the input is shorter than or equal to the maximum length
    if len(userInput) > MAXIMUM_LENGTH:
        print(f'The length of the input must be shorter than or equal to to the maximum length ({MAXIMUM_LENGTH}).')
        continue

    # Checks whether the length of the input is longer than or equal to 1
    if len(userInput) < 1:
        print('The length of the input must be longer than or equal to 1.')
        continue

    # Checks whether the input only consists of lower case characters
    onlyContainLowerCharacter = True

    for position in range(len(userInput)):
        if userInput[position] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            print('The input must only contain lower case characters.')
            onlyContainLowerCharacter = False
            break

    if not onlyContainLowerCharacter:
        continue

    words.append(userInput)
    print('The word is accepted.')

# Prints out the initial list of words (unsorted)
print('The list of words accepted: ')
for word in words:
    print(word)

# Word sorting algorithm start

# Initialize start
# Initialize 2 arrays with 27 elements (which is also an array)
array1 = [[], [], [], [], [], [], [], [], [] ,[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
array2 = [[], [], [], [], [], [], [], [], [], [], [] ,[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
# Initialize end

# Iteration start

# For the first pass, need to look at the last character (position of length - 1)
position = MAXIMUM_LENGTH - 1

# First pass start
# Pass through all words in the list of words inputted
for word in words:
    # Append the word to the corresponding cell in array 1 based on the last character of the word
    # If the word is shorter than the currently scanned position (length < position + 1), then append the word to
    # cell 0 (shorter strings are sorted before all longer strings)
    if len(word) < position + 1:
        array1[0].append(word)
    elif word[position] == 'a':
        array1[1].append(word)
    elif word[position] == 'b':
        array1[2].append(word)
    elif word[position] == 'c':
        array1[3].append(word)
    elif word[position] == 'd':
        array1[4].append(word)
    elif word[position] == 'e':
        array1[5].append(word)
    elif word[position] == 'f':
        array1[6].append(word)
    elif word[position] == 'g':
        array1[7].append(word)
    elif word[position] == 'h':
        array1[8].append(word)
    elif word[position] == 'i':
        array1[9].append(word)
    elif word[position] == 'j':
        array1[10].append(word)
    elif word[position] == 'k':
        array1[11].append(word)
    elif word[position] == 'l':
        array1[12].append(word)
    elif word[position] == 'm':
        array1[13].append(word)
    elif word[position] == 'n':
        array1[14].append(word)
    elif word[position] == 'o':
        array1[15].append(word)
    elif word[position] == 'p':
        array1[16].append(word)
    elif word[position] == 'q':
        array1[17].append(word)
    elif word[position] == 'r':
        array1[18].append(word)
    elif word[position] == 's':
        array1[19].append(word)
    elif word[position] == 't':
        array1[20].append(word)
    elif word[position] == 'u':
        array1[21].append(word)
    elif word[position] == 'v':
        array1[22].append(word)
    elif word[position] == 'w':
        array1[23].append(word)
    elif word[position] == 'x':
        array1[24].append(word)
    elif word[position] == 'y':
        array1[25].append(word)
    else:
        array1[26].append(word)
# First pass end

# Reorder the words in a sorted list after the first pass if the words has only 1 character (last position is 0)
if position == 0:

    # Reorder start (if length == 1)
    sortedWords = []

    # The list of words is already sorted in ascending order by reading from the first cell to the last cell in
    # array 1
    for cellNumber in range(27):
        for word in array1[cellNumber]:
            sortedWords.append(word)
    # Reorder end (if length == 1)

    # Prints out the sorted list and then end
    print('The sorted list of words: ')
    for word in sortedWords:
        print(word)

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
            array2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ,[], [], [],
                      [], [], []]

            # Second pass (or 4th pass, 6th pass, 8th pass, ...) start
            # Reads from the first cell to the last cell in array 1
            for cellNumber in range(27):
                # Reads every word in each cell in array 1
                for word in array1[cellNumber]:
                    # Appends the number to corresponding cell in array 2 based on the second last (or 4th last,
                    # 6th last, 8th last, ...) character of the word
                    # If the word is shorter than the currently scanned position (length < position + 1), then append
                    # the word to cell 0 (shorter strings are sorted before all longer strings)
                    if len(word) < position + 1:
                        array2[0].append(word)
                    elif word[position] == 'a':
                        array2[1].append(word)
                    elif word[position] == 'b':
                        array2[2].append(word)
                    elif word[position] == 'c':
                        array2[3].append(word)
                    elif word[position] == 'd':
                        array2[4].append(word)
                    elif word[position] == 'e':
                        array2[5].append(word)
                    elif word[position] == 'f':
                        array2[6].append(word)
                    elif word[position] == 'g':
                        array2[7].append(word)
                    elif word[position] == 'h':
                        array2[8].append(word)
                    elif word[position] == 'i':
                        array2[9].append(word)
                    elif word[position] == 'j':
                        array2[10].append(word)
                    elif word[position] == 'k':
                        array2[11].append(word)
                    elif word[position] == 'l':
                        array2[12].append(word)
                    elif word[position] == 'm':
                        array2[13].append(word)
                    elif word[position] == 'n':
                        array2[14].append(word)
                    elif word[position] == 'o':
                        array2[15].append(word)
                    elif word[position] == 'p':
                        array2[16].append(word)
                    elif word[position] == 'q':
                        array2[17].append(word)
                    elif word[position] == 'r':
                        array2[18].append(word)
                    elif word[position] == 's':
                        array2[19].append(word)
                    elif word[position] == 't':
                        array2[20].append(word)
                    elif word[position] == 'u':
                        array2[21].append(word)
                    elif word[position] == 'v':
                        array2[22].append(word)
                    elif word[position] == 'w':
                        array2[23].append(word)
                    elif word[position] == 'x':
                        array2[24].append(word)
                    elif word[position] == 'y':
                        array2[25].append(word)
                    else:
                        array2[26].append(word)
            # Second pass (or 4th pass, 6th pass, 8th pass, ...) end

        # For the third pass (or 5th pass, 7th pass, 9th pass, ...)
        # For all passes that read from array 2 and write to array 1
        else:
            # Re-initialize array 1 because array 1 should be cleared because this pass should write to array 1
            array1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                      [], [], []]

            # Third pass (or 5th pass, 7th pass, 9th pass, ...) start
            # Reads from the first cell to the last cell in array 2
            for cellNumber in range(27):
                # Reads every word in each cell in array 2
                for word in array2[cellNumber]:
                    # Appends the word to the corresponding cell in array 1 based on the third last (or 5th last,
                    # 7th last, 9th last, ...) character of the word
                    # If the word is shorter than the currently scanned position (length < position + 1), then append
                    # the word to cell 0 (shorter strings are sorted before all longer strings)
                    if len(word) < position + 1:
                        array1[0].append(word)
                    elif word[position] == 'a':
                        array1[1].append(word)
                    elif word[position] == 'b':
                        array1[2].append(word)
                    elif word[position] == 'c':
                        array1[3].append(word)
                    elif word[position] == 'd':
                        array1[4].append(word)
                    elif word[position] == 'e':
                        array1[5].append(word)
                    elif word[position] == 'f':
                        array1[6].append(word)
                    elif word[position] == 'g':
                        array1[7].append(word)
                    elif word[position] == 'h':
                        array1[8].append(word)
                    elif word[position] == 'i':
                        array1[9].append(word)
                    elif word[position] == 'j':
                        array1[10].append(word)
                    elif word[position] == 'k':
                        array1[11].append(word)
                    elif word[position] == 'l':
                        array1[12].append(word)
                    elif word[position] == 'm':
                        array1[13].append(word)
                    elif word[position] == 'n':
                        array1[14].append(word)
                    elif word[position] == 'o':
                        array1[15].append(word)
                    elif word[position] == 'p':
                        array1[16].append(word)
                    elif word[position] == 'q':
                        array1[17].append(word)
                    elif word[position] == 'r':
                        array1[18].append(word)
                    elif word[position] == 's':
                        array1[19].append(word)
                    elif word[position] == 't':
                        array1[20].append(word)
                    elif word[position] == 'u':
                        array1[21].append(word)
                    elif word[position] == 'v':
                        array1[22].append(word)
                    elif word[position] == 'w':
                        array1[23].append(word)
                    elif word[position] == 'x':
                        array1[24].append(word)
                    elif word[position] == 'y':
                        array1[25].append(word)
                    else:
                        array1[26].append(word)
            # Third pass (or 5th pass, 7th pass, 9th pass, ...) end

    # Iteration end

    # Reorder start
    sortedWords = []

    # After the second pass (or 4th pass, 6th pass, 8th pass, ...)
    # After all passes that write to array 2
    if numberOfPasses % 2 == 0:
        # The list of words is already sorted in ascending order by reading from the first cell to the last cell
        # in array 2
        for cellNumber in range(27):
            for word in array2[cellNumber]:
                sortedWords.append(word)

    # After the third pass (or 5th pass, 7th pass, 9th pass, ...)
    # After all passes that write to array 1 (except the first pass)
    else:
        # The list of words is already sorted in ascending order by reading from the first cell to the last cell
        # in array 1
        for cellNumber in range(27):
            for word in array1[cellNumber]:
                sortedWords.append(word)
    # Reorder end

    # Prints out the sorted list and then end
    print('The sorted list of numbers: ')
    for word in sortedWords:
        print(word)

# Word sorting algorithm end
