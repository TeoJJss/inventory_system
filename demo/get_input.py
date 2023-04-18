"""
This file shows how to handle invalid input from user.
Main purpose is to customize understandable error message
"""

while True:                                            # LOOP Repeat until get a valid input
    try:                                                  # Avoid receiving weird error message, we use "try-except"
        inp=int(input("Enter a number: "))                      # Request user to input integer. If user input not integer, it will auto move user to "except" block
        if inp not in range(1,6):                               # Let say we want user to input integer range 1-5, if user input is not between 1-5:
            raise Exception("We only accept number 1-5")                # to give user error, we use "raise Exception()". "raise" will bring user to "except" block directly
        break                                                   # If user is not brought to "except", means input is valid. "break" stop the loop and proceed to the next step. 
    except Exception as e:                                 # "Exception as e" will bring the error msg down
        print(e)                                                # Display the error message

        