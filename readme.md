# CSV Generator

## Description
CSV Generator is a Python-based tool that allows users to generate customized CSV files using AI. By collecting user inputs for column names, data type, increments, the number of rows and file name, the AI generates tables accordingly. Users can then review and download the tables as CSV files. The tool leverages Python and the OpenAI API.

## Features
- **Interactive User Input**: Prompts the user to enter column names, data types, increments, the number of rows and file name for the CSV file.
- **AI-Generated Data**: Uses OpenAI API to generate data based on user-specified column names and number of rows.
- **CSV File Generation**: Saves the generated data as a CSV file based on user confirmation.
- **Error Handling**: Includes robust error handling for invalid inputs and exceptions during data generation and file saving.
- **Logging**: Implements logging for better debugging and error tracking.

## Requirements
- Python 3.1 + 
- OpenAI Python library
- python-dotenv

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Chaemyoung/csv-generator.git
   cd csv-generator
   ```

2. Install the required packages:
   ```
   pip install openai python-dotenv
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage
1. Run the script:
   ```
   python csv_generator.py
   ```

2. Follow the prompts:
- Enter the column names separated by commas.
- Enter the number of rows for the CSV file.
- Confirm whether you want to save the generated data as a CSV file.
- If yes, provide a filename or use the default output.csv.

## Example
```


░█████╗░░██████╗██╗░░░██╗  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔════╝██║░░░██║  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝╚█████╗░╚██╗░██╔╝  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗░╚═══██╗░╚████╔╝░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██████╔╝░░╚██╔╝░░  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═════╝░░░░╚═╝░░░  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

Hello, welcome to the CSV Generator! This tool will help you create a CSV file based on your specified columns and number of rows. Let's get started!

Enter the column names, separated by commas. Include data types - optional, and Identity(starting_num, increment) - optional. (e.g., name(varchar), age(int, IDENTITY(1,1)), email): name(varchar), age(int), occupation(varchar)
Provide some detail explanation of the data to get better results.: This file will be used to store customer data. This csv will be import to SSMS as a customer table.
Enter the number of rows for the CSV file (e.g., 10): 5

AI Response:

name,age,occupation
John Doe,32,Software Engineer
Jane Smith,28,Teacher
Michael Johnson,45,Doctor
Emily Brown,39,Marketing Manager
David Wilson,52,Accountant

Do you want to save this as a CSV file? (y/n): y
Enter the filename (default: output.csv): customer.csv
CSV file saved as customer.csv
```

## Error Handling
- The script includes error handling for invalid inputs and API errors.
- If an error occurs, an appropriate message will be displayed to the user.

## Notes
- This tool uses the OpenAI API, which may incur costs based on your usage.
- Ensure you have sufficient credits in your OpenAI account.
- The quality and relevance of the generated data depend on the AI model's capabilities.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Chaemyoung/csv-generator/issues) if you want to contribute.

## License
[MIT](https://choosealicense.com/licenses/mit/)
