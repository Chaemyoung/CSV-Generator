import os
import csv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Get the API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


# Get the ai reponse in csv file format
def get_ai_response(column_names: str, number_of_rows: int):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide responses in CSV format when tables are requested."},
                {"role": "user", "content": " Please provide the response in CSV format." + "Inside the CSV format file, I want to have these columns. I want you to generate the data related to the column name. Use the appropriate data type: " + column_names + "I want you to generate " + number_of_rows + " rows of data."} 
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to save the response as a CSV file
def save_as_csv(response: str, filename="output.csv"):
    lines = response.strip().split('\n')
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            writer.writerow(line.split(','))
    print(f"CSV file saved as {filename}")


def main():
    print("Hello, welcome to the CSV Generator!")
    column_names = str(input("Enter the names of the column: "))
    number_of_rows = int(input("Enter the number of rows as an integer: "))    
    response = get_ai_response(column_names, number_of_rows)
    print("\nAI Response:")
    print(response)

    save_choice = input("\nDo you want to save this as a CSV file? (y/n): ")
    if save_choice.lower() == 'y':
        filename = str(input("Enter the filename (default: output.csv): ")) or "output.csv"
        save_as_csv(response, filename)

if __name__ == "__main__":
    main()