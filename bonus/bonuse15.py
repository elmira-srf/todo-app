import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for questions in data:
    print(questions["question_text"])
    for index, a in enumerate(questions["alternatives"]):
        print(index+1, "-", a)
    user_choice = int(input("Enter your answer: "))
    questions["user_choice"] = user_choice

for index, q in enumerate(data):
    if q['user_choice'] == q['correct_answer']:
        score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index+1} {result} - Your answer: {q['user_choice']},"\
              f"Correct answer: {q['correct_answer']}"
    print(message)

print(data)
print(score, "/", len(data))