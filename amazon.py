price = [31, 25, 85, 29, 35]
x = 60

def create_pairs(prices):
    pairs = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            pairs.append((prices[i], prices[j]))
    return pairs

def calculate_sum_of_pairs(pairs, x):
    result_sum = 0
    for pair in pairs:
        if pair[0] + pair[1] < x:
            result_sum += pair[0] + pair[1]
    return result_sum

# Create pairs
result_pairs = create_pairs(price)

# Calculate the sum of pairs that satisfy the condition
result_sum = calculate_sum_of_pairs(result_pairs, x)

print("Sum of pairs that satisfy the condition:", result_sum)
