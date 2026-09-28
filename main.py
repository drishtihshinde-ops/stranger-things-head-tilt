from questions import questions
from logic import add_score, get_result
from head_tilt import get_head_tilt

print("🎬 Welcome to 'Which Stranger Things Character Are You?' Game!")
print("Tilt your head LEFT or RIGHT to select options.\n")

for q in questions:
    print("\n" + q["question"])
    print("Left Option:", q["left"]["text"])
    print("Right Option:", q["right"]["text"])

    choice = get_head_tilt()
    if choice == "L":
        add_score(q["left"]["character"])
        print("You chose:", q["left"]["text"])
    elif choice == "R":
        add_score(q["right"]["character"])
        print("You chose:", q["right"]["text"])
    else:
        print("Skipped question.")

result = get_result()
print("\n🎉 Your Stranger Things character is:", result)
