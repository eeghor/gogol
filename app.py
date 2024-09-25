import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_openai_response(prompt):
    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # or whichever engine you prefer
            prompt=prompt,
            max_tokens=100,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt for OpenAI: ")
    result = get_openai_response(user_prompt)
    print(f"OpenAI Response: {result}")
