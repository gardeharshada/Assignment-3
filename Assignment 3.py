# Write a program to input any alphabet and check whether it is vowel or consonant.
ch = input("a")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The alphabet is a Vowel")
else:
    print("The alphabet is a consonant")    