import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Get the API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide concise answers."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_user_input():
    file_name = input("Enter the name of the file: ")
    column_name = input("Enter the name of the column: ")
    number_of_rows = input("Enter the number of rows: ")

def main():
    print("Hello, welcome to the CSV Generator!")
    get_user_input()

if __name__ == "__main__":
    main()