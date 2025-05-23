# Thoughts
This problem was straightforward, I knew that it would involve hashing and immediately thought of having the number in the list as the key and the value as the frequency. The hardest 
part of this alogorithm was sorting the values of the dictionary in descending order, but I just used a lambda with the sort function on the values in the dictionary to resolve this.
After having the frequencies of each value sorted from largest to smallest, a for loop is implemented for 'k' times over the highest frequencies. Each iteration adds the first value
of the tuple made from the sorted function to the list. After the iteration runs 'k' times, the list is returned.
