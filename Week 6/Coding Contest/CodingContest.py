# Q1. Write a function called list_average(lst) that takes a list of
#  numbers lst as a parameter and returns the average of the numbers in the list.
def list_average(lst):
    avg = sum(lst)/len(lst)
    return avg


numbers = [10, 20, 30, 40, 50, 60]
average = list_average(numbers)
print(average)

# Q2. Write a function called dictionary_value_sum(d) that takes a
# dictionary d as a parameter, where the values are numbers, and returns
#  the sum of all the values in the dictionary.


def dictionary_value_sum(d):
    value_list = []
    for k, v in d.items():
        value_list.append(v)
    sum_values = sum(value_list)
    print(sum_values)


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
dictionary_value_sum(my_dict)
my_dict = {"apple": 10, "banana": 20, "orange": 30}
dictionary_value_sum(my_dict)
my_dict = {"x": -5, "y": 5, "z": 0}
dictionary_value_sum(my_dict)
my_dict = {}
dictionary_value_sum(my_dict)

# Q3. Write a function called filter_even_numbers(lst) that takes a
# list of integers lst as a parameter and returns a new list containing
# only the even integers from the input list.


def filter_even_numbers(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)


filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
filter_even_numbers([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
filter_even_numbers([11, 13, 17, 19, 23, 29])
filter_even_numbers([])

# Q4. Write a function called union_of_sets(set_a, set_b) that
# takes two sets set_a and set_b as parameters and returns a new
# set containing the union of the two input sets.


def union_of_sets(set_a, set_b):
    new_set = set_a.union(set_b)
    print(new_set)


union_of_sets({1, 2, 3}, {3, 4, 5})
union_of_sets({10, 20, 30}, {40, 50, 60})
union_of_sets({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10})
union_of_sets({2, 4, 6, 8, 10}, {2, 4, 6, 8, 10})

# Q5. Write a function called is_palindrome(s) that takes a string
# s as a parameter and returns True if the string is a palindrome
# (reads the same forward and backward), otherwise False.


def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False


string = is_palindrome("racecar")
print(string)
string = is_palindrome("hello")
print(string)
string = is_palindrome("level")
print(string)
string = is_palindrome("A man a plan a canal Panama")
print(string)
string = is_palindrome("")
print(string)

# Q6. Write a function called get_factors(n) that takes an integer n as
# a parameter and returns a list of its factors, excluding 1 and the number itself.


def get_factors(n):
    factor_list = []
    for i in range(2, n):
        if n % i == 0:
            factor_list.append(i)
    print(factor_list)


get_factors(6)
get_factors(12)
get_factors(20)
get_factors(7)
get_factors(1)
