import ollama

print("\nFree AI Study Guide for C Programming")
print("------------------------------------")

topic = input("Enter a C programming topic: ").strip()

if not topic:
    print("No topic entered. Exiting.")
    exit()

prompt = f"""
Create a beginner-friendly C programming study guide on the topic: "{topic}".

Include:
- Brief overview
- Key concepts
- Simple C syntax examples
- Common mistakes
- 3 practice questions
- Key takeaways

Keep it concise and easy to understand.
"""

print(f"\nGenerating study guide for: {topic}\n")

try:
    stream = ollama.generate(
        model="llama3",
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        print(chunk["response"], end="", flush=True)

    print("\n\nDone.")

except Exception as e:
    print("\nError:", e)
