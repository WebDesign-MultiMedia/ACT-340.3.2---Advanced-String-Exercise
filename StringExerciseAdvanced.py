# Problem 1
print("Problem 1")
wiseWord = "You learn more from failure than from success."
print(wiseWord[0:4]) # You 
print(wiseWord[4:9]) # learn
print(wiseWord[10:14]) # more
print(' ')

# Problem 2
print("Problem 2")
print(wiseWord.replace("."," !")) # You learn more from failure than from success.
print(' ')

# Problem 3
print("Problem 3")
new_str =  "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"
print(new_str, ": Original string ")
print(new_str.lower(), ": Lower case string ")
print(' ')

# Problem 4
print("Problem 4")
print(new_str.upper(), ": Upper case string ")
print(' ')

# Problem 5
print("Problem 5")
new_str1 = "There are no traffic jams along the extra mile."
print(new_str1)
print(new_str1.startswith("Z"), 'no "Z"') # False
print(new_str1.startswith("t"), ' no "t"') # False
print(' ')

# Problem 6
print("Problem 6")
print(new_str1)
print(new_str1.index("j"), ' "j" is at the index of 21') # 
print(' ')

# Problem 7
print("Problem 7")
print(new_str1)
a = new_str1.count("t")
b = new_str1.count("o")
print(f"The letter 't' appears {a} times and the letter 'o' appears {b} times")
print(' ')

# Problem 8
print("Problem 8")
greeting = "Good Morning!"
print(len(greeting), ' length')  # 13
print(' ')

# Problem 9
print("Problem 9")
alphabet= "abcdefghijklmnopqrstuvwxyz"
print(alphabet.isalnum(), ': isalnum') # b'abcdefghijklmnopqrstuvwxyz'
print(alphabet.isalpha(), ': isalpha') # True
print(alphabet.isascii(), ': isascii') # True
print(' ')

# Problem 10
print("Problem 10")
learning = "Learning is fun!"

x = learning.find("y")
print(x)

# z = learning.index("y")
# print(z)
print(' ')

# Problem 11
print("Problem 11")
count_string= "Twinkle twinkle little star, how I wonder what you are"
print(count_string.count("Twinkle"), ' "Twinkle" appears 1 times')
print(count_string.count("twinkle"), ' "twinkle" appears 1 times')
print(count_string.count("star"), ' "star" appears 1 times')
print(count_string.count("little"), ' "little" appears 1 times')
print(count_string.count("how"), ' "how" appears 1 times')
print(count_string.count("wonder"), ' "wonder" appears 1 times')
print(count_string.count("what"), ' "what" appears 1 times')
print(count_string.count("you"), ' "you" appears 1 times')
print(count_string.count("are"), ' "are" appears 1 times')
