import json

path = 'data/gov.txt'

result = [json.loads(line) for line in open(path)]

time_zone = [rec['tz'] for rec in result if 'tz' in rec]


