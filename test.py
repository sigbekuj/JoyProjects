#splitting string of characcters every 2 characters and if theres no second pair then replace wihe _

def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]

# Example usage:
#print(solution("abcdef"))  # Output: ['ab', 'cd', 'ef']
#print(solution("abcde"))   # Output: ['ab', 'cd', 'e_']

#____________________________________________________#
def selection_sort(numbers):
    
    n = len(numbers)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return print(numbers) 
        
        
#____________________________________________________#
def sum_two_smallest_numbers(numbers):
        sum = numbers[0] + numbers[1]
        return print(sum)


#numbers = [3, 6, 10,1,45,32]
#selection_sort(numbers)  
#sum_two_smallest_numbers(numbers)
            

#two sum#

#____________________________________________________#
class Solution:
    def twoSum(self, nums, target):
        num_map = {} #dictionary to store value and its index
        for i, num in enumerate(nums):
            complement = target - num #find the complement
            if complement in num_map:
                return [num_map[complement], i] #return indices of the two numbers
            num_map[num] = i #store the current number adn its index
        return[]

#nums = [2,7,11,15]
#target = 9
#print(Solution().twoSum(nums, target))

#________________________________________________#
#convert a string into a new string where the repeating letters show as ")" and single letters "("
def duplicate_encode(word):
    word = word.lower()
    new_string = [ ]
    for char in word:
        if word.count(char) == 1:
            new_string.append("(")
        else:
            new_string.append(")")
    return "".join(new_string)


print(duplicate_encode("success"))
print(duplicate_encode("meme"))
print(duplicate_encode("joy"))
