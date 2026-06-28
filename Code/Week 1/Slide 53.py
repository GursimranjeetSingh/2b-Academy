def ask_question(question, correct_answer):
    """Ask a question and return 1 if correct, 0 if wrong."""
    answer = input(question + " ").strip().lower()

    if answer == correct_answer.lower():
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Answer: {correct_answer}")
        return 0

def display_result(score, total):
    percent = (score / total) * 100

    print(f"\nYour Score: {score}/{total} ({percent:.1f}%)")

    if percent >= 80:
        print("🏆 Excellent!")
    elif percent >= 50:
        print("👍 Good effort!")
    else:
        print("📚 Keep studying!")

# Run the quiz
score = 0
score += ask_question("Capital of India?", "New Delhi")
score += ask_question("2 ** 8 = ?", "256")
score += ask_question("Python is interpreted? (yes/no)", "yes")

display_result(score, 3)