# Goal: This code calculates the maximum profit you can achieve by buying and selling a stock on different days.
# The stock prices for each day are provided in an array, and the goal is to find the best day to buy and the best day to sell.

# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at array[0]: 7
# Enter the element at array[1]: 1
# Enter the element at array[2]: 5
# Enter the element at array[3]: 3
# Enter the element at array[4]: 6
# Enter the element at array[5]: 4
# Output:
# Maximum Profit: 5 (Buy on day 1 at price 1 and sell on day 4 at price 6)

def best_time(arr, n):
    cost_price = arr[0]  # Initialize the cost price with the first day's price
    max_profit = 0  # Initialize the maximum profit to 0
    for i in range(n):
        # Calculate the profit if you sell on the current day
        profit = arr[i] - cost_price
        # Update max profit if the current profit is greater
        max_profit = max(max_profit, profit)
        # Update the cost price if a lower price is found
        cost_price = min(cost_price, arr[i])
    return max_profit

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Get the result for maximum profit
result = best_time(array, size)
print(result)
