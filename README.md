# Assigner

A simple application that reads a list of names and choices, and randomly assigns choices to the names.

This application was created as a quick way to carry out a draw for the 2018 World Cup.

## Usage

```
usage: assigner.py [-h] [-s SEED] names choices
```

To run the application, two filenames must be provided—the first should contain the names, and the second should contain the choices to be assigned.

Positional arguments | Description
-------------------- | -----------
`names`              | filename containing names of individuals in the draw
`choices`            | filename containing choices

Optionally, you can set the seed with `-s` or `--seed` in order to obtain reproducible results.

Optional arguments   | Description
-------------------- | -----------
`-s, --seed`         | random seed for reproducible results (default: None)

This application handles cases where the number of choices is greater than the number of names, and where the number of names is greater than the number of choices.

Some simplistic examples are shown below.

## Examples

### Equal number of names and choices

In this scenario, each name in `names.txt` is assigned exactly one (1) choice from `choices.txt`.

```
$ cat names.txt
alice
bob
eve

$ cat choices.txt
rock
paper
scissors

$ python3 assigner.py names.txt choices.txt
{'alice': ['paper'], 'bob': ['scissors'], 'eve': ['rock']}
```

### More choices than names

In this scenario, *at least one (1)* name in `names.txt` will have two (2) or more choices from `choices.txt`.

In the example below, `bob` is assigned both `paper` and `scissors`.

```
$ cat names.txt
alice
bob
eve

$ cat choices.txt
rock
paper
scissors
lizard

$ python3 assigner.py names.txt choices.txt
{'alice': ['rock'], 'bob': ['paper', 'scissors'], 'eve': ['lizard']}
```

### More names than choices

In this scenario, *at least one (1)* name in `names.txt` will not be assigned any choice from `choices.txt`.

In the example below, `alice` is not assigned any choices.

```
$ cat names.txt
alice
bob
eve
mike

$ cat choices.txt
rock
paper
scissors

$ python3 assigner.py names.txt choices.txt
There are more names (4) than choices (3)!
The following names were not assigned choices: {'alice'}
{'bob': ['paper'], 'eve': ['scissors'], 'mike': ['rock']}
```
