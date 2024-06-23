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
    """
    Get the AI response for the given column names and number of rows.

    A function to get the AI response for the given column names and number of rows.

    :param column_names: The string, names of the columns in the CSV file
    :param number_of_rows: The int, number of rows to generate
    :precondition: column_names must be a string
    :precondition: number_of_rows must be an integer
    :postcondition: Get the AI response in CSV format
    :return: The AI response in CSV format
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide responses in CSV format when tables are requested."},
                {"role": "user", "content": " Please provide the response in CSV format." + "Inside the CSV format file, I want to have these columns. I want you to generate the data related to the column name. Use the appropriate data type: " + column_names + "I want you to generate " + str(number_of_rows) + " rows of data."} 
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Function to save the response as a CSV file
def save_as_csv(response: str, filename="output.csv"):
    """
    Save the response as a CSV file.

    A function to save the response as a CSV file.

    :param response: The string, the response to save
    :param filename: The string, the filename to save the response as (default: output.csv)
    :precondition: response must be a string
    :precondition: filename must be a string
    :postcondition: Save the response as a CSV file
    :return: None
    """
    # Ensure the filename ends with .csv
    if not filename.lower().endswith('.csv'):
        filename += '.csv'

    try:
        lines = response.strip().split('\n')
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in lines:
                writer.writerow(line.split(','))
        print(f"CSV file saved as {filename}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")


def main():
    """
    Drive the program.
    """
    print("Hello, welcome to the CSV Generator!")

    column_names = str(input("Enter the names of the column (comma-separated): "))

    while True:
        number_of_rows = input("Enter the number of rows: ")
        if number_of_rows.isdigit():
            number_of_rows = int(number_of_rows)
            break
        else:
            print("Invalid input. Please enter a valid number.")

    try:
        response = get_ai_response(column_names, number_of_rows)
    except RuntimeError as e:
        print(e)
        return
        
    print("\nAI Response:")
    print(response)

    while True:
        save_choice = input("\nDo you want to save this as a CSV file? (y/n): ").lower()
        if save_choice in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
    if save_choice.lower() == 'y':
        filename = str(input("Enter the filename (default: output.csv): ")) or "output.csv"
        save_as_csv(response, filename)


if __name__ == "__main__":
    main()