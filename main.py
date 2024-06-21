import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_user_input():
    file_name = input("Enter the name of the file: ")
    column_name = input("Enter the name of the column: ")
    number_of_rows = input("Enter the number of rows: ")

def main():
    print("Hello, welcome to the CSV Generator!")
    get_user_input()

if __name__ == "__main__":
    main()