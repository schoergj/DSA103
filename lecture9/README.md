# Lecture 5: Version Control, Package Management and Code Quality

## Background: Essential Concepts

### What is `uv`?
`uv` is a modern Python package manager that serves as an alternative to pip. It allows you to install packages and handles the following tasks:
- Installing Python packages from PyPI and other sources
- Managing virtual environments for project isolation
- Managing Python versions and project configurations

`uv` uses the same package ecosystem as pip but implements these operations with a focus on speed and reliability.

### What is `ruff`?
A linter is a tool that analyzes your code to identify potential issues, style violations, and areas for improvement without actually running the code. Linting is important because it helps:
- Catch bugs and errors early in development
- Ensure consistent code style across a project
- Improve code readability and maintainability

`ruff` is a Python linter and formatter that checks your code for:
- Potential bugs and logical errors
- Code complexity and maintainability issues
- Import organization and formatting

By using a linter like `ruff`, you can catch many issues before your code is even run, leading to more reliable code.

### What are GitHub Actions?
GitHub Actions is a continuous integration and continuous deployment (CI/CD) platform that allows you to automate workflows directly in your GitHub repository. When specific events occur (like pushing code or creating a pull request), GitHub Actions can automatically:

**Run automated tests**: Execute your test suite to ensure new changes don't break existing functionality
**Check code quality**: Run linters like ruff to enforce coding standards
**Perform security scans**: Check for vulnerabilities in dependencies

For research, GitHub Actions provides several key benefits:
- **Reproducibility**: Every code change is tested in a clean, consistent environment
- **Collaboration**: Team members can see test results before merging code
- **Quality assurance**: Automated checks prevent broken code from entering the main branch

---

## Exercise 1: Repository Setup and Basic Functionality

### Goals
- Fork and clone a repository
- Set up a Python environment with uv
- Explore the structure of the code
- Run basic functionality tests

### Prerequisites

- Git installed on your system
- GitHub account created
- uv installed:
    - Linux/Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh`
    - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`


### Instructions

#### Step 1: Fork the Repository
1. Navigate to the course repository: `https://github.com/schoergj/DSA103`
2. Click "Fork" in the top-right corner
3. Create a fork in your GitHub account

#### Step 2: Clone Your Fork

##### Mac/Linux
```bash
# Replace [your-username] with your actual GitHub username
git clone https://github.com/[your-username]/DSA103.git
cd python-chemistry-intro
```


#### Step 3: Explore the Repository Structure
Examine the following files and directories. Read the function defined in `chemistry_tools.py` and make sure you understand what it does.
```
python-chemistry-intro/
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Lockfile for reproducible installs
├── README.md               # Project documentation
├── src/
│   └── dsa103/    # Main package directory
│       ├── __init__.py
│       └── chemistry_tools.py
├── tests/                  # Test files
│   └── test_molecular_weight.py
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions configuration
```

#### Step 4: Set Up the Environment
```bash
# Create and activate a virtual environment with uv
uv venv

# Activate the environment (Linux/Mac)
source .venv/bin/activate
# Or on Windows
# .venv\Scripts\activate

# Install the package in development mode
uv pip install -e .
```

#### Step 5: Explore Basic Functionality
Place  the following Python code into `scripts/explore_formula.py` to use the installed package:

```python
# Test molecular formula calculation
from dsa103.chemistry_tools import calculate_molecular_formula

# Calculate molecular formula of water (Smiles: O)
formula_water = calculate_molecular_formula("O")
print(f"Molecular formula of water: {formula_water}")

# Calculate molecular formula of caffeine (Smiles: CN1C=NC2=C1C(=O)N(C(=O)N2C)C)
formula_caffeine = calculate_molecular_formula("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
print(f"Molecular formula of caffeine: {formula_caffeine}")
```

#### Step 6: Tests
We've now covered how the package is structured and how we can use functions that have been defined in it. However, to ensure that when changes have been made to the code it still retains the intended functionality we define tests. Check how they are defined in `tests/test_molecular_formula.py`

```bash
# Run all tests
uv run pytest tests/

# Run with verbose output
uv run pytest tests/ -v
```

#### Step 7: Code Quality
Similarly we can also check the quality of the code by running `ruff`:
```bash
# Run ruff linting
uv run ruff check .

# Automatically fix found issues
uv run ruff check --fix .
```

### Questions
1. What information does `pyproject.toml` contain?
2. How does the `uv.lock` file ensure reproducibility?

---

## Exercise 2: Branches and Merging

### Goals
- Create and work with Git branches
- Make changes to code
- Use pull requests for code review

### Instructions

#### Step 1: Create a new Branch
```bash
# Create and switch to a new branch
git checkout -b add-molecular-weight-calculation

# Verify you're on the new branch
git branch
```

#### Step 2: Add a new function
We now want to modify the file `chemistry_tools.py` to add a new function to calculate the molecular weight of molecules:

```python

def calculate_molecular_weight(molecule: str) -> float:

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.") 
    
    return rdMolDescriptors.CalcExactMolWt(mol)
```

#### Step 3: Ensuring Code Quality and Tests
With this we have added a new function to `chemistry_tools.py`. Before you commit the code we need to ensure two things: 
    1. Does the code work? 
    2. Does it match the code standards that we have defined?

For the first add a test case for the new function to `tests/test_chemistry_tools.py` and then ensure that all issues raised by `ruff` are corrected.


#### Step 4: Commit Changes
We are now ready to commit the changes and upload them to github. A good way to name your is to follow the convention detailed [here](https://www.conventionalcommits.org/en/v1.0.0/).

```bash
# List all changes
git status

# Add all relevant changes
git add <path to file>
# or add all changes with:
#git add .

# Double check that all relevant changes have been committed
git status

# Commit with descriptive message
git commit -m "feat: Added function molecular weight calculator and tests for this function."

# Push to GitHub
git push
```

#### Step 5: Create a Pull Request
1. Go to your Repository on GitHub and open "Pull Requests"
2. Click "New Pull Request" and specify that you want to merge "add-molecular-weight-calculation" into "main"
3. Write a descriptive title and description
4. Click "Create pull request"

Now you have created a pull request. Ensure that all tests are passing and if not fix the issues. 

#### Step 7: Reviewing Pull Requests

Before we can merge the pull request it is best practise to have somebody review your code to ensure that there are no issues that you missed. This becomes especially important when you are working with multiple people on a project to ensure that your team mates know what changes have been made and also to ensure that the changes that you made are compatible with the code that they wrote. In a best case scenario such incompatabilities would be cought by the tests. To have someone else review your code follow these steps:

1. Team up with another student from the course. You're going to be reviewing each others code.
2. On you Github Repo navigate to "Settings" then "Collaborators and Teams". From here you can give another person access to your repo.
3. Once the other student has access to your repo, go back to your pull request and on the top right request them to review your pull request.

Do this for each others repositories and review the code. If you find no issues with the code you can accept it otherwise you can request changes. Once the pull request has been accepted it can be merged.