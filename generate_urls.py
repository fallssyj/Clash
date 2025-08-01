from pathlib import Path

def generate_urls(base_dir, url_prefix, exclude_dirs=None, exclude_files=None):
    base_path = Path(base_dir).resolve()
    exclude_dirs = set(exclude_dirs or [])
    exclude_files = set(exclude_files or [])

    for file in base_path.rglob('*'):
        # 跳过排除的目录
        if any(part in exclude_dirs for part in file.parts):
            continue
        # 跳过排除的文件
        if file.name in exclude_files:
            continue
        if file.is_file():
            rel_path = file.relative_to(base_path).as_posix()
            url = f"{url_prefix}{rel_path}"
            print(url)

if __name__ == "__main__":
    base_dir = '.'
    url_prefix = 'https://gh-proxy.com/github.com/fallssyj/Clash/raw/refs/heads/main/'
    # 需要排除的目录
    exclude_dirs = ['.git', '.github', '__pycache__', 'node_modules']
    # 需要排除的文件
    exclude_files = ['README.md', '.DS_Store', '.gitattributes' , '.gitignore']
    generate_urls(base_dir, url_prefix, exclude_dirs, exclude_files)
