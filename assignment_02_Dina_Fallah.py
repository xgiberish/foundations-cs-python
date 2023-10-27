def digit_count_recursive(number):
    if number == 0:
        return 0
    else:
        return 1 + digit_count_recursive(number // 10)

def main():
    firstEx = int(input("Please give me a number: ")) #Code goes boom if you don't give a number

    print(digit_count_recursive(firstEx))

    
main()

            
        
    