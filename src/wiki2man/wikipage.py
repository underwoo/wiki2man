import subprocess
import sys
from .connect import Connect

class WikiPage:
    def __init__(self, wiki_url, wiki_username, wiki_password, page_title):
        self.conn = Connect(wiki_url, wiki_username, wiki_password)
        wikipage = self.conn.get_wiki_page(page_title)
        self.wikitext = wikipage['wikitext']
        self.revid = wikipage['revid']
        self.title = wikipage['title']
        self.pageid = wikipage['pageid']
        self.date = wikipage['date']


    def convert2man(self, manpage_name, man_section):
        pandoc_cmd = [
            "pandoc",
            "-s",
            "-f", "mediawiki",
            "-t", "man",
            "-M", f"title={manpage_name}",
            "-M", f"header={self.title}",
            "-M", f"section={man_section}",
            "-M", "footer=User Documentation",
            "-M", f"date={self.date:%B %d, %Y}",
        ]
        sb_ret =  subprocess.run(pandoc_cmd,
                                 input=self.wikitext,
                                 capture_output=True)
        if sb_ret.returncode != 0:
            print(f"Error converting {self.title} from {self.conn.url}",
                  file=sys.stderr)
            print(sb_ret.stderr)
            return None
        else:
            return sb_ret.stdout
