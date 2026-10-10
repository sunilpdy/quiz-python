import json
import random
import sys


def load_quiz(filename):
    """Load quiz data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        sys.exit(f"Error: '{filename}' not found.")
    except json.JSONDecodeError as e:
        sys.exit(f"Error: invalid JSON in '{filename}': {e}")

    questions = data.get("questions", [])
    if not questions:
        sys.exit("Error: no questions found in the file.")

    for i, q in enumerate(questions, start=1):
        if not all(k in q for k in ("question", "options", "answer")):
            sys.exit(f"Error: question {i} is missing a required field.")
        if not 0 <= q["answer"] < len(q["options"]):
            sys.exit(f"Error: question {i} has an invalid answer index.")

    return data.get("title", "Quiz"), questions


def ask_question(number, total, q):
    """Display one question and return True if answered correctly."""
    print(f"\nQuestion {number}/{total}: {q['question']}")

    # Shuffle options but keep track of the correct one
    indexed = list(enumerate(q["options"]))
    random.shuffle(indexed)

    correct_label = None
    for label, (orig_index, option) in enumerate(indexed, start=1):
        print(f"  {label}. {option}")
        if orig_index == q["answer"]:
            correct_label = label

    while True:
        choice = input("Your answer (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(indexed):
            break
        print(f"Please enter a number between 1 and {len(indexed)}.")

    if int(choice) == correct_label:
        print("✅ Correct!")
        return True

    print(f"❌ Wrong! The correct answer was: {correct_label}. "
          f"{q['options'][q['answer']]}")
    return False


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "questions.json"
    title, questions = load_quiz(filename)

    random.shuffle(questions)

    print("=" * 40)
    print(f"  {title}")
    print("=" * 40)

    score = 0
    for i, q in enumerate(questions, start=1):
        if ask_question(i, len(questions), q):
            score += 1

    percent = score / len(questions) * 100
    print("\n" + "=" * 40)
    print(f"Final score: {score}/{len(questions)} ({percent:.0f}%)")
    print("=" * 40)


if __name__ == "__main__":
    main()
