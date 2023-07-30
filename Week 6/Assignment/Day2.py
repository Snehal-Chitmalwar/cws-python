# Q1.Write a function called sum_natural_numbers(n) that takes an integer
# n as a parameter n returns sum of natural numbers from 1 to n.
def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print(sum_natural_numbers(4))

# Q2. Write a function called find_largest(lst) that takes list
#  of integers lst as parameter n returns largest int in list.


def find_largest(lst):
    largest = max(lst)
    return largest


print(find_largest([2, 34, 12, 45, 78]))

# Q3. Write a function called find_smallest(lst) that takes list
# of integers lst as parameter n returns smallest int in list.


def find_smallest(lst):
    smallest = min(lst)
    return smallest


print(find_smallest([2, 34, 12, 45, 78]))

# Q4. Write a function called count_vowels(s) that  takes string s
#  as parameter n returns total number of vowels(a,e,i,o,u) in the string


def count_vowels(s):
    count, s = 0, s.lower()
    for i in s:
        if i in ["a", "e", "i", "o", "u"]:
            count += 1
    return count


print(count_vowels("Snehal"))

# Q5. Write a function called is_prime(n) that takes an  integer n
# as a parameter and returns TRue if number is prime, otherwise false.


def is_prime(n):
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


if is_prime(10):
    print("Prime")
else:
    print("Not Prime")

# Q6.Write a function called find_common_elements(lst1,lst2) taht takes 2
#  lists lst1 n lst2 as parameter n returns a list containing common
#  elements b/w 2 lists.


def find_common_elements(lst1, lst2):
    common_list = []
    for i in lst2:
        if i in lst1:
            common_list.append(i)
    return common_list


print(find_common_elements([23, 23, 4, 56], [4, 56, 45]))

# Q7. Write a function called merge_dictionaries(dict1,dict2) taht takes
# 2 dictionaries dict1 n dict2 as parameter n returns a dictionary containing
# key-value pairs from both i/p dictionaries.If a key is present in both dictioaries,
# value from dict2 should overwrite value from dict1.


def merge_dictionaries(dict1, dict2):
    new_dict = dict1.copy()
    for k, v in dict2.items():
        new_dict[k] = v
    print(new_dict)


merge_dictionaries({"Rose": 23, "Jack": 67, "Michaela": 78}, {
                   "Rose": 90, "Jin": 89, "Jennifer": 60})
