#!/usr/bin/python env
import socket
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="IP of your listening machine")
    parser.add_option("-p", "--port", dest="port", help="Port you want to listen on")
    options, arguments = parser.parse_args()

    if not options.ip:
        parser.error("[-] Please specify an IP of your listening machine, use -i [IP]/--ip [IP] to do so or use "
                     "--help for more info")

    if not options.port:
        parser.error("[-] Please specify a PORT on which you want to listen, use -p [PORT]/--port [PORT] to do so or "
                     "use --help for more info")

    return options


options = get_args()

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((options.ip, int(options.port)))
listener.listen(0)
print("[+] Listening for connections on port " + options.port)
listener.accept()
print("[+] Received a connection from IP " + options.ip)
