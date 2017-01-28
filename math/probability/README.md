# Probability

1. **or** - `P(A) or P(B) = P(A or B) = P(A U B)`
2. **and** - `P(A) and P(B) = P(A and B) = P(A n B)`
3. **conditional** = P(A|B)

## Or
**Addition rule**, add the two probabilities together.
Probability that it rains is 20% and the probability that it snows is 15%, the probability of the two events is 35%.
We can add two events probabilities as long as they are **disjoint**.
**Disjoint** or **Mutually Exclusive** means two events cannot occur together.


If two events are not disjoint, in other words, they can occur together then you need to subtract away the probability of A and B occuring.


```P(A or B) = P(A) + P(B) - P(A and B)```

### Example
Probability that a bear is male. A bear *can* be male and brown.

```
P(male) = .45
P(brown) = .23
P(male and brown) = .15
P(male or brown) = .45 + .23 - .15 = .53
```

## And
**Multiplication rule**


Two events must be **independent**, where A does not affect B
```
P(A and B) = P(A) * P(B)
```

If two events are **dependent** where A affects B or vice versa, then `P(A and B) = P(A) * P(B|A)`

## Conditional Probability
Probability of C given D is `P(C|D) = P(C and D) / P(D)`

## Example
What is the probability that a bear is brown given it is male.

```
P(brown|male) = P(brown and male) / P(male)
P(brown|male) = .15 / .45 = .33
