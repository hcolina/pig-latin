print ("Welcome to the Pig Latin Translator!")

pyg = ("ay")

original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha() :
    print ("You chose: " + original)
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print ("")
    print ("Your new word is " + new_word)
else: 
    print ("This is not a valid entry.")