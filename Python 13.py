"""
The Challenge: The Vault Cracker

This exercise combines everything you have learned so far. 
It is written in the descriptive paragraph format.

At the top of your script, define a function named hack_the_vault. 
Inside the parentheses, give it a single parameter named password 
(this will be the secret code the user has to guess).

Inside the function, before you start looping, create a variable 
called attempts and set it to 0. Next, start an infinite while True: loop. 
The very first thing inside this loop should be to add 1 to your attempts
variable so you can track how many guesses they have made.

Next, ask the user to input a guess by prompting them with: Enter the 
vault password: . Use an if statement to check if their guess is exactly 
equal to the password parameter. If it is a match, use the return keyword 
to hand back a formatted string that says exactly: "Access Granted! It 
took you X attempts." (Replace X with your actual attempts variable).

If they guess wrong, use an else statement to print "Access Denied. Try 
again." so the loop will automatically repeat.

Finally, step completely outside of your function (make sure you are no 
longer indented). Create a variable called vault_status and set it equal 
to your hack_the_vault function, passing in "open sesame" as the secret 
password. On the very last line, print your vault_status variable to see 
the returned message!
"""

def vault(password):

    attempts = 0

    while True:
        action = input("What action do you want to do? Quit or Access: ").strip().lower()
        attempts += 1

        if action == "quit":
            return

        elif action == "access":
            pw = int(input("Enter the password: "))
            if pw == password:
                print(attempts)
                return ("Access granted")
            else:
                print(attempts)
                print("Password wrong")

access = vault(1234)
print(access)
