"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""

"""
I find lambdas, or anonymous functions, to be really useful when attempting complex functions on large lists of data, or functions that require other functions.

For example, I used a lambda expression to sort dictionary values by their keys. Here is an example:

Suppose we have a dictionary where each key, a name, has a value that is an integer, an age.

E.g.
names =
{
    'bob': 50
    'sally': 28
    'tim': 15
}

How would we sort this by their age? One method is to use lambdas, as follows:

sorted_names = sorted(names.items(), key = lamda kv: kv[1])

Lamdas allow us to use a short function when necessary without defining them, hence an "anonymous" function.

A common use for anonymous functions are when you use a function like map() of filter(). However, you can usually accomplish the same thing using list comprehenseion, which is another cool thing you can do in python!

E.g.
filter = [x for x in list if x > 0]

With list comprehension, we don't have to always write a for loop to accomplish something. It makes the code quite elegent and easy to understand.

By the way, here is a joke I saw on reddit a while back for a sorting algorithm:

In Stalin_sort, you iterate down a list of elements checking if they're in order. If they are out of order they get elmintaed. By the end you have a sorted list.
"""