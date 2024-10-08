from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def format_diff(diff, formatter):
    """Checks the file format for compliance with the formats available
    in the utility and runs the format set for this file format."""
    if formatter == "stylish":
        return format_stylish(diff)
    if formatter == "json":
        return format_json(diff)
    if formatter == "plain":
        return format_plain(diff)
