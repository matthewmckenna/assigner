#!/usr/env/bin python
"""randomly assign choices to names"""
import argparse
from collections import defaultdict
import pprint
import random
from typing import DefaultDict, List


def main(args: argparse.Namespace) -> None:
    """main entry point"""
    # dict mapping from a `name` to a list of `choices`
    d: DefaultDict[str, List[str]] = defaultdict(list)

    # cannot use `if args.seed` because a seed of `0` is valid, but "falsy"!
    if args.seed is not None:
        random.seed(args.seed)

    # creates lists from `names` and possible `choices`
    with open(args.names, 'rt') as f, open(args.choices, 'rt') as f2:
        names = [name.strip() for name in f]
        choices = [choice.strip() for choice in f2]

    # if there are more choices than names, at least one name
    # will have more than one choice
    num_extra_choices = len(choices) - len(names)

    # shuffle the names
    # could also use: random.sample(names, k=len(names))
    random.shuffle(names)

    # shuffle the order of the choices
    # `len(randomised_choices)` will be < `len(choices)` if
    # `len(names)` != `len(choices)`
    # in these cases, it will be `min(len(choices), len(names))`
    randomised_choices = random.sample(choices, k=min(len(choices), len(names)))

    for name, choice in zip(names, randomised_choices):
        d[name].append(choice)

    if len(names) > len(choices):
        names_without_choices = set(names) - d.keys()
        print(f'There are more names ({len(names)}) than choices ({len(choices)})!')
        print(f'The following names were not assigned choices: {names_without_choices}')

    # `remaining_choices` will be an empty set (and therefore "falsy") if
    # `len(names)` == `len(choices)`
    remaining_choices = set(choices) - set(randomised_choices)

    if remaining_choices:
        # `additional_choices` contains names of those who get
        # an additional choice, as num_names > num_choices
        additional_choices = random.sample(names, k=num_extra_choices)

        for name, choice in zip(additional_choices, remaining_choices):
            d[name].append(choice)

    pprint.pprint(dict(d))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='carry out random draws',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('names', help='filename containing names of individuals in the draw')
    parser.add_argument('choices', help='filename containing choices')
    parser.add_argument('-s', '--seed', help='random seed for reproducible results', type=int)
    args = parser.parse_args()
    main(args)
