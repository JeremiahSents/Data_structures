def power_set(s):
   
   if not s:
      return [[]]
    
   first = s[0]
   rest = s[1:]
   
   subsets_without_first = power_set(rest)
   
   subsets_with_first = add_elements_first(first ,subsets_without_first)
   


def add_elements_first(element,subsets):
    if not subsets:
        return[]



if __name__ == "__main__":
    
    input_str = input("Enter elements of the set separated by spaces:\n")
    input_list = input_str.split()
    
    result = power_set(input_list)
    
    print(f"\nThere are {len(result)} subsets.")
    print("The subsets making up the power set are:")
    print_subsets(result)