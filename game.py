import time

def run_quiz():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) define", "B) func", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "Which movie features a character named Jack Dawson?",
            "options": ["A) Titanic", "B) Inception", "C) The Revenant", "D) Avatar"],
            "answer": "A"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        }
    ]
    
    score = 0
    
    print("\n🎉 Welcome to the Quiz Game! 🎉\n")
    time.sleep(1)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("\nYour answer (A, B, C, D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

        time.sleep(1)
    
    print(f"\n🏆 You scored {score} out of {len(questions)}! 🏆")

def main():
    while True:
        run_quiz()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! 🎉")
            break

if __name__ == "__main__":
    main()
