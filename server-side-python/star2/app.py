from bottle import route, run
import json
import random
@route('/')
def index():
    return "Hello world"


orgs_list = [
    {"is_non_profit": False, "name": 'Fiverr', 'address': 'Israel'},
    {"is_non_profit": False, "name": 'Fanatic', 'address': 'France'},
    {"is_non_profit": False, "name": 'Google', 'address': 'US'}
]


@route('/org')
def get_org():
    org = random.choice(orgs_list)
    org['value'] = random.randint(10000, 100000)
    return json.dumps(org)


def main():
    run(host='localhost', port=7000, debug=True, reload=True)


if __name__ == '__main__':
    main()
