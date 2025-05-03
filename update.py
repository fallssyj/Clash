import requests
import sys
import os


urls = [
    'https://raw.githubusercontent.com/dler-io/Rules/refs/heads/main/Clash/Provider/TikTok.yaml',
    'https://raw.githubusercontent.com/dler-io/Rules/refs/heads/main/Clash/Provider/AI%20Suite.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/Apple-proxy.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/Apple-direct.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/CN.yaml',
    'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/refs/heads/master/Clash/Providers/BanAD.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/foreign.yaml'
]

def getFile(url):
    try:
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Failed to retrieve {url}: {res.status_code}")
            return
        name = os.path.basename(url).replace('%20', '-') 
        file_path = os.path.join(os.path.dirname(__file__),'Providers', name) 
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(res.text)
    except Exception as e:
        print(e)

    
def main():
  for url in urls:
    getFile(url)
    


if __name__ == '__main__':
  main()
  provider_dir = os.path.join(os.path.dirname(__file__), 'Providers')
  yaml_files = [f for f in os.listdir(provider_dir) if f.endswith('.yaml')]
  for yaml in yaml_files:
    requests.get('https://purge.jsdelivr.net/gh/fallssyj/Clash/Providers/' + yaml)
