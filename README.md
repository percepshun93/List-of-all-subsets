# List of all subsets
This code gives out all the subsets of any given set.

The main purpose of this block of code is to find out the all different subsets of a given set of 'n' numbers
The number of subsets of a set of 'n' numbers is 2^n
This code gives out all of these 2^n subsets

# Functionality

There is a module in python called itertools which has a function called 'combinations'
combinations takes in 2 arguments - one iterable element, and one integer
the iterable element is used to take out subsets from, using the integer to specify the number of elements you want to have in your subset

For Eg:
combinations([1,2],2) gives out a subset (1,2) i.e, having 2 elements
combinations([1,2,3],2) gives out 3 subsets - (1,2),(1,3),(2,3) i.e, all subsets having 3 elements

using this, all subsets can be found by running a single loop which increments this integer argument inside the combinations function.
