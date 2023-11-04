def getAverage(data_frame):
    score_dict = {}

    for student in data_frame:
        name = student["Name"]
        scores = student["Scores"]

        student_average = sum(scores) / len(scores)

        score_dict[name] = student_average

    return score_dict


def getYougest(data_frame):
    youngest_student = data_frame[0]  # Dictionaries are ordered now, don't come for me
    for student in data_frame[1:]:
        if student["Age"] < youngest_student["Age"]:
            youngest_student = student

    return youngest_student["Name"]


def getHighest(data_frame):
    score_sums = {}

    for student in data_frame:
        total_score = sum(student["Scores"])
        name = student["Name"]
        score_sums[name] = total_score

    favorite_student = data_frame[0]

    for student in data_frame[1:]:
        if score_sums[student["Name"]] > score_sums[favorite_student["Name"]]:
            favorite_student = student

    return favorite_student["Name"]


def addStudent(data_frame):
    name = input("What's the student's name? ")
    age = int(input("Their age: "))
    scores_input = input("Provide their scores, separated by spaces: ")
    scores = [int(score) for score in scores_input.split()]

    new_student = {"Name": name, "Age": age, "Scores": scores}

    data_frame.append(new_student)

    return data_frame


def removeStudent(data_frame):
    remove_me = input("Please give me a name to remove from the student list: ")

    found = False

    for student in data_frame:
        if student["Name"] == remove_me:
            data_frame.remove(student)
            print(f"{remove_me} was removed.")
            found = True

    if not found:
        print("That student does not exist.")

    return None


def getCommon(a_frame, another_frame):
    common_students = set()

    for student in a_frame:
        for another_student in another_frame:
            if student["Name"] == another_student["Name"]:
                common_students.add(student["Name"])
    return common_students


# Thought process: I figured by subtracting the consecutive scores then we can tell if it's negative then their score has increased
# Second thoughts, idk if the improvement would count as consistent but like improvement is improvement
def findImprovement(data_frame):
    improved_names = []

    for student in data_frame:
        scores = student["Scores"]
        has_improved = True

        for i in range(len(scores) - 1):
            if scores[i] > scores[i + 1]:
                has_improved = False
                break

        if has_improved:
            improved_names.append(student["Name"])

    improved_students = tuple(improved_names)
    return improved_students


def main():
    data_frame = [
        {"Name": "Goku", "Age": 37, "Scores": (99, 99, 99)},
        {"Name": "Vegita", "Age": 48, "Scores": (10, 20, 9000)},
        {"Name": "Yugi", "Age": 18, "Scores": (78, 69, 42)},
        {"Name": "Nami", "Age": 20, "Scores": (49, 79, 99)},
        {"Name": "Luffy", "Age": 19, "Scores": (40, 30, 10)},
    ]

    another_data_frame = [
        {"Name": "Naruto", "Age": 17, "Scores": (95, 88, 75)},
        {"Name": "Gon", "Age": 12, "Scores": (90, 85, 78)},
        {"Name": "Lelouch", "Age": 18, "Scores": (98, 94, 92)},
        {"Name": "Sakura", "Age": 16, "Scores": (80, 85, 88)},
        {"Name": "Ichigo", "Age": 16, "Scores": (88, 90, 86)},
    ]
    while True:
        print("\nOptions:")
        print("1. Calculate Average Scores")
        print("2. Find Youngest Student")
        print("3. Find Student with Highest Total Score")
        print("4. Add a Student")
        print("5. Remove a Student")
        print("6. Find Common Students")
        print("7. Find Students with Improved Scores")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print(getAverage(data_frame))
        elif choice == "2":
            print(getYougest(data_frame))
        elif choice == "3":
            print(getHighest(data_frame))
        elif choice == "4":
            addStudent(data_frame)
        elif choice == "5":
            removeStudent(data_frame)
        elif choice == "6":
            print(getCommon(data_frame, another_data_frame))
        elif choice == "7":
            print(findImprovement(data_frame))
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-8).")


main()
