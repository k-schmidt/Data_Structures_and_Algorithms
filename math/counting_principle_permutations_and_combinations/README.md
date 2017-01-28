# The Counting Principle, Permutations, and Combinations

## Counting Principle

### Example
If I have three pants and 4 shirts. Using the **counting principle** I can wear 12 outfits (`3x4`). If I also have two pairs of shoes then the number of outfits has doubled, 24.

### Couting Principle Defintion

When there are `m` ways to do one thing, and `n` ways to do another, there are `mxn` ways of doing both.

### Further Example
Lets say there is a lock with 5 slots each having 10 digits. Then the number of possibilities are `10x10x10x10x10 = 100,000` or 10^5. If there are now 6 slots then the number of possibilities in 10^6. If there are 12 numbers to choose from, then the possibilities change to 12^6.

### Counting Principle Formula
**Permutation with Repetition**


n^r where n is the number of things to choose from and r is how many times you choose.


**Permutation without Repetition** - When you choose a card from a deck and don't put it back.


n! where n is the number of things to choose from.


##Permutations
### Permutation without Repetition Example
Lets say you want a 4 digit password where the characters cannot be repeated.


WATCHOUT! The answer is **not** 26! because we only want the first 4. The answer is `26!/(26-4)!`.

### Formula

`n!/(n-r)!` where n is the number of things to choose from and r is how many times you choose.


Many times you will see `nPr` in mathematical notation.

## Combinations
### Combinations without Repetition
Permutations and Combinations are different for each order of choices whereas combinations are the same no matter the order.
Order matters for Permutations.
There are always `r!` more ways to make permutations than combinations.

### Formula

`Combinations = n!/r!(n-r)!` = `nCr`
