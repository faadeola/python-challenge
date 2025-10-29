import random

try:
    num_of_num = int(input("How many numbers needs to be check? \n"))
    user_guess = int(input("Guess a number that could be in the list\n"))
except ValueError:
    print("You entered a wrong value. Restart Programme!")
    exit()

# -- Generate random numbers in range up to 49
number_list = random.sample(range(50), num_of_num)

is_even = [val for val in number_list if val % 2 == 0]
is_odd = [val for val in number_list if val % 2 != 0]


def avgNumber(list_name):
    """ Returns the average of all the number in a given list"""

    sum_of_num = 0

    # Loop through list and sum up values
    for val in list_name:
        sum_of_num += val

    # Find the average of the list
    avg_of_list = sum_of_num/len(list_name)

    # Return the average value calculated
    return avg_of_list


def guess_response():
    """ A function to generate the outcome of the user inputed response"""

    response = ""
    response_index = [i for i in range(
        len(number_list)) if user_guess == number_list[i]]
    if user_guess in number_list:
        response = f"Number found in the list at index {', '.join(map(str, response_index))}" if response_index else ''

    else:
        response = "Number not found in the list"

    return response


# print all element in the even list with comma as seperator
print("Even numbers found in the list is/are")
print(*is_even, sep=", ")

# print all element in the odd list with comma as seperator
print("Odd numbers found in the list is/are")
print(*is_odd, sep=", ")

# print minimum and maximum number in the list
print(f"Minimum number: {min(number_list)}")
print(f"Maximum number: {max(number_list)}")


print(number_list)
avgResult = avgNumber(number_list)  # returns average of the whole numbers

# print outcome of user's guess
print(guess_response())

print(number_list_sorted)
