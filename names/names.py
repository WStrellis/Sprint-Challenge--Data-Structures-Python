import time
# from doubly_linked_list_modified import DoublyLInkedList as DoublyLinkedListMod
from lru import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names O(n)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names O(n)
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements

all_names = names_1 + names_2
lrucache = LRUCache(20000)
for name in all_names:
    # if the name is already in the cache add to duplicates
    if lrucache.get(name):
        duplicates.append(name)
    lrucache.set(name, name)

# for name in names_1:
#     if lrucache.get(name):
#         duplicates.append(name)
#     lrucache.set(name, name)

# for name in names_2:
#     if lrucache.get(name):
#         duplicates.append(name)
#     lrucache.set(name, name)

# 4.5 seconds
# dll = DoublyLinkedListMod()
# for name in names_1:
#     # add item to dll
#     unique_name = dll.add_to_head(name)
#     # add name to duplicates if it was added to dll
#     if unique_name:
#         duplicates.append(unique_name)

# for name in names_2:
#     # add item to dll
#     unique_name = dll.add_to_head(name)
#     # add name to duplicates if it was added to dll
#     if unique_name:
#         duplicates.append(unique_name)


# for name_1 in names_1:  # O(n)
#     for name_2 in names_2:  # O(n)
#         if name_1 == name_2:  # O(1)
#             duplicates.append(name_1)

#runtime: O(n^2)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
