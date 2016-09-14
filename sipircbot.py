# --coding-- utf-8

import socket

irc_host = "irc.freenode.net"
irc_port = 6667
irc_chan = "#linuxba"#,#tuna

bot_name = "mekubot"
usr_name = "meku_bot"
ral_name = "MekuTeleBot"

irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_sock.connect((irc_host, irc_port))


irc_sock.send(("NICK " + bot_name + "\r\n").encode())
irc_sock.send(("USER " + bot_name + " " + bot_name + " " + usr_name + " :" + ral_name + "\r\n").encode())
irc_sock.send(("JOIN " + irc_chan + "\r\n").encode())

while True:
	data = irc_sock.makefile(encoding='utf-8')
	for line in data:
		if(line.startswith("PING")):
			irc_sock.send(line.replace("PING", "PONG").encode())
		else:
			print(line.encode('utf-8').decode())
