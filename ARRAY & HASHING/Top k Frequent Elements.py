
# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sorting the dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Display the sorted dictionary
print(sorted_dict)

#
# # Sample dictionary
# my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
#
# # Sorting the dictionary by values
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
#
# # Display the sorted dictionary
# print(sorted_dict)
import collections
nums = [1,1,1,2,2,3]
k = 2

count = collections.defaultdict(list)

for i in nums:
   count[i]=count.get(i,0) +1
print(count)
print(list(count.keys())[:k])


