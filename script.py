import argparse
from pprint import PrettyPrinter as pp
from typing import Any, Dict, List, Text, Tuple
from urllib.parse import unquote_plus


def parse(
    string: Text, basepath_sep=";", payload_params_sep=";", params_vals_sep="="
) -> Dict[str, str]:

    output: Dict[str, str] = {}
    string_parts: Tuple[str, str, str] = unquote_plus(string).partition(basepath_sep)
    pairs: List[str] = string_parts[2].split(sep=payload_params_sep)
    output["basepath"] = string_parts[0]

    for pair in pairs:
        temp: List[str] = pair.split(sep=params_vals_sep, maxsplit=1)
        output[temp[0]] = temp[1]

    return output


def pretty_print(dict_: Dict[str, str]) -> None:
    p: Any = pp(indent=2, sort_dicts=False)
    print("\nParsed request URL:\n")
    p.pprint((dict_))


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
    pretty_print(parse(arg.string))


if __name__ == "__main__":
    main()
