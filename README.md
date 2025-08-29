# Student Registration System
This is a simple Python-based application that uses SQLite to manage student registrations.
It allows users to add student names and emails into a local database.

## Features
- Register new students with name and email
- Stores data securely using SQLite
- Prevents duplicate email entries
- Easy to extend with more features (e.g., search, update, delete)

## Technologies Used
- Python 3
- SQLite
- Visual Studio Code (recommended editor)
- Git for version control
## Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/studentregistrations.git
   cd studentregistrations
2. Make sure Python is installed:
   bash
   python3 --version
3. Run the script:
   bash
   python3 main.py

How It Works
- The script connects to a local SQLite database called `students.db`.
- It creates a table called `students` if it doesn't exist.
- You can register a student by calling the function `register_student(name, email)`.
*Example*
python
register_student("Amina", "amina@example.com")

Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!
License
This project is licensed under the MIT License.

