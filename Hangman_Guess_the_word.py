import random
print("                 Ⓗ-Ⓐ-Ⓝ-Ⓖ-Ⓜ-Ⓐ-Ⓝ : GUESS THE WORD")

alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessed=[]
chance=10    # to be customized 

file=open("hangman_words.txt","r") # word's dictionary
word_list=file.readlines()
secret_word=(random.choice(word_list))[:-1] #removes \n
while len(secret_word)<4 or len(secret_word)>8:
    secret_word=(random.choice(word_list))[:-1]

decoded=["_"]*len(secret_word)
encoded_no=len(secret_word)
while chance!=0:
    print("**"*len(decoded))
    for alpha in decoded:
        print(alpha,end=' ')
    print()
    print("**"*len(decoded))
    print()
    if encoded_no==0:
        print("Congrats, you did it !!")
        break
    print(f"Chance Remaining :{chance} ")
    print(f"Guess the ALPHABET :-       <<Guessed so far - {guessed}>>")
    guess=input(">>>")
    while guess not in alphabets or guess in guessed:
        print()
        if guess not in alphabets:
            print("Invalid input....")
            print("Guess an alphabet :-")
        else:
            print("Already guessed...")
            print("Guess another alphabet :-")
        guess=input(">>>")
    guessed+=[guess]
    if guess not in secret_word:
        chance-=1
    else:
        for index in range(len(secret_word)):
            if secret_word[index]==guess:
                decoded[index]=guess
                encoded_no-=1
    print()
else:
    print("Sorry, you lost !!")
    print()
    print('E N C R Y P T E D  W O R D :-')
    print("--"*len(decoded))
    for alpha in secret_word:
        print(alpha,end=' ')
    print()
    print("--"*len(decoded))
    
    
        
            
        
    
    
    
