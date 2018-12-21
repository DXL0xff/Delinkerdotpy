## Delinkerdotpy
# Primary link traversal proxification tool to subvert malicious URL's

delinker.py was written in Python3 and developed inside of a Unix environment, the following script should also work on Windows, and Linux platforms, this tool can also be ported to android and used directly with [Termux](https://termux.com/) under a properly configured environment

It should be noted that delinker.py was created to subvert the tracking-urls commonly deployed by malicious actors across the internet, delinker.py will:

1. Mask client information such as:
   1. Public IPv4 address
   1. Country of Origin
   1. ISP (Internet Service Provider)
   1
1. Route the HTTP request to the target URL via python-requests through a public proxy server
   1. All traffic that goes to the target URL will be transferred to the proxy server (simplified below)
   1. TCP traffic from the HTTP request will be sent from the random proxy server <server_ip:port>
1. Prevent any malicous occurences on the client machine

**Usage:** > `python3 delinker.py -t <target_link> -r <request_count>`

Python modules that are required:

* [lxml](https://lxml.de/)
* [requests](https://packages.debian.org/search?keywords=python3-requests)

**How to Download:**
`pip3 install lxml requests`
or
`apt-get install python-lxml python3-requests`

*TOR can be used with delinker.py! The support for TOR will be available in a later update (This tool won't work through proxychains)*

**All proxy descriptors are directly pulled from [https://free-proxy-list.net/](https://free-proxy-list.net/)**
