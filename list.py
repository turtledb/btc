#! /usr/bin/env python

import argparse
import fnmatch
from btc import encoder, decoder, client, ordered_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default=None)
    parser.add_argument('-s', '--case-sensitive', default=False, action="store_true")
    args = parser.parse_args()
    l = sorted(client.list_torrents(), key=lambda x: x['name'].lower())
    if args.name:
        def case(x):
            if args.case_sensitive:
                return x
            return x.lower()
        l = filter(lambda x: fnmatch.fnmatch(case(x['name']), case(args.name)), l)

    print(encoder.encode([ordered_dict(d) for d in l]))

if __name__ == '__main__':
    main()
