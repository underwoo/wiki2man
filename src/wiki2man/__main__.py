from .wikipage import WikiPage
import sys

def main():
    # Items that will eventually reside in a config file, or to be included via
    # CLI options
    API_URL = 'https://gaeadocs.rdhpcs.noaa.gov/wiki/api.php' # API URL
    login_name = 'bot_username' # MediaWiki bot username
    login_passwd = 'bot_password' # MediaWiki bot password
    man_page_name = 'man_page' # Filename of man page to output
    man_section = "7" # Section number for output man page
    wiki_title = 'Wiki Title' # Title of Wiki page    API_URL = 'https://gaeadocs.rdhpcs.noaa.gov/wiki/api.php'

    wiki = WikiPage(API_URL, login_name, login_passwd, wiki_title)
    man = wiki.convert2man(man_page_name, man_section)

    try:
        with open('.'.join([man_page_name, man_section]), "wb") as f:
            f.write(man)
    except Exception as err:
        print(err, file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
