#!/usr/bin/env python

from requests import head
from requests.exceptions import RequestException

from http_server_availabilty import parse_args


def main():
    args = parse_args()
    try:
        reply = head(f"{args.server}:{args.port}")
        print(f"HTTP response code {str(reply.status_code)}")
    except RequestException as e:
        print(f"Can not establish a connection with {args.server}: {str(e)}")


if __name__ == "__main__":
    main()
