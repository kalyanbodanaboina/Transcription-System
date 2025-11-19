#!/usr/bin/env python
# coding: utf-8

# In[2]:


def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common 

# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = find_common_elements(list1, list2)
print(result)  # Output: [3, 4]


# In[3]:


def word_frequency(sentence):
    # Convert to lowercase
    sentence = sentence.lower()

    # Split into words
    words = sentence.split()

    # Dictionary to store word counts
    freq = {}

    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq

# Example
sentence = "the cat and the hat"
result = word_frequency(sentence)
print(result)  # Output: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}


# In[ ]:




