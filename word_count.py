#ask the user for input
#count each word in the input until there is nothing left to count. search google for: if there is a space continue until the next letter then resume counting?
#print the number of words in the 



def word_count_input():
    count = 0
    user_input = input("What's on your mind today? ")
    for i in user_input:
        if i == " ":
            count -= 1
        count += 1
    print("oh nice, you just told me what's on your mind in " + str(count) + " words!")

    


word_count_input()