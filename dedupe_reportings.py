import argparse
import json


def unique_by_keys(items, keys):
    seen = set()
    unique = []
    for item in items:
        value = tuple(item[k] for k in keys)
        if value not in seen:
            seen.add(value)
            unique.append(item)
    return unique


def remove_key_if_none(item, key):
    if key in item and item[key] is None:
        del item[key]
    return item


def dump_json(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


KEY_ATTR_ID = "attrId"
KEY_CLUSTER = "cluster"
KEY_CONFIGURED_REPORTINGS = "configuredReportings"
KEY_ENDPOINTS = "endpoints"
KEY_MANUFACTURER_CODE = "manufacturerCode"


def dedupe_reportings(line):
    obj = json.loads(line)
    for endpoint in obj.get(KEY_ENDPOINTS, {}).values():
        reportings = endpoint.get(KEY_CONFIGURED_REPORTINGS)
        if reportings:
            unique_reportings = unique_by_keys(
                reportings,
                [KEY_ATTR_ID, KEY_CLUSTER],
            )
            endpoint[KEY_CONFIGURED_REPORTINGS] = [
                remove_key_if_none(r, KEY_MANUFACTURER_CODE)
                for r in unique_reportings
            ]
    return dump_json(obj)


def join_lines(lines, newline=True):
    return "\n".join(lines) + ("\n" if newline else "")


def main(input_file, output_file=None):
    with open(input_file, "r") as db:
        lines = [dedupe_reportings(line) for line in db]

    if output_file:
        with open(output_file, "w") as db:
            db.write(join_lines(lines))
    else:
        print(join_lines(lines, False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Remove repeated "reportings" from a Zigbee2MQTT database.'
    )
    parser.add_argument("input", help="Input database file")
    parser.add_argument("-o", "--output", help="Output database path")
    args = parser.parse_args()
    main(args.input, args.output)
