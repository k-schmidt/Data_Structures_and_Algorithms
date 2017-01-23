# Object Oriented Design

## How to Approach

1. Handle Ambiguity
    + When being asked an object-oriented design question, you should inquire *who* is going to use it and *how* they are going to use it.
    + Example: Coffee Maker
        + Your coffee maker might be an industrial machine designed to be used in a massive restaurant servicing hundreds of customers per hour and making ten different kinds of coffee products.
        + Or it might be a simple machine, designed to be used by the elderly for just simple black coffee.
        + The use cases will significantly impact the design.
2. Define the Core Objects
    + Suppose we are asked to do the object-oriented design for a restaurant. Our core objects might be things like Table, Guest, Party, Order, Meal, Employee, Server, and Host.
3. Analyze Relationships
    + Which objects are members of which other objects?
    + Do any objects inherit from any others?
    + Are relationships many-to-many or one-to-many?
    + Example: Restaurant
        + Party should have an array of Guests.
        + Server and Host inherit from Employee.
        + Each Table has one Party, but each Party may have multiple Tables.
        + There is one Host for the Restaurant.
    + Be very careful, you can often make incorrect assumptions.
        + A single Table may have multiple parties (if it is a communal table)
4. Investigate Actions
   + Consider the key actions that the objects will take and how they relate to each other.
   + May need to update your design.

## Design Patterns

### Singleton Class
Ensures that a class has only one instance and ensures access to the instance through the application.
It can be useful in cases where you have a "global" object with exactly one instance.
The Singleton design patter can interfere with unit testing.

### Factory Method
Offers an interface for creating an instance of a class, with its subclasses deciding which class to instantiate.
You may want to implement this with the creator class being abstract and not providing an implementation for the Factory method.
Or, you could have the Creator class be a concrete class that provides an implementation for the Factory method.
In this case, the Factory method would take a parameter representing which class to instantiate.
