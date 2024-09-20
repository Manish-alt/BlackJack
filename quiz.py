import requests
import json
import html

# API URL
url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"

response = requests.get(url)
score = 0

if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    
    # Extract the 'results' which contains the quiz questions
    questions = data['results']
    
    # Print the questions in a readable format
    print("Trivia Questions:\n")
    
    for i, question in enumerate(questions, 1):
        print(f"Q{i}: {html.unescape(question['question'])}")
        answer = input("Enter True of False: ")
        
        if i == len(questions):
            print(f"\nQuiz has finished. Your Total score is {score}.\n\n")
        else:
            if answer == f"{question['correct_answer']}":
                score += 1
                print("\nAnswer is correct. Next Question\n\n")
            else:
                print("\nAnswer is wrong. Next Question\n\n")
       
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


