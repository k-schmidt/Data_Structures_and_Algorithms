# Sum of First N Natural Numbers

Natural numbers is represented by `N`.
```N = {1, 2, 3, 4, 5, 6, ... }```

The sum of first 6 natural numbers is:
```1 + 2 + 3 + 4 + 5 + 6 = 21```

## Derivation
1. Group numbers
2. Sum each group, should be the same for each group
3. Multiply the sum of one group times number of groups

```
series = 1, 2, 3, 4, 5, 6
group1 = (1, 6)
group2 = (2, 5)
group3 = (3, 4)

sum_group1 = 7
sum_group2 = 7
sum_group3 = 7

sum_of_first_6 = 7 x 3 = 21
```

```
## Even number Series
series = 1, 2, 3, 4, 5, ... (n-2), (n-1), n
number_of_groups = n/2 if n is an even number
sum_of_each_group = n + 1
sum_of_first_n = (n+1) * (n/2)
sum_of_first_n = n(n+1)/2
```

```
## Odd number Series
series = 1, 2, 3, 4, 5
number_of_groups = n//2 since n is odd
sum_of_each_group = 6
sum_of_middle_element = n / 2 = 3
sum_of_all_groups_plus_odd = 12 + 3 = 15
## The equation n(n+1)/2 still works for odd numbered groups
```
