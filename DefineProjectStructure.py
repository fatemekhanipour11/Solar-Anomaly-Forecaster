import os
from pathlib import Path

# --- Define Project Structure ---
# Primary directories
DIRECTORIES = [
    "data",
    "notebooks",
    "results"
]

# Main file names and default content
FILES = {
    "README.md": "# Project Title\n\nA brief description of the project.",
    "requirements.txt": "# List of project dependencies (e.g., pandas, numpy, jupyter)"
}
# ----------------------------

def create_project_structure(base_path="."):
    """
    Creates the necessary project folders and files.

    :param base_path: The base path where the structure is created (default: current directory).
    """
    print("Starting project structure creation...")
    
    # 1. Create directories
    for dir_name in DIRECTORIES:
        path = Path(base_path) / dir_name
        # The exist_ok=True flag prevents an error if the directory already exists
        os.makedirs(path, exist_ok=True)
        print(f"✅ Directory '{dir_name}/' created.")
        
    # 2. Create files with default content
    for file_name, content in FILES.items():
        path = Path(base_path) / file_name
        try:
            # Open file in write mode ('w') with UTF-8 encoding
            with open(path, "w", encoding="utf-8") as f:
                f.write(content.strip())
            print(f"✅ File '{file_name}' created.")
        except Exception as e:
            print(f"❌ Error creating file '{file_name}': {e}")

    print("\nProject structure successfully created.")
    print("\nFinal structure:")
    print("├── data/")
    print("├── notebooks/")
    print("├── results/")
    print("├── README.md")
    print("└── requirements.txt")

# --- Execute the function ---
if __name__ == "__main__":
    create_project_structure()