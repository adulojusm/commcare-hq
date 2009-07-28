#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from datetime import datetime
import json

#directory = r'C:\Source\hq\commcare-hq\django-hq\brac'
#directory = r'C:\Source\hq\commcare-hq\django-hq\pathfinder'
#directory = r'C:\Source\hq\data\brac-chp-jul-24\touse2'
#directory = r'C:\Source\hq\data\brac-chw-jul-24\touse2'
#directory = r'C:\Source\hq\data\brac\CHP\commcare\input'
#directory = r'C:\Source\hq\data\brac\CHW\commcare\input'
directory = r'C:\Source\hq\data\pathfinder\commcare\input'

#domain = "BRAC"
domain = "Pathfinder"
files = os.listdir(directory)
for file in files:
    if "xml" in file:
        filename = (os.path.join(directory,file))
        file = open(filename, "rb")
        dir, short_filename = os.path.split(filename)
        new_dir = os.path.join(dir, "out")
        payload = file.read()
        file.close()
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        new_filename = short_filename.replace(".xml", ".postexport")
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filename)
        headers = { "content-type" : "text/xml", 
                "content-length" : str(len(payload)),
                "time-received" : str(datetime.fromtimestamp(mtime)),
                "original-ip" : "192.168.7.211",
                "domain" : domain
               }
        fout = open(os.path.join(new_dir, new_filename), 'w')
        jsoned = json.dumps(headers)
        fout.write(jsoned)
        fout.write("\n\n")
        fout.write(payload)
        fout.close()
