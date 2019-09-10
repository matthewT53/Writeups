#!/usr/bin/env python

import pyshark
import re

usb_codes = {
   0x04:"aA", 0x05:"bB", 0x06:"cC", 0x07:"dD", 0x08:"eE", 0x09:"fF",
   0x0A:"gG", 0x0B:"hH", 0x0C:"iI", 0x0D:"jJ", 0x0E:"kK", 0x0F:"lL",
   0x10:"mM", 0x11:"nN", 0x12:"oO", 0x13:"pP", 0x14:"qQ", 0x15:"rR",
   0x16:"sS", 0x17:"tT", 0x18:"uU", 0x19:"vV", 0x1A:"wW", 0x1B:"xX",
   0x1C:"yY", 0x1D:"zZ", 0x1E:"1!", 0x1F:"2@", 0x20:"3#", 0x21:"4$",
   0x22:"5%", 0x23:"6^", 0x24:"7&", 0x25:"8*", 0x26:"9(", 0x27:"0)",
   0x2C:"  ", 0x2D:"-_", 0x2E:"=+", 0x2F:"[{", 0x30:"]}",  0x32:"#~",
   0x33:";:", 0x34:"'\"",  0x36:",<",  0x37:".>", 0x4f:">", 0x50:"<"
}

flag = []

capture = pyshark.FileCapture("monkey.pcapng")

for packet in capture:
    # print (packet.highest_layer)
    if packet.highest_layer == "DATA":
        usb_data = packet.layers[1].usb_capdata
        # print (usb_data)
        data = re.split(r":", usb_data)
        print (data)

        n = len(data)
        if n == 8:
            for i in range(2, 8):
                key = int(data[i], 16)

                if key in usb_codes:
                    value = usb_codes[key]

                    if data[0] == "20" or data[0] == "02":
                        flag.append(value[1])
                    else:
                        flag.append(value[0])
                else:
                    if key == 0x2a:
                        flag.append("[DEL]")

print (''.join(flag))
