"""
This programme counts how many times each text appears in a sentence provided
"""

# Declare variables
userInput = input("Enter your long text here\n")

# This function gets unique text from words


def createUnique(value):
    wordContainer = []
    value = value.lower()
    wordSplit = value.split(" ")
    for word in wordSplit:
        if word not in wordContainer:
            wordContainer.append(word)
    return wordContainer, wordSplit


# This function now counts number of times a word appeared
def countText(value):
    uniqueWord, wordSplitList = createUnique(value)

    print("--------------------------------")
    print("Word ---> NumberOfAppearance")
    print("--------------------------------")
    print("--------------------------------")

    for word in uniqueWord:
        print(f"{word} ---> {wordSplitList.count(word)}")


# Print out the result of the count
countText(userInput)
