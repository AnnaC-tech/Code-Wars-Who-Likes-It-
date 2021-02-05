# Code-Wars-Who-Likes-It-
Solution for on Code Wars; Who Likes It? 
Read Me
Code Wars - Who Likes It? This kata was solved in Python.
I am a Junior Programmer with a non-CS background who is learning to code.

Instruction - Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

It also has to pass random tests with multiples names instances.

I first started by using the already created function def likes(names), I created a variable called n_likes and assigned the value of the length of the parameter names to it. 
After this I used an if and return statement to check for conditions in the examples that were given to me.
The last line of code was used to check both the example I had to test for, and to also test for random examples. 

I used an else statement here, following the pattern for the previous examples, and using the len function on the names parameter, and specifying what positional index of the array should be displayed, when showing the result of names who liked.

After submitting this I found a solution by davisj(Patrick_Yuan) on Code Wars that had used the format method, which simplified the code and erased the need for if statements, but used something akin to a switch statement that is used in Javascript.

I hope this helps!
