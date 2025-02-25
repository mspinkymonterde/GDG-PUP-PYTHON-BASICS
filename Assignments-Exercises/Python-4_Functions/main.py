# Function to create a greeting message
def create_greeting(name):
    """
    Create a personalized greeting message.
    Parameters:
        name (str): The name to include in the greeting.
    Returns:
        str: The greeting message.
    """
    return f"Hello {name}, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

while True:
    name = input("Enter your name: ").strip()
    if name.isalpha() or (" " in name and name.replace(" ", "").isalpha()):
        break
    print("Invalid input: Please enter your name (no numbers and special character).")

# Display the greeting message
print(create_greeting(name))
