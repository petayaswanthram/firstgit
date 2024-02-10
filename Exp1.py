import random
import string

# Function to generate a random color hex
def random_color_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Function to generate a random alphabetical string
def random_alphabetical_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Function to generate a random value between two integers (inclusive)
def random_value_between(min_val, max_val):
    return random.randint(min_val, max_val)

# Function to generate a random multiple of 7 between 0 and 70
def random_multiple_of_7():
    return random.randrange(0, 71, 7)

# Example usage
print("Random Color Hex:", random_color_hex())
print("Random Alphabetical String:", random_alphabetical_string(8))
print("Random Value between 3 and 8:", random_value_between(3, 8))
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_7())