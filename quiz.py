import requests
import json
import html

# API URL
url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"

response = requests.get(url)
score = 0
class Quiz:
    
    def __init__(self):
        self.score = 0
    
    def askQuestion(self, questions):
        # Print the questions in a readable format
        print("Trivia Questions:\n")
    
        for i, question in enumerate(questions, 1):
            print(f"Q{i}: {html.unescape(question['question'])}")
            answer = input("Enter True or False: ").capitalize()  # Capitalize the input to match the correct answer format
        
            if answer == question['correct_answer']:
                self.score += 1
                print("\nAnswer is correct. Next Question\n")
            else:
                print("\nAnswer is wrong. Next Question\n")
        
        print(f"\nQuiz has finished. Your Total score is {self.score}.\n")

    def parseData(self):
        url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
    
            # Extract the 'results' which contains the quiz questions
            questions = data['results']
            self.askQuestion(questions)
        
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            

# Create an instance of the Quiz class and start the quiz
quiz = Quiz()
quiz.parseData()

   
    
    
  
       



