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
        print(f"Thank you for your cooperation. Tab now open {web_url}")
        return web_url


def openTab(user_tabs, title, url):
    tab_index = len(user_tabs) + 1
    new_tab= {"Title": title, "URL": url,"Nested":'' ,"Tab Index: ": tab_index ,"is_closed": 0}
    user_tabs.append(new_tab)
    
    return print(f"Succesfully added {title} as a new tab.")

def closeTab(user_tabs, close_me, current_tab):
    
    if close_me is None:
        user_tabs[current_tab]["is_closed"] = 1
    elif close_me is not None and close_me.isdigit() and (0 < close_me < len(user_tabs)):
        user_tabs[close_me]["is_closed"] = 1
    elif close_me is not None and not close_me.isdight():
        print("Are you messing with me?")
        return
    else:
        print("Something is not right here.")
    

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
    user_tabs = []
    current_tab = ''
    
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
            web_url = getUrlFromUser()
            if(web_url):
                web_title=input("What title would you like to give it?")
                openTab(user_tabs, web_title, web_url)
                current_tab = requests.get(web_url)
                print(current_tab)
                
        elif choice == "2":
            close_me = print("Which tab would you like to close? ")
            
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


'''

