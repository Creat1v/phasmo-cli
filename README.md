# Introduction

A small project to use while playing Phasmophobia for easier ghost type findings.

## Install

Clone this repo. This was done using Python 3.9.

## Usage

Available arguments:

```list
EMF
Finger
Freeze
Writing
Box
Orb
```

Execute main.py

```python
usage: main.py [-h] [evi1] [evi2] [evi3]

Shows ghost type depending on given evidences

positional arguments:
  evi1        1. Evidence
  evi2        2. Evidence
  evi3        3. Evidence

optional arguments:
  -h, --help  show this help message and exit
```

## Example

Either pass arguments or walk through the interactive walkthrough.

### Passing arguments

```python
[~]$ python main.py EMF Writing Orb
-----------
Possible evidences: ['EMF', 'Finger', 'Freeze', 'Writing', 'Box', 'Orb']
1st Evidence: EMF
Banshee - ['EMF', 'Finger', 'Freeze']
Jinn - ['EMF', 'Box', 'Orb']
Oni - ['EMF', 'Writing', 'Box']
Phantom - ['EMF', 'Orb', 'Freeze']
Revenant - ['EMF', 'Writing', 'Finger']
Shade - ['EMF', 'Writing', 'Orb']
-----------
2nd Evidence: Writing
Oni - ['EMF', 'Writing', 'Box']
Revenant - ['EMF', 'Writing', 'Finger']
Shade - ['EMF', 'Writing', 'Orb']
-----------
3rd Evidence: Orb
Shade - ['EMF', 'Writing', 'Orb']
```

### Interactive walkthrough

```python
[~]$ python main.py
-----------
Possible evidences: ['EMF', 'Finger', 'Freeze', 'Writing', 'Box', 'Orb']
Enter 1. evidence:
EMF
Banshee - ['EMF', 'Finger', 'Freeze']
Jinn - ['EMF', 'Box', 'Orb']
Oni - ['EMF', 'Writing', 'Box']
Phantom - ['EMF', 'Orb', 'Freeze']
Revenant - ['EMF', 'Writing', 'Finger']
Shade - ['EMF', 'Writing', 'Orb']
-----------
Enter 2. evidence:
Writing
Oni - ['EMF', 'Writing', 'Box']
Revenant - ['EMF', 'Writing', 'Finger']
Shade - ['EMF', 'Writing', 'Orb']
-----------
Enter 3. evidence:
Orb
```
