# Find Maximum Single Sell Profit

Given a list of stock prices for n days, find the maximum profit with a single buy/sell activity.

## Hints
- Kadane's algorithm

## Solution

Runtime Complexity - O(n)


Memory Complexity - O(1)


### Pseudocode

A naive solution, O(n^2), is to find the maximum gain between each element and its succeeding elements.


There is a tricky linear solution of this problem that requires maintaining **current buy price** (which is the smallest number seen so far), **current profit** and **global max profit** as we iterate through the entire array of stock prices.
At each iteration, we will compare the current profit with the global profit and updat the global profit accordingly.


``` text
current profit = INT_MIN
current buy = stock_prices[0]
global sell = stock_prices[1]
global profit = global sell - current buy
for i = 1 to stock_prices.length:
    current profit = stock_prices[i] - current buy
    if current profit is greater than global profit
        then update global profit to current profit and update global sell to stock_prices[i]
    if stock_prices[i] is less than current buy then update current buy to stock_prices[i]
return global profit and global sell
```

### Implementation

``` python
# What if the array is all the same price?

def find_buy_sell_stock_prices(array):
    if array is None or len(array) < 2:
        return None

    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy

    current_profit = -1000  # what is the appropriate min?

    for i in range(1, len(array)):
        current_profit = array[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]

        if current_buy > array[i]:
            current_buy = array[i]

    result = global_sell - global_profit, global_sell

    return result
```
