1.
Since there is no information regarding the source of the input there must be a validation for the input
data. It can be ether wrong type data or non-possible manipulation that can cause a crash of the function.

2. Initial assumed that i've been told on this assignment that the input function is a valid one will not crush me.
In case there were any doubts i would check the function for valid input. In any case the using an "eval" method
must be done with caution since .sys commands can be passed through.

3.
Split the queries by equal sizes to the minimum possible. The reason to use a generator in to leave an option to
use a multithreading or other assyncrony options to make a simultanious queries.
Best way From the start was not doing this as a function but to build a class and then
in case some change comes like we see here we could make a class that inherits from the basic and just has
additional init parameter like chunk size.


