import os

def generate_clash_config(
    providers_dir='Providers',
    base_config='config.yaml',
    output_filename='clash.yaml',
    uri='https://cdn.jsdelivr.net/gh/fallssyj/Clash/Providers/'
):
    # 检查Providers目录是否存在
    if not os.path.isdir(providers_dir):
        print(f"目录不存在: {providers_dir}")
        return

    # 获取并排序所有文件
    try:
        files = sorted(
            f for f in os.listdir(providers_dir)
            if os.path.isfile(os.path.join(providers_dir, f))
        )
    except Exception as e:
        print(f"读取目录出错: {e}")
        return

    # 读取已有的配置内容
    try:
        with open(base_config, 'r', encoding='utf-8') as f_in:
            existing_content = f_in.read()
    except FileNotFoundError:
        print(f"找不到基础配置文件: {base_config}")
        return

    # 写入到新的配置文件
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            # 先写入原有配置
            f.write(existing_content)
            f.write('\nrule-providers:\n')
            # 写入rule-providers部分
            for filename in files:
                name_without_extension = os.path.splitext(filename)[0]
                f.write(f'  {name_without_extension}: {{<<: *class, url: "{uri}{filename}"}}\n')
        print(f"配置文件已生成: {output_filename}")
    except Exception as e:
        print(f"写入配置文件出错: {e}")

if __name__ == "__main__":
    generate_clash_config()
