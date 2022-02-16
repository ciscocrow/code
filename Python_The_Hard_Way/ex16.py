from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you won't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN")

input("?")

print("Openint the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")


print("And finally, we close it.")
target.close()
