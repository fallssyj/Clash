import os
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

BASE_DIR = Path(__file__).resolve().parent
PROVIDER_DIR = BASE_DIR / 'Providers'
ICONS_DIR = BASE_DIR / 'assets' / 'icons'
URL_FILE = BASE_DIR / 'urls.txt'
REPO_PREFIX = 'fallssyj/Clash'

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def read_urls_from_file(filepath: Path) -> List[str]:
    """读取 url 列表，忽略注释和空行"""
    if not filepath.exists():
        print(f"[!] URL 文件不存在: {filepath}")
        return []
    return [
        line.strip()
        for line in filepath.read_text(encoding='utf-8').splitlines()
        if line.strip() and not line.strip().startswith('#')
    ]

def download_file(url: str, timeout: int = 15) -> str:
    try:
        res = requests.get(url, timeout=timeout)
        res.raise_for_status()
        filename = Path(url).name.replace('%20', '-')
        file_path = PROVIDER_DIR / filename
        try:
            file_path.write_bytes(res.content)
            print(f"[✓] 下载成功: {filename}")
        except Exception as e:
            print(f"[✗] 文件写入失败: {filename}\n    错误: {e}")
        return filename
    except requests.RequestException as e:
        print(f"[✗] 下载失败: {url}\n    错误: {e}")
        return ""

def download_all_files(urls: List[str]):
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(download_file, url): url for url in urls}
        for future in as_completed(futures):
            future.result()

def main():
    ensure_dir(PROVIDER_DIR)
    ensure_dir(ICONS_DIR)

    print("=== 下载 Providers 文件 ===")
    urls = read_urls_from_file(URL_FILE)
    if urls:
        download_all_files(urls)
    else:
        print("[!] 没有可下载的 URL。")

if __name__ == '__main__':
    main()