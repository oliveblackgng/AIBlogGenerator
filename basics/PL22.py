def translate(phrase): # fn to translate phrase
    translation="" #empty string
    for letter in phrase: # for every letter in the entered phrase
        if letter in "AEIOUaeiou": # if the letter is a letter in the vowels set
            translation=translation+ "!"
        else :
            translation=translation+letter
    return translation
print(translate(input("Enter a phrase: "))) #print the output
#indent*