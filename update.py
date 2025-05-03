import requests
import os

URLS = [
    'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/refs/heads/master/Clash/Providers/BanAD.yaml',
    'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/refs/heads/master/Clash/Providers/ProxyGFWlist.yaml',
    'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/refs/heads/master/Clash/Providers/Ruleset/AI.yaml'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROVIDER_DIR = os.path.join(BASE_DIR, 'Providers')

def ensure_provider_dir():
    if not os.path.exists(PROVIDER_DIR):
        os.makedirs(PROVIDER_DIR)

def download_file(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        filename = os.path.basename(url).replace('%20', '-')
        file_path = os.path.join(PROVIDER_DIR, filename)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(res.text)
        
        print(f"Downloaded: {filename}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def purge_jsdelivr_cache(filename):
    purge_url = f'https://purge.jsdelivr.net/gh/fallssyj/Clash/Providers/{filename}'
    try:
        res = requests.get(purge_url)
        if res.status_code == 200:
            print(f"Purged cache for: {filename}")
        else:
            print(f"Failed to purge cache for {filename}: {res.status_code}")
    except requests.RequestException as e:
        print(f"Error purging cache: {e}")

def main():
    ensure_provider_dir()
    for url in URLS:
        download_file(url)

    # 遍历 Providers 目录并刷新 jsDelivr 缓存
    yaml_files = [f for f in os.listdir(PROVIDER_DIR) if f.endswith('.yaml')]
    for yaml_file in yaml_files:
        purge_jsdelivr_cache(yaml_file)

if __name__ == '__main__':
    main()
