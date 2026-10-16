
# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    frequency = {}
    for word in sentence.lower().split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
#Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    for char in word:
        if word.count(char) == 1:
            return char
    return None

# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
# Q5. Find the First Repeating Character in a String
def first_repeating_character(word):
    for char in word:
        if word.count(char) > 1:
            return char
    return None

#Q6. Move All Zeros to the End of a List
def move_zeros_to_end(numbers):
    result = []
    for num in numbers:
        if num != 0:
            result.append(num)
    for num in numbers:
        if num == 0:
            result.append(num)
    return result

#Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(numbers):
    unique = list(set(numbers))
    unique.sort(reverse=True)
    if len(unique) >= 2:
        return unique[1]
    else:
        return None

#Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

#Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    for num in range(1, n + 1):
        if num not in nums:
            return num
    return None


#Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []

# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num
    return closest

# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result

#Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_pair_sum(nums):
    maximum = nums[0] + nums[1]
    for i in range(len(nums) - 1):
        total = nums[i] + nums[i + 1]
        if total > maximum:
            maximum = total
    return maximum

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs(nums, target):
    result = []
    for i in nums:
        for j in nums:
            if i < j and i + j == target:
                if [i, j] not in result:
                    result.append([i, j])
    result.sort()
    return result