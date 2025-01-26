# Password Generator
![image](https://github.com/user-attachments/assets/15ec2556-daad-4cc0-8c1a-f6c098e510a7)


A **Password Generator** application with an elegant design created using **Tkinter**, **Photoshop** and **Figma**. This tool generates secure passwords in three difficulty levels: Easy, Normal, and Hard. Users can also save generated passwords to an Excel file for safekeeping. 

---

## Features

- **Password Difficulty Levels**:
  - **Easy**: Short and simple passwords (6 characters).
  - **Normal**: Moderate complexity (12 characters).
  - **Hard**: Highly secure passwords (24 characters with special characters).

- **Functional Buttons**:
  - **Generate**: Creates a password of the selected difficulty level.
  - **Copy**: Copies the generated password to the clipboard.
  - **Clear**: Clears the current password.
  - **Save**: Saves the password along with a description to an Excel file (`passwords.xlsx`).

- **Beautiful GUI**:
  - Designed using `tkinter`, with custom visuals crafted in Photoshop and Figma.

---

## Setup Instructions

Follow these steps to set up and run the Password Generator on your system:

### 1. Prerequisites
- **Python 3.6 or higher**: Ensure Python is installed on your machine.
- **Pip**: Python's package manager, included by default with Python 3.6+.

### 2. Clone or Download the Project
Download the project files or clone the repository:
```bash
git clone <repository-url>
**
**### 3. Install Dependencies***
Navigate to the project directory and install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
**4. Prepare Assets**
Ensure the assets folder is present in the project directory. This folder should contain:

new.png (Background image for the GUI).
Button images (e.g., button_1.png, etc.).
5. Run the Program
Run the Python script:

bash
Copy
Edit
python password_generator.py
6. Additional Configuration for Linux Users
If you are using Linux and tkinter is not installed, install it using the following command:

bash
Copy
Edit
sudo apt-get install python3-tk
How to Use
Choose a Password Type:

Click the button corresponding to the desired password type: Easy, Normal, or Hard.
Generate Password:

Press the Generate button to display the generated password in the text field.
Copy Password:

Use the Copy button to copy the password to your clipboard.
Save Password:

Press the Save button. A new window will open asking for a description of the password (e.g., "Email account"). After entering the description, the password will be saved to an Excel file (passwords.xlsx).
Clear the Field:

Use the Clear button to reset the text field and clear the generated password.
File Structure
php
Copy
Edit
Password Generator/
│
├── password_generator.py      # Main application file
├── requirements.txt           # Dependencies for the project
├── passwords.xlsx             # Excel file to store saved passwords
├── assets/                    # Assets folder for GUI elements
│   ├── new.png                # Background image
│   ├── button_1.png           # Button images
│   └── ...                    # Other assets
Dependencies
The program requires the following Python libraries:

pathlib (Standard Library)
tkinter (Standard Library; may require installation on some systems)
random (Standard Library)
openpyxl (For working with Excel files)
To install the required third-party library, run:

bash
Copy
Edit
pip install openpyxl
Example Output
Generated Passwords:

Easy: XasqRt
Normal: 3aqB@dF6pQtz
Hard: oL1@!mQ$xRp&TN7g*F8T#bZ
Saved to Excel:

perl
Copy
Edit
| Description       | Password        |
|-------------------|-----------------|
| Email account     | XasqRt          |
| Social Media      | 3aqB@dF6pQtz    |
| Bank Account      | oL1@!mQ$xRp&TN7g*F8T#bZ |
