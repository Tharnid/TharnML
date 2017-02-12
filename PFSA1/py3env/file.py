# with open("message1.txt", "w") as target:
#     print( "Message to HQ", file=target )
#     print( "Device Size 10 31/32", file=target )

# various reads
# with open("message1.txt", "r") as source:
#     text= source.read()
# print( text )
#
# with open("message1.txt", "r") as source:
#     for line in source:
#         print(line)
#
# with open("message1.txt", "r") as source:
#     for line in source:
#         junk1, keyword, size= line.partition("Size")
#         if keyword != '':
#             print( size )

message= """Message to Field Agent Garbo
Proceed to Rendezvous FM16uu62
Authorization to Pay $250 USD
"""

with open("message2.txt", "w") as target:
    target.write( message )

amount= None
location= None
with open("message2.txt", "r") as source:
    for line in source:
        clean= line.lower().rstrip()
        junk, pay, pay_data= clean.partition("pay")
        junk, meet, meet_data= clean.partition("rendezvous")
        if pay != '':
            amount= pay_data
        elif meet != '':
            location= meet_data
        else:
            pass # ignore this line
print( "Budget", amount, "Meet", location )
