def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,0,3,0,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zeros is: {average_zero}")

my_list_with_strings = [1,2,'a',4,5]
average_strings = calculate_average(my_list_with_strings) 
print(f"The average of a list with strings is: {average_strings}") 