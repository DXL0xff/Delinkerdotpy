import os
import sys
import ssl
import time
import random
import argparse
import requests
import urllib.request
from itertools import cycle
from lxml.html import fromstring


def get_proxies():
    url = 'https://free-proxy-list.net/'
    
    response = requests.get(url)
    parser = fromstring(response.text)
    
    proxies = set()
    # grab a list of 35 proxies
    for i in parser.xpath('//tbody/tr')[:101]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    return proxies

request_limit = 0 # set unlimited request count
proxy_list = []
agent_list = []

def delink_target():
    global proxy_list
    global agent_list
    global request_limit

    proxy = get_proxies()

    os.system(f'touch {os.getcwd()}/ret_proxies.txt')

    # write proxy descriptors from get_proxies() to file
    for p in proxy:
        with open (f'{os.getcwd()}/ret_proxies.txt', 'a') as pfile:
            pfile.write(p+'\n')
            pfile.close()    
    
    # load proxies from ret_proxies.txt
    print('**DELINKER** <[ INFO ]> Loading proxy descriptors...')
    time.sleep(3)

    with open(f'{os.getcwd()}/ret_proxies.txt', 'r') as prox_desc:
        for proxy_string in prox_desc:
            proxy_list.append(proxy_string.strip('\n'))

    # now that the proxies are loaded, load the user agents
    print('**DELINKER** <[ INFO ]> Loading User-Agents from linker_agents...')
    time.sleep(3) # user needs to be aware of agent loading
    
    with open(f'{os.getcwd()}/linker_agents.txt', 'r') as afile:
        for agent_string in afile:
            agent_list.append(agent_string.strip('\n'))

    # set the default requests to 5 max 500 for script (might take longer)
    if int(args.requests) > 0:
        try:
            for i in range(0, int(args.requests) + 1):
                print('**DELINKER** <[ INFO ] Starting HTTP request relay...')
                URL = args.target
                # random user agent is set
                PROXY_POOL = random.choice(proxy_list)
                SET_PROXY = {'http:': f'http://{PROXY_POOL}', 'https': f'https://{PROXY_POOL}'}

                user_agent = random.choice(agent_list)
                headers = {'Connection' : 'close',
                        'User-Agent' : user_agent}

                print(f'**DELINKER** <[ INFO ]> Transmitting HTTP relay information\nUser-Agent: {user_agent} -> {PROXY_POOL}')
                try:
                    req = requests.get(URL, proxies=SET_PROXY, params=None, headers=headers)

                except Exception as p_err:
                    print(f'**DELINKER** <[ \033[0;33mWARNING\033[0;m ]> Failed to create a connection with {PROXY_POOL}')
                    # print(f'RETURNING P_ERR -> {p_err}')
                    delink_target()

                else:
                    if request_limit == int(args.requests):
                        print("**DELINKER** <[ \033[0;32mFINISHED\033[0;m ]> All HTTP relays finished. Exiting...")
                        
                        target_path1 = f'{os.getcwd()}/ret_proxies.txt'
                        os.system(f'rm {target_path1}')

                        if os.path.isfile(target_path1) == 1:
                            print(f'**DELINKER** <[ \033[0;33mWARNING\033[0;m ]> Failed to remove {target_path1} from the file system')
                            sys.exit(-1)
                        else:
                            sys.exit(1)
                    else:
                        request_limit += 1

        except KeyboardInterrupt:
            print('\n**DELINKER** <[ \033[0;32mFINISHED\033[0;m ]> All HTTP relays finished. Exiting...')

            target_path2 = f'{os.getcwd()}/ret_proxies.txt'
            os.system(f'rm {target_path2}')

            if os.path.isfile(target_path2) == 1:
                print(f'**DELINKER** <[ \033[0;33mWARNING\033[0;m ]> Failed to remove {target_path2} from the file system')
                sys.exit(-1)
            else:
                sys.exit(1)
    
    elif int(args.requests) == 0:
        while request_limit == 0:
            try:
                print('**DELINKER** <[ INFO ] Starting HTTP request relay...')
                URL = args.target
                # random user agent is set
                PROXY_POOL = random.choice(proxy_list)
                SET_PROXY = {'http:': f'http://{PROXY_POOL}', 'https': f'https://{PROXY_POOL}'}

                user_agent = random.choice(agent_list)
                headers = {'Connection' : 'close',
                        'User-Agent' : user_agent}

                print(f'**DELINKER** <[ INFO ]> Transmitting HTTP relay information\nUser-Agent: {user_agent} -> {PROXY_POOL}')
                try:
                    req = requests.get(URL, proxies=SET_PROXY, params=None, headers=headers)

                except Exception as p_err:
                    print(f'**DELINKER** <[ WARNING ]> Failed to create a connection with {PROXY_POOL}')
                    # print(f'RETURNING P_ERR -> {p_err}')
                    delink_target()

            except KeyboardInterrupt:
                print('\n**DELINKER** <[ \033[0;32mFINISHED\033[0;m ]> All HTTP relays finished. Exiting...')

                target_path2 = f'{os.getcwd()}/ret_proxies.txt'
                os.system(f'rm {target_path2}')

                if os.path.isfile(target_path2) == 1:
                    print(f'**DELINKER** <[ \033[0;33mWARNING\033[0;m ]> Failed to remove {target_path2} from the file system')
                    sys.exit(-1)
                else:
                    sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='delinker', description='reverse URL traversal tool')

    parser.add_argument('-t', '--target', help='the target URL to traverse through a proxy', required=True)
    parser.add_argument('-r', '--requests', help='the x amount of requests to send to the URL to traverse', required=True)
    parser.add_argument('--torify', help='run delinker.py through the TOR service (requires TOR to be installed)', action='store_true')
    args = parser.parse_args()

    if args.target and args.requests:
        delink_target()
