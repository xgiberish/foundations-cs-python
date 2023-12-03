# Sweet home Alabama
class Node:
    def __init__(self, input_info):
        self.__info = input_info
        self.__children = []


# End of Node class


class Tree:
    def __init__(self):
        self.root = Node(
            {"id": 1, "Name": "Root", "Family Name": "Root", "Birthday": "Eternal"}
        )
        self.node_counter = 2

    def displayNodes(self, node, indent=""):
        if node is not None:
            print(
                f"{indent}{node.info['id']}) {node.info['Name']} {node.info['Family Name']}"
            )
            for child in node.children:
                self.displayNodes(child, indent + "  ")

    def showNodes(self):
        print("\nCurrent Family Members:")
        self.displayNodes(self.root)

    def search(self, data, node):
        if node is None:
            return None

        if data == node.info["name"]:
            print(node.info["name"], "found")
            return node

        for child in node.children:
            found_node = self.search(data, child)
            if found_node is not None:
                print(found_node.info["name"], "found")
                return found_node

    def addChild(self, parent_node_id, child_data):
        parent_node = self.findNodeById(parent_node_id, self.root)

        if parent_node is not None:
            child_data["id"] = self.node_counter
            self.node_counter += 1
            parent_node.children.append(Node(child_data))
            print(f"{child_data['name']} added to the family tree.")
        else:
            print("Parent node not found.")

    def findNodeById(self, node_id, node):
        if node is None:
            return None

        if node.info["id"] == node_id:
            return node

        for child in node.children:
            found_node = self.findNodeById(node_id, child)
            if found_node is not None:
                return found_node

        return None


## End of Tree class


def getBirthday():
    try:
        birth_year = int(input("What year was this person born: "))
        if birth_year > 2023:
            print("What are you some sort of psychic?")
            return
        birth_month = int(input("What month (1-12): "))
        if birth_month < 1 or birth_month > 12:
            print("Have you ever seen a calendar in your life?")
            return
        birth_day = int(input("What day (1-31): "))
        if birth_day < 1 or birth_day > 31:
            print("You're trying to trick me...")
            return
    except ValueError:
        print("Try again...")

    return birth_year, birth_month, birth_day


def addFamilyMember(family_tree, parent_id, first_name, last_name, birthday):
    try:
        parent_id = int(parent_id)

        if parent_id <= 0 or parent_id >= family_tree.node_counter:
            print("Invalid parent ID. Please choose a valid ID.")
            return

        child_data = {
            "id": family_tree.node_counter,
            "Name": first_name,
            "Family Name": last_name,
            "Birthday": birthday,
        }
        family_tree.addChild(parent_id, child_data)

    except ValueError:
        print("Invalid input. Please enter valid information.")


def main():
    family_tree = Tree()

    while True:
        print("\nWelcome! Here are your options: ")
        print("1) Add A Family Member.")
        print("2) Display Sorted Birthdays. (Oldest to youngest)")
        print("3) Find Relationship.")
        print("4) Visualize Family Tree.")
        print("5) Count Same First Names.")
        print("6) Exit. (The programm that is)")

        user_choise = int(input("What would you like to do?"))
        try:
            if user_choise == 1:
                print("Let's add a new member:")
                first_name = input("Provide a first name: ")
                last_name = input("Provide a last Name: ")
                birthday = getBirthday()
                family_tree.displayNodes()
                parent_id = "Choose the id of the parents: "
                addFamilyMember(family_tree, parent_id, first_name, last_name, birthday)

            elif user_choise == 2:
                print()
            elif user_choise == 3:
                print()
            elif user_choise == 4:
                print()
            elif user_choise == 5:
                print()
            elif user_choise == 6:
                print("Thank you for using me... Reminds me of my ex...")
                break
            else:
                print(
                    "It looks like something is off... Maybe try picking an actual option?"
                )
        except ValueError:
            print("Please pick a valid option...")
