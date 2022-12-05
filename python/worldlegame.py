secret = "award"

print()
print("Welcome to the word solving game!")
print()

letter_count = len(secret)
print(f'The secret word has {letter_count} letters.')
print(f"Your hint is _ _ _ _ _ ")

print()

guess = input("What is your guess? ")
attempt = 1

l1 = secret [0]
l2 = secret [1]
l3 = secret [2]
l4 = secret [3]
l5 = secret [4]

while guess.lower() != secret:
    print("Your guess was not correct. ")
    print()
    print("Your hint is: ")
    for index in range(len(secret)):
        l1 = secret[index]
        g1 = guess[index]
        if l1.lower() == g1.lower():
            print(l1.upper(), end = " ")
        elif g1 in secret:
            print(g1.lower(), end = " ")
        elif l1.lower() != g1.lower():
            print("_", end = " ")
        
    
    print()
    print()

    guess = input("What is your guess? ")
    print()
    attempt += 1

if guess.lower() == secret:
    print ("You guessed it!")
    print ()
    print (f'It took you {attempt} guesses.')
    print()
