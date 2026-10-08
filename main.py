# Simple Quiz Game

score = 0

print("===== Welcome to the Quiz =====")
print("Answer the following questions.\n")

# Question 1
answer = input("1. What is the capital of Nepal? ")

if answer.lower() == "kathmandu":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Kathmandu.")

# Question 2
answer = input("\n2. Which language is used to create this quiz? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Python.")

# Question 3
answer = input("\n3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final result
print("\n===== Quiz Finished =====")
print("Your score:", score, "/ 3")

if score == 3:
    print("Excellent! 🎉")
elif score >= 2:
    print("Good job!")
else:
    print("Keep practicing!")
