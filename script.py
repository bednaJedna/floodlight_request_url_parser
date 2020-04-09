import argparse
from pprint import PrettyPrinter as pp
from typing import Any, Dict, List, Text, Tuple
from urllib.parse import unquote_plus


def parse(
    string: Text, basepath_sep=";", payload_params_sep=";", params_vals_sep="="
) -> Dict[str, str]:
    """Parses provided request URL string into dictionary so humans can read it.
    
    Arguments:
        string {Text} -- request URL
    
    Keyword Arguments:
        basepath_sep {str} -- separator of basepath and payload (default: {";"})
        payload_params_sep {str} -- separator of payload parameters (default: {";"})
        params_vals_sep {str} -- separator of parameter and it's value (default: {"="})
    
    Returns:
        Dict[str, str] -- parsed request URL 
    """
    output: Dict[str, str] = {}
    string_parts: Tuple[str, str, str] = unquote_plus(string).partition(basepath_sep)
    pairs: List[str] = string_parts[2].split(sep=payload_params_sep)
    output["basepath"] = string_parts[0]

    for pair in pairs:
        temp: List[str] = pair.split(sep=params_vals_sep, maxsplit=1)
        output[temp[0]] = temp[1]

    return output


def pretty_print(dict_: Dict[str, str]) -> None:
    """Pretty prints the provided dictionary in the console.

    PrettyPrinter is used for this. Sort_dicts is turned off.
    
    Arguments:
        dict_ {Dict[str, str]} -- dictionary to be pretty printed
    """
    p: Any = pp(indent=2, sort_dicts=False)
    print("\nParsed request URL:\n")
    p.pprint((dict_))


def args() -> Any:
    """Parser of console inputs.
    
    Returns:
        Any -- parsed inputs.
    """
    parser: Any = argparse.ArgumentParser(
        description="Parses and prints foodlight request URL for human use"
    )
    subparsers: Any = parser.add_subparsers()

    parser_fl: Any = subparsers.add_parser(
        "parse_fl", help="Enter floodlight string to be parsed."
    )
    parser_fl.add_argument(
        "fl_string",
        action="store",
        type=str,
        help="Insert Floodlight request URL to parse.",
    )
    parser_ga: Any = subparsers.add_parser(
        "parse_ga", help="Enter GA string to be parsed."
    )
    parser_ga.add_argument(
        "ga_string", action="store", type=str, help="Insert GA request URL to parse.",
    )
    return parser.parse_args()


def main() -> None:
    """Main function.
    """
    arg: Any = args()

    if hasattr(arg, "fl_string"):
        pretty_print(parse(arg.fl_string))

    if hasattr(arg, "ga_string"):
        pretty_print(parse(arg.ga_string, basepath_sep="?", payload_params_sep="&"))


if __name__ == "__main__":
    main()
