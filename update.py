import os
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# 基本路径
BASE_DIR = Path(__file__).resolve().parent
PROVIDER_DIR = BASE_DIR / 'Providers'
ICONS_DIR = BASE_DIR / 'assets' / 'icons'
URL_FILE = BASE_DIR / 'urls.txt'

# GitHub 仓库前缀（用于刷新 jsDelivr 缓存）
REPO_PREFIX = 'fallssyj/Clash'

def ensure_dir(path: Path):
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)

def read_urls_from_file(filepath: Path):
    """读取 url 列表"""
    if not filepath.exists():
        print(f"[!] URL 文件不存在: {filepath}")
        return []
    return [line.strip() for line in filepath.read_text(encoding='utf-8').splitlines() if line.strip()]

def download_file(url: str):
    """下载单个文件"""
    try:
        res = requests.get(url)
        res.raise_for_status()
        filename = Path(url).name.replace('%20', '-')
        file_path = PROVIDER_DIR / filename
        file_path.write_text(res.text, encoding='utf-8')
        print(f"[✓] 下载成功: {filename}")
    except requests.RequestException as e:
        print(f"[✗] 下载失败: {url}\n    错误: {e}")

def purge_jsdelivr_cache(relative_path: str):
    """刷新 jsDelivr 缓存"""
    purge_url = f'https://purge.jsdelivr.net/gh/{REPO_PREFIX}/{relative_path}'
    try:
        res = requests.get(purge_url)
        if res.status_code == 200:
            print(f"[✓] 缓存刷新成功: {relative_path}")
        else:
            print(f"[✗] 缓存刷新失败: {relative_path} (状态码: {res.status_code})")
    except requests.RequestException as e:
        print(f"[✗] 缓存刷新异常: {relative_path}\n    错误: {e}")

def main():
    ensure_dir(PROVIDER_DIR)
    ensure_dir(ICONS_DIR)

    print("=== 下载 Providers 文件 ===")
    urls = read_urls_from_file(URL_FILE)
    for url in urls:
        download_file(url)

    print("\n=== 刷新 Providers 缓存 ===")
    provider_files = [f.name for f in PROVIDER_DIR.glob('*') if f.is_file()]

    print("\n=== 刷新 assets/icons 缓存 ===")
    icon_files = [f.relative_to(BASE_DIR).as_posix() for f in ICONS_DIR.glob('*') if f.is_file()]

    all_to_purge = [f'Providers/{name}' for name in provider_files] + icon_files

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(purge_jsdelivr_cache, all_to_purge)

if __name__ == '__main__':
    main()
