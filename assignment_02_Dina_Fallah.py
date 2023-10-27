def digit_count_recursive(number):
    if number == 0:
        return 0
    else:
        return 1 + digit_count_recursive(number // 10)
    
def max_lookup(our_list):
    if not our_list:
        return None

    if len(our_list) == 1:
        return our_list[0]

    first_element = our_list[0]
    rest_of_list = our_list[1:]

    max_in_rest = max_lookup(rest_of_list)

    return max_in_rest if max_in_rest > first_element else first_element  
  
def input_list():
    while True:
        input_str = input("Enter a list of numbers separated by spaces: ")
        input_list = input_str.split()
        
        try:
            number_list = [int(x) for x in input_list]
            return number_list
        except ValueError:
            print("Invalid input. Please stop wasting my time.")



def main():
    # firstEx = int(input("Please give me a number: ")) #Code goes boom if you don't give a number

    # print(digit_count_recursive(firstEx))
    our_list = input_list()
    max_value = max_lookup(our_list)
    print("The maximum value in the list is:", max_value)


 
main()

            
        
    