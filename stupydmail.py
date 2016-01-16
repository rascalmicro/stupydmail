import cmd
import socket
from twisted.internet import reactor

PORT = 5005
ADDRESSES = {'brandon': '172.16.10.107'}

class StupydMail(cmd.Cmd):

    intro = 'Ready to send stupyd-mail'
    prompt = 'Stupyd-mail: '

    def do_send(self, name):
        reactor.callFromThread(on_main_thread, name)

    def do_EOF(self, line):
        return True

def on_main_thread(name):

        MESSAGE = "Whatever"
        try:
            ip = ADDRESSES[name]
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE.encode(), (ip, PORT))
        except KeyError:
            print("Don't know IP address of {0}".format(name))

def heartbeat():
    print "heartbeat"
    #sock.setblocking(0)
    #data, addr = sock.recvfrom(1024)
    #print "received msg: ", data
    reactor.callLater(2.0, heartbeat)

if __name__ == '__main__':
    #sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.bind((IP, PORT))
    reactor.callLater(2.0, heartbeat)
    reactor.callInThread(StupydMail().cmdloop)
    reactor.run()