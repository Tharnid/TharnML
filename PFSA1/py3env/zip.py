import zipfile
with zipfile.ZipFile( "demo.zip", "r" ) as archive:
    archive.printdir()
    first = archive.infolist()[0]
    try:
        with archive.open(first) as member:
            text= member.read()
            print( text )
    except RuntimeError as e:
        print( e )
