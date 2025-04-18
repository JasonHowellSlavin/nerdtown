# Nerdtown Project  

Nerdtown is going to run python for now. We can decide later if we want to add any languages, frameworks, etc. 
But for now we want to keep it as simple as possible. 

## Getting Started
NOTE: Any time an example would have you replace a word with your own word (filepaths, file names, credentials, etc) it will be shown
in angle brackets `<>`. For example, if I ask you to make a file of your own naming, it might be presented like: 
```
Make a file under the new directory:
Home/<directory>/filename
```
Which could look like: `Home/my-directory/my-filename`. 

### First Steps
- Using the terminal in VSCode
- Using the command line, and reading command line docs
- Running our first program

#### Using the terminal in VSCode
The terminal is the command line interface(cli) that allows you to interact with the file system of your computer
and use command words to interface with applications and run programs. From the command line you can do things as 
grandiouse as changing system permissions or as mundane as creating a new file or directory. 

To use the terminal in VSCode, go up to the menu items, select `Terminal` from the dropdown, and select `New Terminal`. 
You should now see a terminal below, with the filepath highlighted. Here is where you will run command line interface(cli) 
commands, like `python3 hello-world.py`. 

### Using the command line, and reading command line docs

[Here are some basic unix commands](https://mally.stanford.edu/~sr/computing/basic-unix.html) that you can reference, but the most important 
ones you will use often are: 
- *cd* - change directory using a specified file path. (cd Repos/nerdtown/files)
- *ls* - list files in the director
- *mkdir* - make a new director: mkdir my-new-directory-name
- *touch* - make a new file: touch my-new-file-name.file-type (games.py)

### Running our first program
You likely already have python installed since you are using a mac. If you do not, [look at this article](https://docs.python.org/3/using/mac.html).

Next, check to see which version of python you have installed by typing the following into the terminal:
`python --version`
You may see a `command not found` error, if so, follow it's direction or install python. 

Next, use the terminal to cd to the following path: 
`<Repo folder name>/nerdtown/main/getting-started`

From there, run the CLI command: `python3 hello-world.py`. Note, your python version may vary, and the command may vary, for example
`python hello-world.py`. 

### Second Steps

#### Using Git
- Online git tutorials
- Basic git commands
- Git workflow

#### Installing pyenv and using pyenv
- Installation
- Documentation 
- When and why