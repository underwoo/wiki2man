from .wikipage import WikiPage
import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser(prog="wiki2man",
                                     description="Extract wiki text from a MediaWiki Wiki, and create a man page.",
                                     allow_abbrev=False)
    parser.add_argument("--url",
                        help="Wiki API URL")
    parser.add_argument("--username",
                        help="Wiki API username")
    parser.add_argument("--password",
                        help="Wiki API password")
    parser.add_argument("--title",
                        help="Title of man page (e.g. intro_gaea)")
    parser.add_argument("--section",
                        help="Man page section number",
                        type=int,
                        default=7)
    parser.add_argument("--wiki-page",
                        help="Wiki page to extract")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    print(args)
    wiki = WikiPage(args.url,
                    args.username,
                    args.password,
                    args.wiki_page)
    man = wiki.convert2man(args.title, args.section)

    try:
        with open(f"{args.title}.{args.section}", "wb") as f:
            f.write(man)
    except Exception as err:
        print(err, file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
