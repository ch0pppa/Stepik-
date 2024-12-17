words = []

# Input loop
for i in range(1, 5):
    line = input()
    words.append(line)

# Find min and max words
min_word = min(words)  # Get the smallest word
max_word = max(words)  # Get the largest word

# Calculate answer
answer = pow(ord(min_word[-1]) * ord(max_word[-1]), 2)

print(answer)