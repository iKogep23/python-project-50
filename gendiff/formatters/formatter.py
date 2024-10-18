from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def formatter_foo(formatter):
    """Checks the file format for compliance with the formats available
    in the utility and runs the format set for this file format."""
    match formatter:
        case "stylish":
            return format_stylish
        case "json":
            return format_json
        case "plain":
            return format_plain
        case _:
            raise ValueError(f"Unsupported file format: {formatter}")
