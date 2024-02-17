import time

# Define a decorator function called timer
def timer(func):
    # Define a wrapper function inside the decorator
    def wrapper(*args, **kwargs):
        # Measure the start time
        start_time = time.time()
        # Call the original function with the provided arguments and keyword arguments
        result = func(*args, **kwargs)
        # Measure the end time
        end_time = time.time()
        # Calculate the execution time
        execution_time = end_time - start_time
        # Print the execution time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        # Return the result of the original function
        return result
    # Return the wrapper function
    return wrapper

# Apply the timer decorator to the calculate_sum function
@timer
def calculate_sum(n):
    # Calculate the sum of numbers from 1 to n
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Call the calculate_sum function with an argument
result = calculate_sum(1000000)
# Print the result
print("Sum:", result)


