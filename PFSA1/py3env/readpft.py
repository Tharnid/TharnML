import sys
import urllib.request

readme= "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/README"
with urllib.request.urlopen( readme ) as response:
    for line in response.readlines():
        print( line.rstrip() )

local= "file:///Users/slott/Documents/Writing/Secret Agent's Python/currency.html"
with urllib.request.urlopen( local ) as response:
    print( response.read() )
