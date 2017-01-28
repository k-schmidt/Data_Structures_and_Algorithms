# Pigeonhole Principle

## Problem 1
Prove that if 6 integers are selected from {3, 4, 5, 6, 7, 8, 9, 10, 11, 12} there must be 2 integers whose sum is 15.


If you have more pigeons than holes then at least one hole must have at least two pigeons.
One of the **challenges** is figuring out what are the pigeons and what are the holes.


The numbers in the set easily pair to for sums of 15.


## Solution

Label 5 boxes with all pairs of numbers that sum to 15.
Every selected integer is placed into the box with the matching label.
We need to place 6 selected integers into 5 boxes.
So, by the **Pigeohole Principle**, one box must have at least two integers.
So there must be two integers that sum to 15.

## Problem 2
Prove that if 10 points are placed in a 3cm by 3cm square then two points must be less than or equal to sqrt(2) cm apart.

## Solution

sqrt(2) is the hypotenuse of a 1cm x 1cm square. How many 1cm by 1cm boxes can we fit into the 3cm x 3cm square?
We can fit 9 boxes into the 3cm x 3cm square.
Therefore, we have 10 points and 9 squares.
So by the **Pigeonhole Principle**, there must be a square that has more than 1 point on or within its boundary.
So this square has two points less than or equal to sqrt(2)cm apart.

## Problem 3

At a business meeting no one shakes their own hand and no one shakes another person's hand more than once.
Prove that there are 2 people who have shaken hands the same number of times.

## Solution

Start playing around with a particular example.
We have 5 people.
The people are going to be the pigeons.
The number of handshakes are the pigeonholes.
Minimum number of handshakes: 0
Maximum number of handshakes: 4
Possible number of shakes: 5? 0, 1, 2, 3, 4, 5
You can't have one person with 0 handshakes and another with 4.
Similarly, you can't have one person with 4 handshakes and all the others at 0.
So the possible number of shakes: 4.


Suppose there are n people.
The minimum number of handshakes is 0.
The maximum number of handshakes is n-1.
If someone has shaken hands with n-1 people then there can't be someone who has shaken hands with 0 people.
Similarly, if there is someone who has shaken hands with 0 people there can't be someone who has shaken hands with n-1 people.
So we have n people and at most n-1 possible handshakes.
So by the **Pigeonhole Principle**, there must be 2 people who have shaken hands the same number of times.
