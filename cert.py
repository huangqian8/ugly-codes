# -*- coding:utf-8 -*-

import os

# SSL files
ca_bundle = os.getcwd() + "\\ca_bundle.crt"
certificate = os.getcwd() + "\\certificate.crt"
private = os.getcwd() + "\\private.key"

# make dir
synology = os.getcwd() + "\\synology"
erx = os.getcwd() + "\\erx"
os.mkdir(synology)
os.mkdir(erx)

# New files
synology_cert = synology + "\\cert.pem"
synology_privkey = synology + "\\privkey.pem"
erx_server = erx + "\\server.pem"
erx_ca = erx + "\\ca.pem"

# Read & Write files
with open(ca_bundle) as f1:
    ca = f1.read()

with open(certificate) as f2:
    ce = f2.read()

with open(private) as f3:
    pr = f3.read()

with open(synology_cert, "w") as f4:
    f4.write(ca)
    f4.write("\n")
    f4.write(ce)

with open (synology_privkey, "w") as f5:
    f5.write(pr)

with open(erx_server, "w") as f6:
    f6.write(pr)
    f6.write("\n")
    f6.write(ce)

with open(erx_ca, "w") as f7:
    f7.write(ca)