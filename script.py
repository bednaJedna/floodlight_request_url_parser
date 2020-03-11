import argparse
from pprint import PrettyPrinter as pp
from typing import Any, Dict, List, Text
from urllib.parse import unquote_plus


def parse(string: Text) -> Dict[str, str]:
    output: Dict[str, str] = {}
    pairs: List[str] = unquote_plus(string).split(sep=";")
    output["basepath"] = pairs[0]

    for pair in pairs[1:]:
        temp: List[str] = pair.split(sep="=", maxsplit=1)
        output[temp[0]] = temp[1]

    return output


def pretty_print(dict_: Dict[str, str]) -> None:
    p: Any = pp(indent=2, sort_dicts=False)
    print("\nParsed request URL:\n")
    p.pprint(dict_)


def args() -> Any:
    parser: Any = argparse.ArgumentParser(
        description="Parses and prints foodlight request URL for human use"
    )
    parser.add_argument(
        "string",
        action="store",
        type=str,
        help="Insert Floodlight request URL to parse.",
    )
    return parser.parse_args()


def main() -> None:
    arg: Any = args()

    if arg.string:
        pretty_print(parse(arg.string))


if __name__ == "__main__":
    main()
