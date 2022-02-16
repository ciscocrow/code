# the one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that * args i s actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#just one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# no arguments
def print_none():
    print("i got nothing'.")

print_two("Zed", "Shaw")
print_two_again("zed", "Shaw")
print_one("First!")
print_none()
