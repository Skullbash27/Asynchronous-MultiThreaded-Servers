import argparse#activates command line calling

def command_line(description):
    parser=argparse.ArgumentParser(description=description)
    parser.add_argument('host',help='IP or hostname')
    parser.add_argument('-p',metavar='port',type=int,default=2500,help='TCP port (default 2500)')#Sets the default port number to 2500
    args=parser.parse_args()
    address=(args.host, args.p)
    return address
