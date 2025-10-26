""" Problem Description """
# Write a Python program that:
""" 1. Accepts five sentences from the user ( or you can use a predefined list for testing). """
""" 2. Stores them in a list. """
""" 3. Creates a function called analyze_sentence(sentence) that: """
# --- Counts the number of words in the sentence.
# --- Counts the number of unique words(case-insensitive).
# --- Finds the longest word in the sentence.
""" 4. For each sentence, print: """
# --- The sentence itself
# --- Total word count
# --- Unique word count
# --- Longest word
""" 5. After analyzing all sentences: """ 
# --- Print the average number of words per sentence.
# --- Print the sentence with the most words.


# Get number of sentence to analyze
numSentence = int(input("Enter number of sentence\n"))
sentenceContainer = []

# Get each sentence and add them to the list
for i in range(numSentence):
    eachSentence = input(f"Enter sentence {i+1} \n").title()
    sentenceContainer.append(eachSentence)


def analyze_sentence(sentence):
    """ 
        This function analyzes each sentence in a list consisting of multiple sentences and checks for 
            1. The number of word in a sentence
            2. Number of unique word
            3. The longest word in the sentence
    """

    # --Split the sentence into a list holding each word
    clean_sentence = sentence.replace('.', '').replace(',', '')
    sentenceHold = clean_sentence.split(" ")

    def countWord(sentence):
        """ A function to count number of word in a sentence """
        numOfWord = len(sentenceHold)  # --Returns the length of the list
        return numOfWord

    def countUnique(sentence):
        """ A function to get the unique number word """
        uniqueWord = []
        for word in sentenceHold:
            # --Check if word is not in the list of word uniquely created
            if word not in uniqueWord:
                uniqueWord.append(word)  # -- Add word to list if not there
        return len(uniqueWord)

    def longWord(sentence):
        """ A function to find the longest word """
        charCount = []  # -- Hold number count for each character in a word
        longestWordList = []  # -- Hold longest word found in each sentence
        wordCheck = []  # -- Hold unique value

        # -- Get length of each word and add each length to a list
        for word in sentenceHold:
            numChar = len(word)
            charCount.append(numChar)

        # -- Sort the list holding each word length in ascending orders
        charCount = sorted(charCount)

        # -- Get the highest length
        longestWordChar = charCount[-1]

        # -- Get the longest word in the sentence
        for word in sentenceHold:
            if word not in wordCheck:
                wordCheck.append(word)
                if len(word) == longestWordChar:
                    longestWordList.append(word)

        # Print longest word as single word if it is just one but as a list if more than one
        if len(longestWordList) == 1:
            return longestWordList[0]
        else:
            return longestWordList

    # Call functions
    numOfWord = countWord(sentence)
    numUnique = countUnique(sentence)
    longestWord = longWord(sentence)

    # return values for use
    return numOfWord, numUnique, longestWord


def sentenceLength(sentenceContainer):
    """ Function to get number of words in the sentences list """
    totalWord = 0
    for sentence in sentenceContainer:
        splitSentence = sentence.split(" ")
        totalWord += len(splitSentence)
    return totalWord


def getLongWord(sentenceContainer):
    """ A function to get the longest sentence in the whole sentences list """
    wordHold = []
    wordHoldNum = []

    for sentence in sentenceContainer:
        wordHoldNum.append(len(sentence.split()))

    # Sort the list holding length of each sentence
    wordHoldNum = sorted(wordHoldNum)

    # Check which of the sentence holds the longest length
    for sentence in sentenceContainer:
        if sentence not in wordHold:
            if len(sentence) == wordHoldNum[-1]:
                wordHold.append(sentence)

    # Print longest word
    if len(wordHold) == 1:
        print(f"Sentence with the most words: {wordHold[0]}")
    else:
        for i in range(len(wordHold)):
            print(f"Sentence with the most words are:\n {wordHold[i]}")


# Print out analysis for each sentence
for i in range(len(sentenceContainer)):
    numOfWord, numUnique, longestWord = analyze_sentence(sentenceContainer[i])
    print(f"Sentence {i+1}: {sentenceContainer[i]}")
    print(f"Total words: {numOfWord}")
    print(f"Unique word: {numUnique}")
    print(f"Longest word: {longestWord}")
    print("="*80)

# Assign variables to get average of number of words per sentence
totalWord = sentenceLength(sentenceContainer)
averageWord = totalWord/len(sentenceContainer)

# Print average number of words per sentence
print(f"Average number of words per sentence: {averageWord}")

# Print the sentence with the most words
getLongWord(sentenceContainer)
