import ollama

def generate_blog(transcript):

    prompt = f"""
    Convert the following YouTube transcript into a structured blog article.

    Transcript:
    {transcript}

    Blog structure:
    - Title
    - Introduction
    - Key Points
    - Conclusion
    """

    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    return response["response"]