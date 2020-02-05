

# Installing pipenv and jupyter notebook

From https://github.com/pypa/pipenv,

```
brew install pipenv
cd sandbox
pipenv install
pipenv install notebook --dev
pipenv shell
jupyter notebook
```

# For VSCode:

Select the interpreter, command->shift-p (select the interpreter from pipenv, I had to click on terminal for it to actually load)

```
pipenv install pylint --dev
pipenv install pycodestyle --dev
pipenv install autopep8 --dev
```

I had to restart VSCode
