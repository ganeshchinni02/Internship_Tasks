# Q1. Find the Frequency of Each Word in a Sentence
from solutions import word_frequency
sentence = "python is easy and python is powerful"
sentence1="M.S Dhoni is a great cricketer and M.S Dhoni is a great captain"
print(word_frequency(sentence))
print(word_frequency(sentence1))

# Q2. Find the Frequency of Each Character in a Word
from solutions import character_frequency
print(character_frequency("mahendra singh dhoni"))
print(character_frequency("bhuvneshwar kumar"))

# Q3. Find the First Non-Repeating Character in a Word
from solutions import first_non_repeating_character
print(first_non_repeating_character("cover drive"))   
print(first_non_repeating_character("helicopter"))

# Q4. Check Whether Two Strings Are Anagrams
from solutions import are_anagrams
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))

#Q5. Find the First Repeating Character in a String
from solutions import first_repeating_character
print(first_repeating_character("MahendraSinghDhoni")) 
print(first_repeating_character("sureshRaina"))

#Q6. Move All Zeros to the End of a List
from solutions import move_zeros_to_end
numbers = [0, 1, 2, 0, 3, 4, 0, 5]
numbers1 = [0, 0, 0, 1, 2, 3]
print(move_zeros_to_end(numbers))
print(move_zeros_to_end(numbers1))

#Q7. Find the Second Highest Distinct Number in a List
from solutions import second_highest_distinct
numbers = [10, 20, 30, 40, 50]
numbers1 = [5, 10, 15, 20, 25]
print(second_highest_distinct(numbers))  
print(second_highest_distinct(numbers1))

#Q8. Remove Duplicates Without Changing the Original Order
from solutions import remove_duplicates_preserve_order
numbers = [1, 2, 3, 2, 4, 3, 5]
numbers1 = [10, 20, 30, 20, 40, 30, 50]
print(remove_duplicates_preserve_order(numbers))
print(remove_duplicates_preserve_order(numbers1))

#Q9. Find the Missing Number from 1 to N
from solutions import find_missing_number
numbers = [1, 2, 4, 5, 6]
numbers1 = [1, 2, 3, 5, 6]
print(find_missing_number(numbers, 6))
print(find_missing_number(numbers1, 6))

#Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import two_sum_first_pair
numbers = [2, 7, 11, 15]
numbers1 = [3, 2, 4]
target = 9
print(two_sum_first_pair(numbers, target))
print(two_sum_first_pair(numbers1, target))

#Q11. Find the Number Closest to Zero in a List
from solutions import closest_to_zero
numbers = [3, -2, 5, -1, 0, 4]
numbers1 = [-5, -3, -1, 2, 4]   
print(closest_to_zero(numbers))
print(closest_to_zero(numbers1))


# Q12. Find Common Elements Between Two Lists
from solutions import common_elements
list1 = [1, 2, 3, 4, 5]
list3 = ['apple', 'banana', 'cherry']           
print(common_elements(list1))
print(common_elements(list3))

#Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import max_consecutive_pair_sum
numbers = [1, 2, 3, 4, 5]
numbers1 = [10, 20, 30, 40, 50]
print(max_consecutive_pair_sum(numbers))
print(max_consecutive_pair_sum(numbers1))

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import all_unique_pairs
numbers = [1, 2, 3, 4, 5]
numbers1 = [2, 4, 6, 8, 10]
print(all_unique_pairs(numbers, 5))
print(all_unique_pairs(numbers1, 10))

