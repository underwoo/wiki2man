# wiki2man

`wiki2man` will extract wiki text from a MediaWiki Wiki, and create a man page.

## Installation

`wiki2man` can be installed via `pip`:

```
pip install git+https://gitlab.gfdl.noaa.gov/Seth.Underwood/wiki2man
```
## Usage

To convert a wiki page to RST:

```
wiki2man --type rst \
         --url https://gaeadocs.rdhpcs.noaa.gov/wiki/api.php \
         --wiki-page wiki_page_title
         --username User.Name
         --password "P@s5w0rd"
         --title file_name
```

This will convert the wiki page `wiki_page_title`, and write the output
to `file_name.rst`.

To convert a man page:

```
wiki2man --type rst \
         --url https://gaeadocs.rdhpcs.noaa.gov/wiki/api.php \
         --wiki-page wiki_page_title
         --username User.Name
         --password "P@s5w0rd"
         --title file_name
         --section 7
```

This will convert the wiki page `wiki_page_title`, and write the output
to `file_name.7`.

## Known Issues

* The MediaWiki to man conversion does not handle tables correctly
