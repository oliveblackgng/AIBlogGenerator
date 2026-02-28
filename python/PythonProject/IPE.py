"""
AI-Assisted Study Guide for 'Basics of C Programming'
-----------------------------------------------------

This program uses the OpenAI API to generate study materials dynamically.
Users can enter a C programming topic and get:
    1. A summary explanation
    2. A sample C code example
    3. A short quiz for self-practice

Developed by: [Your Name]
For: [Course or Assignment Name]
"""

# Import the OpenAI library
from openai import OpenAI

# Initialize the OpenAI client
# Replace 'YOUR_API_KEY' with your actual key from platform.openai.com
client = OpenAI(api_key="YOUR_API_KEY")

def generate_content(prompt):
    """
    Sends a prompt to the AI model and returns its response.
    """
    response = client.chat.completions.create(
        model="gpt-4-turbo",       # can also use 'gpt-3.5-turbo' if limited
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,           # controls creativity level
    )
    return response.choices[0].message.content


def ai_study_guide(topic):
    """
    Generates structured study material for a given C topic.
    """
    print("\n=========================================================")
    print(f"📘 AI Study Guide: {topic.title()}")
    print("=========================================================\n")

    # Generate topic explanation
    summary_prompt = f"Explain the concept of '{topic}' in C programming in simple, beginner-friendly terms."
    summary = generate_content(summary_prompt)
    print("🧠 TOPIC SUMMARY:\n", summary, "\n")

    # Generate example code
    code_prompt = f"Provide a simple C program example demonstrating '{topic}', with line-by-line explanation."
    code_example = generate_content(code_prompt)
    print("💻 CODE EXAMPLE:\n", code_example, "\n")

    # Generate quiz
    quiz_prompt = f"Create 5 multiple-choice quiz questions on '{topic}' in C programming with correct answers."
    quiz = generate_content(quiz_prompt)
    print("📝 PRACTICE QUIZ:\n", quiz)
    print("\n=========================================================\n")


# -------- Main Program -------- #
print("🎓 Welcome to the AI-Assisted C Programming Study Guide 🎓")
print("---------------------------------------------------------")
print("Type a C topic (e.g., loops, arrays, pointers, functions)")
print("Type 'exit' to quit.\n")

while True:
    topic = input("Enter topic: ").strip().lower()
    if topic == "exit":
        print("\nThank you for using the AI Study Guide. Keep learning C! 🚀")
        break
    elif topic == "":
        print("Please enter a valid topic name.\n")
    else:
        ai_study_guide(topic)
