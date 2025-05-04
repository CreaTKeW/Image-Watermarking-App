# Image Watermarking App (Markapp)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge&logo=python&logoColor=white)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-success?style=for-the-badge&logo=bootstrap&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-blue?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

A desktop application built with Python using Tkinter and ttkbootstrap, designed for adding text watermarks to images. Users can select an image, input watermark text, customize its appearance (color, font, position), and save the resulting image.

## ✨ Features

* **Graphical User Interface (GUI):** Clean and modern interface powered by `ttkbootstrap`.
* **Image Loading:** Supports popular image formats (JPG, PNG, BMP, GIF).
* **Image Preview:** Displays the selected image directly within the application window.
* **Text Watermark Addition:** Input field for custom watermark text.
* **Result Saving:** Ability to save the watermarked image in various formats (PNG, JPG, BMP, GIF).
* **Settings Window:**
    * **Text Color Selection:** Uses an interactive `ColorChooserDialog`.
    * **Text Font Selection:** Choose from available system fonts, including size and style, via `FontDialog`.
    * **Watermark Position Selection:** Dropdown menu with placement options (e.g., `bottom-left`, `top-left`, `center`, `bottom-right`, `top-right`).
    * **Settings Preview:** Instant preview of the selected color and font within the settings window.
* **Error Handling:** User feedback for issues (e.g., file not found, invalid format, missing watermark text) via `Messagebox` dialogs.

## 🛠️ Technologies & Libraries

### Backend / Logic
* **Python 3:** The core programming language.
* **Pillow (PIL Fork):** Library for image manipulation (opening, drawing text, saving).
* **Matplotlib (Font Manager):** Used specifically to find and manage system fonts for Pillow.

### Frontend / GUI
* **Tkinter:** Python's standard library for creating GUIs.
* **ttkbootstrap:** An extension for Tkinter/ttk adding modern themes and widgets (buttons, labels, entry fields, dialogs).

### Tools & Concepts
* **Git & GitHub:** Version control.
* **Object-Oriented Programming (OOP):** Application structure based on classes (`App`, `Logic`, `Settings`).
* **Event Handling:** Responding to user actions (button clicks, menu selections).
* **Virtual Environments:** Dependency management (`venv`).
* **Modular Structure:** Code separated into logic (`logic.py`) and user interface (`main_window.py`, `settings_window.py`) modules.

## 📂 Project Structure

The project directory structure is as follows:

```plaintext
Image-Watermarking-App/
├── resources/
│   └── example.jpg
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   └── logic.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── settings_window.py
│   ├── __init__.py
│   └── main.py
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.x
* pip (Python package installer)
* Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CreaTKeW/Image-Watermarking-App.git
    cd Image-Watermarking-App
    ```
2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
3.  **Install dependencies:**
    Install necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python src/main.py
    ```
    The application should start, displaying the main window.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author
**Damian Ptaszkiewicz**

* **GitHub:** [@CreaTKeW](https://github.com/CreaTKeW)
