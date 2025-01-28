def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"Heollo,{name} you are {age} years old"
name = "Maruti Nandan Thakur"
age = 37
print(format_string(name,age))

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
print("15 is" , conditional_check(15))  
print("5 is", conditional_check(5))   
print("10 is", conditional_check(10))  

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(1, n + 1):  # for loop 
        sum += i
    return sum
print("sum number =",loop_sum(10)) 

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:  # Handle an empty list
        return (0, None, None)
    
    total = sum(numbers)  # finds sum of all numbers 
    maximum = max(numbers)  # finds maximum from the list named numbers
    minimum = min(numbers)   # finds minimum from the list named numbers
    
    return (total, maximum, minimum)

my_numbers = [2, 5, 3, 40, 10, 15] #List creation
result = list_operations(my_numbers) #function call
print(f"Sum of numbers: {result[0]}\n Maximum of numbers: {result[1]}\n Minimumof numbers: {result[2]}")  

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    high_score_name_list =[]  # emplty list to store neme according to matched condition
    for name , score in students_dict.items():        # forloop for storing name 
        if score > 80 :
            high_score_name_list.append(name)        # adding name as data to the empty list
    return high_score_name_list

students = {        # Dictionary type data structure creation
    "Hari": 67,
    "Mohan": 75,
    "Charlie": 85,
    "David": 60,
    "Eve": 92
}
print(f"Name of Students with scores above 80: {dict_operations(students)}")



def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return list(set(list1) & set(list2))  # returning the a list having common value 
list1 = [1,3,5,6,8,9,10]
list2 = [0,5,7,2,15,12,8]
print(f"Common value between two lists are:{set_operations(list1,list2)}")

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    results = {   # dictionary data structure 
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'Infinity'  # Handle division by zero
    }        
    return results
a = 10.5
b = 2.5
print(arithmetic_ops(a,b))
    

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    dict = {           # dictionary in which value is added with logical operation
                'and' : x and y ,
                'or'  : x or y ,
                'not_x': not x 
    }
    return dict

x = True
y = False
result_dict = logical_ops(x, y)

print(result_dict) 

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {

         'and': a & b,
            'or': a | b ,
            'xor': a ^ b
    }

a = 10
b = 15 
print(bitwise_ops(a,b))