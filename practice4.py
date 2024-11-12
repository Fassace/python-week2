# Program 4: Create two sets of integers from user input and find the intersection
def common_elements_in_sets():
    set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
    set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))
    common_set = set1.intersection(set2)
    return set1, set2, common_set

# Program 4
set1, set2, common_set = common_elements_in_sets()
print("First Set:", set1)
print("Second Set:", set2)
print("Common Elements:", common_set)