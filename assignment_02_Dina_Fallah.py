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
 
 #Last ex           
def is_2d_matrix(matrix):
    if not all(isinstance(row, list) for row in matrix):
        return False 
    if len(set(len(row) for row in matrix)) != 1:
        return False 
    return True

def input_2d_matrix():
    matrix = []
    
    while True:
        try:
            rows = int(input("Enter the number of rows in the matrix: "))
            cols = int(input("Enter the number of columns in the matrix: "))
            
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            
            for _ in range(rows):
                row = input(f"Enter {cols} elements for a row separated by spaces: ").split()
                if len(row) != cols:
                    print("Each row should have the same number of elements.")
                    matrix.clear()
                    break
                matrix.append([int(x) for x in row])
            
            if is_2d_matrix(matrix):
                return matrix
            else:
                print("Invalid input. Please make sure all rows have the same number of elements.")
                matrix.clear()
        except ValueError:
            print("Invalid input. Please enter valid integers for rows and columns.")

def our_mean(column):
    return sum(column) / len(column)

def standard_deviation(column, mean):
    squared_diff = [(x - mean) ** 2 for x in column]
    variance = sum(squared_diff) / len(column)
    std_deviation = variance ** 0.5
    return std_deviation

def matrix_final_check(matrix, column = 0, count = 0):
    num_columns = len(matrix[0])

    if column == num_columns:
        return count

    current_column = [row[column] for row in matrix]
    mean = our_mean(current_column)
    std_deviation = standard_deviation(current_column, mean)

    if mean == 0 and std_deviation == 1:
        count += 1

    return matrix_final_check(matrix, column + 1, count)

def main():
    while True:
        choice = input("Choose your operation: \n1) Count Digits.\n2) Find Max.\n3) Count Normalized Columns.\nType 'exit' to quit: ")
        
        if choice == 'exit':
            break
        
        choice = int(choice)
        
        if choice == 1:
            firstEx = int(input("Please give me a number: "))  # Code goes boom if you don't give a number
            print(digit_count_recursive(firstEx))
        elif choice == 2:
            our_list = input_list()
            max_value = max_lookup(our_list)
            print("The maximum value in the list is:", max_value)
        elif choice == 3:
            matrix = input_2d_matrix()
            count = matrix_final_check(matrix) 
            if count > 0:
                print(f"{count} column(s) have a mean of 0 and a standard deviation of 1.")
            else:
                print("No columns have a mean of 0 and a standard deviation of 1.")
        else:
            print("Invalid choice. I literally told you what the options are.")
 
main()

            
        
    