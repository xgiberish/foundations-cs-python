import requests

VALID_DOMAINS = ('com', 'net', 'org', 'io', 'edu', 'gov', 'lb')

INVALID_CHARACTERS = '!@#$%^&*()+'

'''
For the sake of my own sanity I will be validating the site name and domain without the path
Nested tabs will be allowed to contain paths as they would contain special characters
So basically, the main tab will be the main page then I'll be verifying nested tabs according to their parent page
'''

#response = requests.get('https://oxylabs.io/')

def getUrlFromUser():
    siteName = input("Please provide the site name: ")
    siteDomain= input("Please provide the site domain: ")
    
    web_url ='https://' + siteName + '.' + siteDomain
    
    return inputValidator(web_url)

def inputValidator(web_url):
    webName, domain = web_url.rsplit('.', 1)
    
    if domain.lower() not in VALID_DOMAINS:
        print("Invalid URL domain. Yes I know I've limited your options, please deal with it.")
        return False
    elif any(character in webName for character in INVALID_CHARACTERS):
        print("What kind of a link is that?")
        return False
    else:
        print("Thank you for your cooperation.")
        return True


def openTab():
    return

def closeTab():
    return

def switchTab():
    return

def displayAllTabs():
    return

def openNestedTabs():
    return

def clearAllTabs():
    return

def saveTabs():
    return

def importTabs():
    return




def main():
    while True:
        print("\nOptions:")
        print("1. Open Tab")
        print("2. Close Tab")
        print("3. Switch tab")
        print("4. Display All tabs")
        print("5. Open Nested tab")
        print("6. Clear All Tabs")
        print("7. Save Tabs")
        print("8. Import Tabs")
        print("9. Exit")

        choice = input("What would you like to do?: ")

        if choice == "1":
            getUrlFromUser()
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print()
        elif choice == "5":
            print()
        elif choice == "6":
            print()
        elif choice == "7":
            print()
        elif choice == "8":
            print()
        elif choice == "9":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose a valid operation (1-9).")


main()


'''
Resources 

Python web scraping: 
https://www.youtube.com/watch?v=8dTpNajxaH0
https://oxylabs.io/blog/python-web-scraping

Fuctions used:
https://python-reference.readthedocs.io/en/latest/docs/str/rsplit.html
https://www.programiz.com/python-programming/methods/built-in/any


'''

