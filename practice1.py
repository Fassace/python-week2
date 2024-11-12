# Program 1: Create a list of integers from user input and compute the sum
def sum_of_integers():
    user_input = input("Enter a list of integers separated by spaces: ")
    int_list = list(map(int, user_input.split()))
    total_sum = sum(int_list)
    return int_list, total_sum

# Execute each program and display results
# Program 1
int_list, total_sum = sum_of_integers()
print("List of integers:", int_list)
print("Sum of integers:", total_sum)