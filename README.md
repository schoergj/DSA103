# DSA103

Repository for the course DSA103 Advanced Chemical Data Science. All course material will be shared here, wheras OLAT will only be used for all course-related communication.

Instructors and persons responsible for the course: Prof. Meredith C. Schuman, Dr. Johannes Schörgenhumer

Teaching assistant: Dimitrios Xynos


## Course content

- Computational thinking review
- Python review
- Version control
- Data acquisition
- Data wrangling
- Data analysis and interpretation
- Current topics in chemical data science

## Prerequisites
Throughout this course, you will need your personal computer, please bring it to every session. You will use several tools, which have to be installed on your PC (if you have done the DSA101, you might already know some of them). We highly recommend to have your computer set up appropriately before the first lecture:

1) Git/Github: Make sure you have Git installed and a GitHub account. **This repo uses Git LFS. Run `git lfs install` after cloning.**
2) We will use the package manager uv and its virtual environment (https://docs.astral.sh/uv/). Follow the instructions on the website to install uv. In some cases (on Windows), you will get an error about an ExecutionPolicy. In order to remedy that, open a Power Shell Terminal as administrator and `Set-ExecutionPolicy -ExecutionPolicy Unrestriced -Scope LocalMachine`. Find out more here: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.5.
3) IDE: For running code and Jupyter notebooks and for facilitating version control, we will be using an IDE. All demonstration will be done in Visual Studio Code, but other development environments, such as Pycharm, work as well. Whatever IDE you are using, make sure that you keep it and its extensions (e.g. for Jupyter) up to date and that you are familiar with the working environment.

If anything else is going to be required, you will be notified in due course.

## How to work with this repository
The initial steps:
1) Fork the repository using the Fork button on GitHub.
2) Clone your fork.
3) Create a virtual environment, by running `uv venv` in the terminal (in the IDE).
4) Activate the virtual environment via the terminal (e.g. on Windows: `.venv\Scripts\activate`).
5) Run the command `uv sync` to synchronize the environment with the provided lock file. Any missing dependencies will be thereby installed.
6) Select the Python interpreter from the DSA103 environment (in VSC: click in the Search bar, hit Ctrl+P, then type "Python: Select Interpreter" - or use the button in the lower right corner of the window). Likewise you can can set the Interpreter for Jupyter notebooks.

This repository will be updated regularly throughout the course. Make sure to keep up to date by synchronizing your fork via GitHub. Should the virtual environment change as well (new dependencies to install), we will notify you - you can update the environment running the `uv sync` command again after starting the environment.

**Important: In order to avoid merge conflicts, always copy any files you work on (notebooks, scripts, data, etc.) to the user folder provided in each lecture folder, or create a new file under a different name.** This way you can always accept incoming changes, without altering your personal file versions. 

We do recommend to practice the git workflow throughout this course and to commit to your fork after significant changes. **If there are any problems with your IDE, uv, git or your repo, that prevent you from using the environment as intended, please notify us via mail immediately and don't wait until the next Q&A session.** 

## Authors
This repository was created and is maintained by Merry Schuman and Johannes Schörgenhumer.

## Acknowledgements

Many thanks to Marvin Alberts and Alexander Steppke for writing exercises and helping with solutions!

## License
CC BY-NC-SA 4.0 

You are free to share and adapt, as long as attribution to the authors is appropriately given, the material is not used for any commercial purposes and any material built on the content of the DSA104 repository is shared under the same license.

Full license information are found here: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en
