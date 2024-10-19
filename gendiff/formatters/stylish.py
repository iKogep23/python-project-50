import json
from gendiff.data_comparer import NESTED, ADDED, REMOVED, CHANGED, UNCHANGED


INDENT = ' ' * 4
FLAGS = {
    ADDED: '  + ',
    REMOVED: '  - ',
    UNCHANGED: ' ' * 4
}


def get_stringify_value(value):
    """Gets a json representation of the parameter value."""
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def stringify_value(value, depth):
    """Returns a list of strings in json representation
    of the parameter values."""
    if not isinstance(value, dict):
        return get_stringify_value(value)
    string_list = ['{']
    spaces = INDENT * depth
    for key, value_ in value.items():
        if isinstance(value_, dict):
            string = f'{spaces}{INDENT}{key}: ' \
                     f'{stringify_value(value_, depth + 1)}'
            string_list.append(string)
        else:
            string = f'{spaces}{INDENT}{key}: {stringify_value(value_, depth)}'
            string_list.append(string)
    string_list.append(f'{spaces}}}')
    return '\n'.join(string_list)


def stringify_diff(diff, depth):
    """Returns a list of strings in stylish representation
    of the values in variable diff."""
    diff_list = []
    spaces = INDENT * depth
    for key, flags in diff.items():
        type_ = flags.get('type')
        value = flags.get('value')
        if type_ == NESTED:
            result_key = f'{spaces}{INDENT}{key}: ' \
                         f'{{\n{stringify_diff(value, depth + 1)}'
            result_value = f'{spaces}{INDENT}}}'
            diff_list.extend([result_key, result_value])
        elif type_ == CHANGED:
            old_value = value.get('old value')
            new_value = value.get('new value')
            result_key = f'{spaces}{FLAGS[REMOVED]}{key}: ' \
                         f'{stringify_value(old_value, depth + 1)}'
            result_value = f'{spaces}{FLAGS[ADDED]}{key}: ' \
                           f'{stringify_value(new_value, depth + 1)}'
            diff_list.extend([result_key, result_value])
        else:
            result_string = f'{spaces}{FLAGS[type_]}{key}: ' \
                            f'{stringify_value(value, depth + 1)}'
            diff_list.append(result_string)
    return '\n'.join(diff_list)


def format_stylish(diff, depth=0):
    """Conversts a values in variable diff into stylish format."""
    final_list = ['{', stringify_diff(diff, depth), '}']
    return '\n'.join(final_list)
