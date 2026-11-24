import json
import sys

from combo_parser import parse_line

# read and parse every line from standard in
for line in sys.stdin:
    record = parse_line(line)
    if record:
        print(json.dumps(record))