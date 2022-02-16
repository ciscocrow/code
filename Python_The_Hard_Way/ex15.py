from sys import argv

script, filename = argv

#Opens the file and sets to variable "txt"
txt = open(filename)

print("\n")
print(txt)
print("\n")

#Prints out the name of the file
print(f"here's your file {filename}:")

#uses "read function and prints out"
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
