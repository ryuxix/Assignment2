"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    # Base case 
    if len(numbers) == 0:
        return 0
    # Recursion case
    return numbers [0] + sum_list(numbers[1:])


# Uncomment to test sum_list
print("\nTest sum_list:")
print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")


def count_even(numbers):
   # Base case
   if len(numbers) == 0:
       return 0
   # Recursion case
   if numbers[0] % 2 == 0:
       return 1 + count_even(numbers[1:])
   else:
       return count_even(numbers[1:])

# Uncomment to test count_even
print("\nTest count_even:")
print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

def find_strings_with(strings, target):
   # Base case
   if len(strings) == 0:
       return []
   # Recurison case
   rest_result = find_strings_with(strings[1:], target)

   if target in strings[0]:
       return [strings[0]] + rest_result
   else:
       return rest_result

# Uncomment to test find_strings_with
print("\nTest find_strings_with:")
result = find_strings_with(["hello", "world", "help", "test"], "hel")
print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
print(f"  (expected: ['hello', 'help'])")
    
result = find_strings_with(["cat", "dog", "bird"], "z")
print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
print(f"  (expected: [])")

# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    # Learned from resource 2
    # Base case if the path is a file and is counted as 1
    if os.path.isfile(directory_path): 
        return 1
    # Recursion case if path is directory
    total = 0
    # This loops through all the items inside the directory
    for item in os.listdir(directory_path): # os.listdir(path) is where it returns a list of everything in a directory
        full_path = os.path.join(directory_path, item) # os.path.join() is where it combines path components correctly for any system
        total += count_files(full_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    # Base case
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path] # return list containing the file
        else:
            return [] # not infected
        
    infected = []
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        infected += find_infected_files(full_path, extension)

    return infected

# Department infection comparison
hr_count = (
    len(find_infected_files("breach_data/HR"))+
    len(find_infected_files("breach_data/HR_1")) +
    len(find_infected_files("breach_data/HR_2"))
)
sales_count = len(find_infected_files("breach_data/Sales"))
operations_count = len(find_infected_files("breach_data/Operations"))

# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    ## 1. Uncomment to run tests for count_files functions
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    ## 2. Uncomment to run count_files for breached files
    print("Total files (breeched files):", count_files("breach_data")) # ???

    ## 3. Uncomment to run tests for find_infected_files function
    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case2_nested"))) # 0
    print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    ## 4. Uncomment to run find_infected breached files
    print("Total Infected Files (breached files):", len(find_infected_files("breach_data"))) # ???

    ## 5. Determine how many files were corrupted by department (Finance, HR, and Sales)
    # Printing the infected files of HR, Sales, and Operations
    print("HR infected files:", hr_count)
    print("Sales infected files:", sales_count)
    print("Operations infected files:", operations_count)

    
    print("\n⚠ Uncomment the test functions in the main block to run tests!")