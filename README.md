# Delinkerdotpy
**Primary link traversal proxification tool to subvert malicious URL's**

**PREFACE: _This tool can be used to send spoofed HTTP requests to a target server, use responsibly the developers do not assume any liability for the misuse of this tool_**

[delinker.py](https://github.com/DXL0xff/Delinkerdotpy/blob/master/delinker.py) was written in Python3 and developed on a Unix environment, the following script should also work on Windows, and Linux platforms, this tool can also be ported to android and used directly with [Termux](https://termux.com/) under a properly configured environment

It should be noted that [delinker.py](https://github.com/DXL0xff/Delinkerdotpy/blob/master/delinker.py) was created to subvert the tracking-urls commonly deployed by malicious actors across the internet, delinker.py will:

1. Mask client information such as:
   1. _Public IPv4 address_
   1. _Country of Origin_
   1. _ISP (Internet Service Provider)_
1. Route the HTTP request to the target URL via python-requests through a public proxy server
   1. _All traffic that goes to the target URL will be transferred to the proxy server (simplified below)_
   1. _TCP traffic from the HTTP request will be sent from the random proxy server <server_ip:port>_
1. Prevent any malicous occurences on the client machine

**Installation & Usage:**
1. `git clone https://github.com/DXL0xff/Delinkerdotpy.git`
1. `cd Delinkerdotpy`
1. `python3 delinker.py -t <target_link> -r <request_count>`

Python modules that are required:

* [lxml](https://lxml.de/)
* [requests](https://packages.debian.org/search?keywords=python3-requests)

**How to Download:**
`pip3 install lxml requests`
or
`apt-get install python3-lxml python3-requests`

** How to verify that this tool works?**
1. Create a link shortener with [https://grabify.link](https://grabify.link)
1. Copy the created link
1. Issue `python3 delinker.py -t <grabify_link> -r <request_count>` _You can set the <request_count> to 10_
1. Wait for the local process to finish
1. Reload https://grabify.link/<temp_extension>, and verify the request's with the HTTP information sent from delinker.py

*TOR can be used with delinker.py! The support for TOR will be available in a later update (This tool won't work through proxychains)*

**All proxy descriptors are directly pulled from [https://free-proxy-list.net/](https://free-proxy-list.net/)**
