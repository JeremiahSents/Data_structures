
# [a,b]
def power_set(s):
    # Base case
    if not s:
        return [[]]
    
    # Recursive case
    # first = [a]
    
    
    # rest = [b]
    
        
    first = s[0]
    rest = s[1:]
    
    # subsets-without_first = []
    
    subsets_without_first = power_set(rest)
    
    subsets_with_first = add_element_to_subsets(first, subsets_without_first)
    
    return subsets_without_first + subsets_with_first

def add_element_to_subsets(element, subsets):
    # Adds element to each subset (recursively)
    if not subsets:
        return []
    else:
        first_subset = subsets[0]
        rest_subsets = subsets[1:]
        
        new_subset = [element] + first_subset
        return [new_subset] + add_element_to_subsets(element, rest_subsets)

def print_subsets(subsets):
    if not subsets:
        return
    else:
        print(subsets[0])
        print_subsets(subsets[1:])

if __name__ == "__main__":
    
    input_str = input("Enter elements of the set separated by spaces:\n")
    input_list = input_str.strip().split()
    
    result = power_set(input_list)
    
    print(f"\nThere are {len(result)} subsets.")
    print("The subsets making up the power set are:")
    print_subsets(result)


# power_set(['a', 'b'])
# │
# ├── first = 'a'
# │   rest = ['b']
# │
# ├── subsets_without_first = power_set(['b'])
# │   │
# │   ├── first = 'b'
# │   │   rest = []
# │   │
# │   ├── subsets_without_first = power_set([])
# │   │   └── return [[]]   ← Base case: 1 subset (empty set)
# │   │
# │   ├── subsets_with_first = add_element_to_subsets('b', [[]])
# │   │                        = [['b']]
# │   │
# │   └── return [[]] + [['b']] = [[], ['b']]
# │
# ├── subsets_with_first = add_element_to_subsets('a', [[], ['b']])
# │                        = [['a'], ['a', 'b']]
# │
# └── return [[], ['b']] + [['a'], ['a', 'b']]
#     = [[], ['b'], ['a'], ['a', 'b']]
