"""
Convert MediaWiki Paages
~~~~~~~~~~~~~~~~~~~~~~~~

Extract the MediaWiki text using the MediaWiki API, and convert to a man page
or ReStructured Text (rst) document.

Basic usage:

    >>> import WikiPage
    >>> wiki = WikiPage(api_url,
                        username,
                        password,
                        wiki_page)
    >>> wiki.convert2rst()

:copyright: (c) 2022, 2023 Seth Underwood.
:license: MIT, see LICENSE.md for more details.
"""

from .wikipage import WikiPage

__all__ = WikiPage
__version__ = "1.0.0"
__author__ = "Seth Underwood"
