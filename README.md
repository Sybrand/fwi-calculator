# FWI

A quick FWI prototype using "Updated source code for calculating fire danger indices in the canadian forest fire weather index system" : Y. Wang, K.R. Anderson and R.M. Suddaby. As provided by Natural Resources Canada.

This reproduction is a modified copy of an official work that is published by Natural Resources Canada (NRCan) and the reproduction has not been produced in affiliation with, or with the endorsement of, NRCan.

# Running

## Calculator

If you run:
```
python calculator.py
```
it will calculate the FWI for a single day

## Percentile

If you run:
```
python percentile.py
```
it will consume data.txt, and create fwioutput.txt. It will also calculate the 90th percentile of data provided.

## Notebook

You can also load up the FWI Calculator jupyter notebook.

```
jupyter notebook
```

# Getting your environment up

## Installing pipenv and jupyter notebook

From https://github.com/pypa/pipenv,

```
brew install pipenv
cd sandbox
pipenv install
pipenv install notebook --dev
pipenv shell
jupyter notebook
```

## For VSCode:

Select the interpreter, command->shift-p (select the interpreter from pipenv, I had to click on terminal for it to actually load)

```
pipenv install pylint --dev
pipenv install pycodestyle --dev
pipenv install autopep8 --dev
```

I had to restart VSCode
