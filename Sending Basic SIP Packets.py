from scapy.all import *
import hashlib
import random

send(IPv6(dst="destination ip") / UDP(dport=any desired port, sport=5060) / Raw(load="REGISTER sip:sip2sip.info SIP/2.0"))
