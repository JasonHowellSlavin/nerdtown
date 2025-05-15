

# Django 5.1 Setup with Python 3.12, pyenv, and Poetry

This guide walks you through setting up a Django 5.1 project using Python 3.12, managed with pyenv and Poetry.

## Prerequisites

* macOS or Linux (Windows users can adapt steps accordingly)
* Homebrew (for macOS) or appropriate package manager for Linux

## Step 1: Install pyenv

```bash
brew install pyenv
```



Add the following to your `~/.zshrc` (or `~/.bashrc`):

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```



Then, reload your shell:

```bash
source ~/.zshrc
```



Verify installation:

```bash
pyenv --version
```



## Step 2: Install Python 3.12

```bash
pyenv install 3.12
```



Set Python 3.12 as the local version for your project:

```bash
pyenv local 3.12
```



Confirm the active Python version:

```bash
python --version
```



## Step 3: Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python
```



Verify installation:

```bash
poetry --version
```



## Step 4: Initialize Your Django Project


Set the local Python version:

```bash
pyenv local 3.12
```



Initialize a new Poetry project:

```bash
poetry init --no-interaction
```



Install Django 5.1:

```bash
poetry add Django@5.1
```



Poetry will create a virtual environment and install Django along with its dependencies.

## Step 5: Create a New Django Project

```bash
poetry run django-admin startproject my_project .
```



Apply migrations:

```bash
poetry run python manage.py migrate
```



Run the development server:

```bash
poetry run python manage.py runserver
```



Your Django 5.1 project is now running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

For a more detailed explanation, refer to the original article by Jilles Soeters: 


[1]: https://jilles.me/setting-up-django-5-1-using-python-3-12-with-pyenv-and-poetry/?utm_source=chatgpt.com "Setting up Django 5.1 using Python 3.12 with pyenv and Poetry"

