# Introduction to Hash Tables

Hash Tables have:
- Keys
- Values


At the heart of a hash table is an array structure.
We are going to write a hash function that is going to look at a certain key, evaluate that key, and spit out an index number and tell us where to store the value in the array.


```
Hash(key) -> index
Everytime you enter that key you will get that index number.
```

Two keys can 'hash' to the same index.
There are many different ways to avoid a collision.
One way to get around it is to create a linked list pointing to the other value.
This is called 'chaining'.
