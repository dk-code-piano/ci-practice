import json
import sys

from combo_parser import parse_line

for line in sys.stdin:
    record = parse_line(line)
    if record:
        print(json.dumps(record))