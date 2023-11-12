import requests
import json

VALID_DOMAINS = ('com', 'net', 'org', 'io', 'edu', 'gov', 'lb')

INVALID_CHARACTERS = '!@#$%^&*()+'

'''
For the sake of my own sanity I will be validating the site name and domain without the path
Nested tabs will be allowed to contain paths as they would contain special characters
So basically, the main tab will be the main page then I'll be verifying nested tabs according to their parent page
'''


def validateTabIndex(user_tabs, tab_index):
    if tab_index is not None and tab_index.isdigit() and (0 < tab_index < len(user_tabs)):
        return tab_index
    elif tab_index is not None and not tab_index.isdight():
        print("That is not a number...")
    else:
        print("UNACCEPTABLEEEE")
    

def getUrlFromUser():
    siteName = input("Please provide the site name: ")
    siteDomain= input("Please provide the site domain: ")
    
    web_url ='https://' + siteName + '.' + siteDomain
    
    return web_url

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
    
def nestedValidator(user_tabs):
    parent_index = print("Which tab would you like to nest in?")
    if validateTabIndex(parent_index):
        parent_url = user_tabs[parent_index]["URL"]
                
        child_url = getUrlFromUser()
        
        child_base = child_url.rsplit('.', 1)
        
        child_tab = openTab(child_url)
        
        if child_base != parent_url:
            print("That's not a valid child for this tab.")
        else:
            openNestedTabs(user_tabs, parent_index, child_tab)
        
        #I may have not understood this one clearly, but I worked on it as if we're on the same site and we're going to different pages within it
        #Anyway it's too late to back down now, I've had a lot on my plate lately
    else:
        return
    

def openTab(user_tabs, title, url):
    tab_index = len(user_tabs) + 1
    new_tab= {"Title": title, "URL": url,"Nested":'' ,"Tab Index: ": tab_index}
    user_tabs.append(new_tab)
    
    return print(f"Succesfully added {title} as a new tab.")

def closeTab(user_tabs, close_me):
    
    if close_me is None:
        user_tabs.popitem()
    elif validateTabIndex(user_tabs, close_me):
        user_tabs.pop(close_me) 
    else:
        print("Something is not right here.")
        
def displayHTML(web_url):
    try:
        current_tab = requests.get(web_url)
        print(current_tab.text)
    except:
        print(f"We faced an issue getting to {web_url}")
    

def switchTab(user_tabs):
    displayAllTabs(user_tabs)
    tab_index = input("Which tab would you like to switch to? ")
    
    if tab_index is not None and tab_index.isdigit() and (0< tab_index < len(user_tabs)):
        displayHTML(user_tabs[tab_index]['URL'])
    elif tab_index is not None and not tab_index.isdigit():
        print("That's not an option...")
    
        
def displayAllTabs(user_tabs):
     for tab in user_tabs:
        if tab.get("is_closed", 0) == 0:
            print("Your current open tabs are: ")
            print(f"Title: {tab['Title']}, Nested: {tab['Nested']}, Tab Index: {tab['Tab Index: ']}")

def openNestedTabs(user_tabs, parent_index, child_tab):
    user_tabs[parent_index["Nested"]] = child_tab

def clearAllTabs(user_tabs):
    input = input("Are you sure about this? if so then what's the best anime out there? If you get it right then I'll clear everything.")
    if input == 'Gintama':
        user_tabs.clear()
        return("It's done.")
    else:
        print("You've failed")
        return

def saveTabs(user_tabs):
    add_to = ".json"
    user_json = input("Input a name for your file, we'll handle converting it to a json file: ")
    user_json.join(add_to)
    with open(user_json, 'w') as json_file:
        json.dump(user_tabs, json_file, indent = 2)
    print(f"File {user_json} saved.")

def importTabs():
    import_file = input("Please provide the file name to be imported: ")
    
    try:
        with open(import_file, 'r') as json_file:
            imported_tabs = json.load(json_file)
        print(f"Tabs imported succesfully.")
        displayAllTabs(imported_tabs)
    except:
        print("We faced an issue importing your files... ")




def main():
    user_tabs = []
    
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
            initial_url = getUrlFromUser()
            web_url = inputValidator(initial_url)
            if(web_url):
                web_title=input("What title would you like to give it? ")
                openTab(user_tabs, web_title, web_url)
                displayHTML(web_url)
                
                
        elif choice == "2":
            close_me = print("Which tab would you like to close? ")
            closeTab(close_me)
            
        elif choice == "3":
            switchTab(user_tabs)
            
        elif choice == "4":
            displayAllTabs(user_tabs)
            
        elif choice == "5":
            print()
            
        elif choice == "6":
            clearAllTabs(user_tabs)
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

Methods used:
https://python-reference.readthedocs.io/en/latest/docs/str/rsplit.html
https://www.w3schools.com/python/python_ref_dictionary.asp

Json file saving:
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
https://www.geeksforgeeks.org/json-dumps-in-python/

'''


