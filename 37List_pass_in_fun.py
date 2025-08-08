# pass list in function 
def process_list(my_list):
    """
    Function to process a list and print its elements.
    :param my_list: List of elements to process
    """
    # count of the event and odd numbers 
    even_count = 0
    odd_count = 0
    for i in my_list:
        if i%2 == 0:
            print(f"{i} is even")
            even_count += 1      
        else:
            print(f"{i} is odd")
            odd_count += 1
    return even_count, odd_count
# Example usage
my_list = [1, 2, 3, 4, 5]
process_list(my_list)
even_count, odd_count = process_list(my_list)
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")