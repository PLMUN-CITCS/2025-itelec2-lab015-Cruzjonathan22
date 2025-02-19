total_sum = 0
while True:total_sum = 0
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        # Removed the `break` here so it keeps asking for input on invalid entry
    
print("The total sum is:", total_sum)