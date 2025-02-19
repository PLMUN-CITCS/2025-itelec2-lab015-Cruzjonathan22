total_sum = 0  # Initialize the total sum

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")

    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    try:
        number = float(user_input)  # Try to convert input to a number
        total_sum += number  # Add the number to the total sum
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        # The loop continues asking for input on invalid entries

print("The total sum is:", total_sum)  # Print the final total sum
