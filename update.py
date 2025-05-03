import requests
import sys
import os


urls = [
    'https://raw.githubusercontent.com/dler-io/Rules/refs/heads/main/Clash/Provider/TikTok.yaml',
    'https://raw.githubusercontent.com/dler-io/Rules/refs/heads/main/Clash/Provider/AI%20Suite.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/Apple-proxy.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/Apple-direct.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/CN.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/common-ad-keyword.yaml',
    'https://raw.githubusercontent.com/Hackl0us/SS-Rule-Snippet/refs/heads/main/Rulesets/Clash/Basic/foreign.yaml',
    'https://raw.githubusercontent.com/dler-io/Rules/refs/heads/main/Clash/Provider/Steam.yaml'
]

def getFile(url):
    try:
        res = requests.get(url)
        if res.status_code != 200:
            print(f"Failed to retrieve {url}: {res.status_code}")
            return
        name = os.path.basename(url).replace('%20', '-') 
        file_path = os.path.join(os.path.dirname(__file__), name) 
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(res.text)
    except Exception as e:
        print(e)


def main():

  for url in urls:
    getFile(url)


if __name__ == '__main__':
  main()
