# Git Commit Logger

This script generates a text file for each Git repository found in a specified directory. The text file lists the commit messages for each author, classified by type (create, update, bugfix, other).

## Requirements

- Python 3.x
- GitPython
- Arrow

## Usage

1. Clone this repository to your local machine
2. Install the necessary requirements by running `pip install -r requirements.txt`
3. Navigate to the `git-commit-logger` directory
4. Modify the `path` variable in `main.py` to point to the directory containing your Git repositories
5. Run the script using `python main.py`
6. The output text files will be generated in the `output` directory

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
