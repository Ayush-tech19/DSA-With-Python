# Function to rotate list by one position to the right
def rotate_by_one(lst):
    # Check if list is empty
    if len(lst) == 0:
        return lst
    
    # Store the last element
    last_element = lst[-1]
    
    # Shift all elements one position to the right
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    
    # Put the last element at the first position
    lst[0] = last_element
    
    return lst


# Example usage
my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_by_one(my_list)

print("Rotated List:", rotated_list)