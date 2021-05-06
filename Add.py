# Take input from the user
user_input = input("Please enter three numbers: ")
print(user_input)

# Split the given input string into 3 parts
string_tokens = user_input.split(",")
print(string_tokens)

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

print(int_tokens)
# Calculate the result: a + b - c
a, b, c = int_tokens
print(a)
print(b)
print(c)
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)