import os
import csv
import logging
import art
from dotenv import load_dotenv
from openai import OpenAI

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"

# Text Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY environment variable not set.")
    exit(1)

# Create an OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize a list to store history of generated tables
generated_tables = []

# Get the AI response in CSV file format
def get_ai_response(column_names: str, number_of_rows: int, user_explanation: str) -> str:
    """
    Get the AI response for the given column names and number of rows.

    A function to get the AI response for the given column names and number of rows.

    :param column_names: The string, names of the columns in the CSV file
    :param number_of_rows: The int, number of rows to generate
    :param user_explanation: The string, detail explanation of data to generate better result
    :precondition: column_names must be a string
    :precondition: number_of_rows must be an integer
    :postcondition: Get the AI response in CSV format
    :return: The AI response in CSV format
    """
    history = "\n".join([f"Table: {table['name']}\nColumns: {', '.join(table['columns'])}\nRows:\n{table['data']}\n" for table in generated_tables])
    try:
        prompt = f"""
        Previously generated tables:
        {history}

        Please provide the response in CSV format. Inside the CSV format file, I want to have these columns with the specified data types and identity properties: {column_names}.
        The text inside the brackets next to the column names indicates the data type and identity properties (starting number, increment), but these are optional.
        If the data types and identity are not given, then choose the appropriate data types and identity.
        Generate the data according to the specified data types and identity properties where applicable.
        This is the detailed explanation of the data that I want you to use as a reference. However, do not rely on this. If it does not make sense, you don't have to listen to it.
        {user_explanation}
        I want you to generate {number_of_rows} rows of data.
        Ensure the data is realistic and appropriate for each column type. This is important. Do not include anything other than CSV formats. No explanations, no notes, no talking. ONLY CSV data.
        """
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a highly intelligent and helpful assistant. When a user requests data in a table(CSV) format, you should provide the response as a well-structured CSV file. Ensure that the CSV format includes appropriate headers and corresponding data rows, accurately reflecting the column names and data types specified by the user. Use the previous tables' data as a reference if provided."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"


def save_as_csv_and_store(response: str, filename="output.csv") -> None:
    """
    Save the response as a CSV file and store the table data.

    :param response: The string, the response to save
    :param filename: The string, the filename to save the response as (default: output.csv)
    :precondition: response must be a string
    :precondition: filename must be a string
    :postcondition: Save the response as a CSV file and store the table data
    :return: None
    """
    # Ensure the filename ends with .csv
    if not filename.lower().endswith('.csv'):
        filename += '.csv'

    try:
        lines = response.strip().split('\n')
        header = lines[0].split(',')
        data = "\n".join(lines[1:])
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows([line.split(',') for line in lines[1:]])
        
        print(f"CSV file saved as {YELLOW}{BOLD}{filename}{RESET}")
        
        # Store the generated table data
        generated_tables.append({
            "name": filename,
            "columns": header,
            "data": data
        })
    except Exception as e:
        logging.error(f"{RED}Error saving file: {str(e)}{RESET}")

def main() -> None:
    """
    Drive the program.
    """
    print(GREEN + art.program_title + RESET)
    print(f"\n{GREEN}Hello, welcome to the CSV Generator! This tool will help you create a CSV file based on your specified columns and number of rows. Let's get started!{RESET}")

    while True:
        # Display previously generated tables
        if generated_tables:
            print(f"\n{CYAN}{BOLD}Previously generated tables:{RESET}")
            for table in generated_tables:
                print(f"{YELLOW}{table['name']}{RESET}: {', '.join(table['columns'])}")
        
        # Get the column names from the user
        column_names = input(f"Enter the {BLUE}{BOLD}column names, separated by commas{RESET}. Include {BLUE}{BOLD}data types - optional{RESET}, and {BLUE}{BOLD}Identity(starting_num, increment) - optional.{RESET} {CYAN}(e.g., name(varchar), age(int, IDENTITY(1,1)), email){RESET}: ").strip()
        if not column_names:
            logging.error(f"{RED}Column names cannot be empty.{RESET}")
            return
        
        # Get the user explanation from the user
        user_explanation = input(f"Provide {BLUE}{BOLD}some detailed explanation {RESET}of the data to get better results: ").strip()
        
        # Get the number of rows from the user
        while True:
            number_of_rows = input(f"Enter {BLUE}{BOLD}the number of rows{RESET} for the CSV file (e.g., 10): ")
            # Check if the input is a valid number
            if number_of_rows.isdigit():
                number_of_rows = int(number_of_rows)
                break
            else:
                print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

        try:
            response = get_ai_response(column_names, number_of_rows, user_explanation)
        except RuntimeError as e:
            print(e)
            return
            
        print(f"{MAGENTA}\nAI Response:\n{RESET}")
        print(response)

        # Ask the user if they want to save the response as a CSV file
        while True:
            save_choice = input(f"{CYAN}{BOLD}\nDo you want to save this as a CSV file? (y/n): {RESET}").lower()
            if save_choice in ['y', 'n']:
                break
            else:
                print(f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}")

        # Save the response as a CSV file and store the table data
        if save_choice.lower() == 'y':
            # Get the filename from the user
            filename = str(input(f"Enter the {BLUE}{BOLD}filename{RESET} (default: output.csv): ")).strip() or "output.csv"
            save_as_csv_and_store(response, filename)

        # Ask the user if they want to continue
        continue_choice = input(f"{CYAN}{BOLD}\nDo you want to generate another CSV file? (y/n): {RESET}").lower()
        if continue_choice == 'n':
            print(f"{GREEN}Thank you for using the CSV Generator. Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()
