#!/usr/bin/env python

import pyshark
import re
import base64

SRC_IP = "192.168.196.133"

cap = pyshark.FileCapture("kiminonawa.pcapng")

message = ""
for packet in cap:
    if packet.highest_layer == "DNS":
        print ("Source IP: " + packet.ip.src)
        ip = packet.ip.src
        query_name = packet.dns.qry_name
        if query_name and ip == SRC_IP:
            m = re.search(r"(.*)\.evil\.corp", query_name)

            if m:
                encoded_str = m.group(1)

                print ("\tExtracted: " + encoded_str)
                decoded_str = base64.b64decode(encoded_str)
                decoded_str = decoded_str.decode("UTF-8")
                message += decoded_str

print ("[+] Message: " + message)
