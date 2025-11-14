"""
Python module containing a function to sort a list of dictionaries by a specific key.
This implementation uses the highly efficient operator.itemgetter method.
"""
from operator import itemgetter
from typing import List, Dict, Any

def sort_list_of_dicts(data: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries based on the value of a specified key.

    :param data: The list of dictionaries to be sorted.
    :param key: The dictionary key to use for sorting.
    :return: A new, sorted list of dictionaries.
    """
    # itemgetter is implemented in C and is generally the fastest way to sort
    # by a dictionary key in Python.
    return sorted(data, key=itemgetter(key))

# --- Example Usage ---
if __name__ == "__main__":
    # Sample data
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 60000},
        {'name': 'Bob', 'age': 25, 'salary': 75000},
        {'name': 'Charlie', 'age': 35, 'salary': 60000},
        {'name': 'David', 'age': 25, 'salary': 50000},
    ]

    print("--- Original List ---")
    for emp in employees:
        print(emp)

    print("\n--- Sorted by 'age' (Ascending) ---")
    sorted_by_age = sort_list_of_dicts(employees, 'age')
    for emp in sorted_by_age:
        print(emp)

    print("\n--- Sorted by 'salary' (Ascending) ---")
    sorted_by_salary = sort_list_of_dicts(employees, 'salary')
    for emp in sorted_by_salary:
        print(emp)