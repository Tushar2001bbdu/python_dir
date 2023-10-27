def linear_search(ar, target):
    for i in range(len(ar)):
        if ar[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

# Example of how to use the linear_search function
ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 6
result = linear_search(ar, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
