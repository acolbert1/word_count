import os.path
from os import path

#this method is for parsing through a file in the same folder.
def file_count_input():
    count = 0
    if path.exists('tesssdsdt.txt') == True:
        with open('test.txt', 'r')  as f:
            data = f.read()
            for i in data:
                if i == " ":
                    count -= 1
                count += 1
    else:
        user_input = input("What's on your mind today? ")
        for i in user_input:
            if i == " ":
                count -= 1
            count += 1
    print("oh nice, you just told me what's on your mind in " + str(count) + " words!")
            


#this method is for parsing through user input.
# def word_count_input():
#     count = 0
#     user_input = input("What's on your mind today? ")
#     for i in user_input:
#         if i == " ":
#             count -= 1
#         count += 1
#     print("oh nice, you just told me what's on your mind in " + str(count) + " words!")

    


# word_count_input()
file_count_input()

#if data exists, user input = data otherwise user_input will run