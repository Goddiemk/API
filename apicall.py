import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('type', help='Type of currency')
parser.add_argument('date', help='Date (dd-mm-yyyy)')
args = parser.parse_args()

r = requests.get('http://forex.cbm.gov.mm/api/history/%s' % args.date)
data = json.loads(r.content)
print(data['rates'][args.type])
