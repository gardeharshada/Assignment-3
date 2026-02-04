# Write a program to prompt user to enter userid and password. after verifying userid and password display a 4 digit random number and ask user to enter the same.if user enters the same number then show him success message otherwise failed. (Something like captcha)
correct_userid = "admin"
correct_password = "1234"

#taking input from user
userid = input("Enter User ID:")
password = input("Enter Password")

# verifying user ID and password
if userid == correct_userid and password == correct_password:
    print("User ID and password verified.")

    # Generate 4-digit random number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    # Ask user to enter captcha
    user_captcha = int(input("Enter the captcha number:"))

    if user_captcha == captcha:
        print("Success! Verification completed.")
    else:
        print("Failed! Incorrect captcha.")

else:
    print("Invalid User ID or password")


