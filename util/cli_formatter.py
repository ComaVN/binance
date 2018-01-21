import json
from prettytable import PrettyTable


def format(value, format):
    return {
        'json': lambda v: json.dumps(v,
            indent=2,
            sort_keys=True,
        ),
        'plain': plain_formatter,
    }[format](value)


def plain_formatter(value):
    # RH: TODO: support more kinds of values
    # value is a list of flat dictionaries, all having the same keys
    table = PrettyTable()
    fields = list(value[0])
    table.field_names = fields
    for row in value:
        table.add_row([row[k] for k in fields])
    return table.get_string()
