import zipfile
import zlib
corpus_file = "/usr/share/dict/words"

with zipfile.ZipFile( "demo.zip", "r" ) as archive:
    first = archive.infolist()[0]
    print( "Reading", first.filename )
    with open( corpus_file ) as corpus:
        for line in corpus:
            word= line.strip().encode("ASCII")
            try:
                with archive.open(first, 'r', pwd=word) as member:
                    text= member.read()
                print( "Password", word )
                print( text )
                break
            except (RuntimeError, zlib.error, zipfile.BadZipFile):
                pass
