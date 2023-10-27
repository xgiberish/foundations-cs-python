def factorial(number):
    result = 1
    if number <= 1:
        print("What part of a positive number did you not understand?")
        return None
    elif number == 0:
        return result
    else:
        for i in range(1,number+1):
            result *= i
        print("Your result is: ", result)
        
def divisors(number):
    results = list()
    if number< 1:
        print("You get nothing.")
    else:
        for i in range(1, number+1):
            if  number%i == 0:
                results.append(i)
        return results
    
def reverseString(line):
    newWord = []
    for i in range(len(line) - 1, -1, -1):
           newWord.append(line[i])
    return "".join(newWord)

def evenNumbers(numberList):
    evenNumbers= []
    numbers = numberList.split()
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            evenNumbers.append(numbers[i])
    
    return evenNumbers

def passwordChecker(password):
    specialCharacters = ['#', '?', '!', '$', '@','%','^','&','*']
    if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password) or not any(char in specialCharacters for char in password):
        return "Weak, do you even lift?"
    return "Strong password"

def descriptiveStatistics():
    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = input_str.split()
    
    fancyNumbers = [int(item) for item in input_list]

    meanResult = sum(fancyNumbers) / len(fancyNumbers)
    sorted_numbers = sorted(fancyNumbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        medianResult = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        medianResult = sorted_numbers[n // 2]

    max_count = 0
    modeResult = None
    for num in fancyNumbers:
        count = fancyNumbers.count(num)
        if count > max_count:
            max_count = count
            modeResult = num

    if max_count == 1:
        modeResult = "No mode"
    
    rangeResult = max(fancyNumbers) - min(fancyNumbers)
    
    squared_differences = [(x - meanResult) ** 2 for x in fancyNumbers]
    varianceResult = sum(squared_differences) / len(fancyNumbers)
    
    standardDeviation = varianceResult ** 0.5

    print("Mean: ", meanResult)
    print("Median: ",medianResult)
    print("Mode: ", modeResult)
    print("Range: ", rangeResult)
    print("Variance: ", varianceResult)
    print("Standard Deviation: ", standardDeviation)

    
    

def main():
    #Factorial testing
    
    ''' 
    number3 = input("Gimme a word so I can do a magic trick: ")
    print("Fancy: ", reverseString(number3))
    number = int(input("Please provide a positive number: "))
    result = factorial(number)
    if result is not None:
         print("Your factorial: ", result)
        
    #Divisors
    number2 = int(input("Gimme a special number: "))
    result2 = divisors(number2)
    print("Your special list: ", result2)
    
    #String reversal
 
    #Even numbers
    number4= input("Gimme a nice list seperate them by a space: ")
    print("Your even numbers are: ", evenNumbers(number4))
    
    #Stonks
    yourPassword = input("What's your password? ")
    print("Hm, I wonder if I can use that...", passwordChecker(yourPassword))
    
    #FSD Specials
    descriptiveStatistics()
'''
    
    
main()
