class Task:
    def __init__(self, task_id, description, priority, completed=False):
        self.__task_id = task_id
        self.__description = description
        self.__priority = priority
        self.__completed = completed

    def getTaskId(self):
        return self.__task_id

    def getDescription(self):
        return self.__description

    def getPriority(self):
        return self.__priority

    def getCompleted(self):
        return self.__completed

    def setCompleted(self, completed):
        self.__completed = completed


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.header = None
        self.size = 0

    def displayQueue(self):
        current = self.header

        while current is not None:
            print(
                f"Task ID: {current.info.getTaskId()}, Description: {current.info.getDescription()}"
            )
            current = current.next

    def enqueue(self, info):
        node = Node(info)

        if self.size == 0:
            self.header = node
            self.size += 1
            print(
                f"Successfully added task with ID {node.info.getTaskId()} and description: {node.info.getDescription()}"
            )

        else:
            if node.info.getPriority() > self.header.info.getPriority():
                node.next = self.header
                self.header = node
                self.size += 1

            else:
                current = self.header
                previous = current

                while (
                    current is not None
                    and current.info.getPriority() >= node.info.getPriority()
                ):
                    previous = current
                    current = current.next

                previous.next = node
                node.next = current
                self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Your Queue is Empty! Enqueue first.")
        elif self.size == 1:
            print("We are removing:", self.header.info.getDescription())
            self.header = None
            self.size -= 1
        else:
            print("We are removing:", self.header.info.getDescription())
            current = self.header
            self.header = self.header.next
            current.next = None
            self.size -= 1

    def getTaskById(self, task_id):
        current = self.header

        while current is not None:
            if current.info.getTaskId() == task_id:
                return current.info
            current = current.next

        return None

    def displayTasks(self):
        current = self.header

        while current is not None:
            print(
                f"Task ID: {current.info.getTaskId()}, Description: {current.info.getDescription()}, Priority: {current.info.getPriority()}"
            )
            current = current.next


class Stack:
    def __init__(self):
        self.header = None
        self.size = 0

    def isEmpty(self):
        return self.header is None

    def displayStack(self):
        current = self.header

        while current is not None:
            print("|" + str(current.info) + "|")
            current = current.next

        print("---")

    def push(self, info):
        node_to_add = Node(info)

        node_to_add.next = self.header
        self.header = node_to_add
        self.size += 1

    def peek(self):
        if self.isEmpty():
            print("You've done nothing")

        else:
            print(
                "Your most recent accomplishment: ", self.header.info.getDescription()
            )


def finishTask(task_queue: PriorityQueue, task_stack: Stack):
    if task_queue.size == 0:
        print("You have nothing to do.")
    else:
        completed_task = task_queue.header.info
        completed_task.setCompleted(True)

        task_queue.dequeue()

        task_stack.push(completed_task)

        print(f"Procrastination who? You finished: {completed_task.getDescription()}")


def setPriority():
    while True:
        print("\nPriority Scale:")
        print("1. Gintama.")
        print("2. Jujutsu Kaisen.")
        print("3. Attack on Titan.")
        print("4. Neon Genesis Evangelion.")
        print("5. Jojo's Bizarre Adventure.")
        print("6. Bleach.")
        print("7. Demon Slayer.")
        print("8. Highschool of the Dead.")
        print("9. To LOVE-Ru.")
        print("10. One Piece.")
        print("11. Boku No Pico.")

        try:
            user_answer = int(
                input(
                    "Choose the number corresponding to the importance of your task 1 being of crucial importance: "
                )
            )
            if user_answer == 1:
                print("We must begin right away!")
                return 100
            elif user_answer == 2:
                print("Yes yes, very important task.")
                return 90
            elif user_answer == 3:
                print("Kill every last one of them, tasks I mean.")
                return 80
            elif user_answer == 4:
                print("This deserves to be higher, but we have limited options.")
                return 70
            elif user_answer == 5:
                print("Yes yes, very important task.")
                return 60
            elif user_answer == 6:
                print("Quite the fruity task.")
                return 50
            elif user_answer == 7:
                print("A task is still a task.")
                return 40
            elif user_answer == 8:
                print("I can feel the haters coming, this can wait.")
                return 30
            elif user_answer == 9:
                print("You're just here for the plot.")
                return 20
            elif user_answer == 10:
                print("You have no life and plenty of time, this too can wait.")
                return 10
            elif user_answer == 11:
                print("Oh no...")
                while True:
                    print(
                        "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
                    )
                    print("FBIOPENUP")
            else:
                print("Invalid choice. Please choose a number between 1 and 11.")
        except ValueError:
            print("Do you even know what a number is?")


def addANewTask(task_queue: PriorityQueue, task_id):
    description = input("Can you describe this task of yours? ")
    priority = setPriority()
    new_task = Task(task_id, description, priority)
    task_queue.enqueue(new_task)
    print("Task added successfully.")


def main():
    my_tasks = PriorityQueue()
    task_stack = Stack()
    task_id = 1

    while True:
        print("\nOptions:")
        print("1. Add new Task.")
        print("2. Get task from id.")
        print("3. Mark high priority task as done.")
        print("4. Display tasks based on priority.")
        print("5. Display unfinished tasks.")
        print("6. Display the last completed task.")
        print("7. I think we should go our separate ways.")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Alrighty, let's add a new task.")
            addANewTask(my_tasks, task_id)
            task_id += 1

        elif choice == "2":
            my_tasks.displayQueue()
            chosen_task = input("Choose your poison: ")
            task = my_tasks.getTaskById(chosen_task)
            if task:
                print(
                    f"Task ID: {task.getTaskId()}, Description: {task.getDescription()}, Priority: {task.getPriority()}"
                )
            else:
                print("Task not found.")

        elif choice == "3":
            print("You did it! You finished: ")
            finishTask(my_tasks, task_stack)

        elif choice == "4":
            print("Displaying tasks based on priority:")
            my_tasks.displayQueue()

        elif choice == "5":
            print("Displaying unfinished tasks:")
            my_tasks.displayTasks()

        elif choice == "6":
            print("Look at your accomplishments:")
            task_stack.peek()

        elif choice == "7":
            print("Rude.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-7).")


main()
