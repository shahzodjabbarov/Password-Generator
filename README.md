# Password Generator
![image](https://github.com/user-attachments/assets/15ec2556-daad-4cc0-8c1a-f6c098e510a7)
A **Password Generator** application with an elegant design created using **Photoshop** and **Figma**. This tool generates secure passwords in three difficulty levels: Easy, Normal, and Hard. Users can also save generated passwords to an Excel file for safekeeping.

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
  - **Save**: Saves the password with a description to an Excel file (`passwords.xlsx`).

- **Beautiful GUI**:
  - Designed using `tkinter`, with custom visuals created in Photoshop and Figma.

---

## Setup Instructions

Follow these steps to set up and run the Password Generator:

### 1. Prerequisites
- **Python 3.6 or higher**: Ensure Python is installed.
- **pip**: Python’s package manager.

### 2. Clone or Download the Project
Download or clone the repository:

```bash
git clone <repository-url>
```

### 3. Install Dependencies
Navigate to the project directory and install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Program
Run the Python script:

```bash
python password_generator.py
```

### 5. Linux Users
If `tkinter` isn't installed, use:

```bash
sudo apt-get install python3-tk
```

---

## How to Use

1. **Choose a Password Type**: Click Easy, Normal, or Hard.
2. **Generate Password**: Press Generate to create a password.
3. **Copy Password**: Click Copy to copy it to your clipboard.
4. **Save Password**: Press Save and enter a description to store in `passwords.xlsx`.
5. **Clear**: Press Clear to reset the text field.

---

## File Structure

```
Password Generator/
├── main.py      # Main application file
├── requirements.txt           # Project dependencies
├── passwords.xlsx             # Excel file for saved passwords
├── assets/                    # GUI assets
│   ├── new.png                # Background image
│   ├── button_1.png           # Button images
│   └── ...                    # Other assets
```

---

## Dependencies

- `pathlib`: Standard Library
- `tkinter`: Standard Library
- `random`: Standard Library
- `openpyxl`: For working with Excel files

Install openpyxl using:

```bash
pip install openpyxl
```

---

## Example Output

- **Easy**: `XasqRt`
- **Normal**: `3aqB@dF6pQtz`
- **Hard**: `oL1@!mQ$xRp&TN7g*F8T#bZ`

---

