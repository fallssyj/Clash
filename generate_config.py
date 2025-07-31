import os

# 设置Providers目录路径
providers_dir = 'Providers'

# 获取目录下所有文件
files = os.listdir(providers_dir)

# 过滤出文件
file_list = [f for f in files if os.path.isfile(os.path.join(providers_dir, f))]

# 定义输出文件路径
output_filename = 'clash.yaml'
uri = 'https://cdn.jsdelivr.net/gh/fallssyj/Clash/Providers/'

# 读取已有的配置内容
with open('config.yaml', 'r', encoding='utf-8') as f_in:
    existing_content = f_in.read()

# 写入到新的配置文件
with open(output_filename, 'w', encoding='utf-8') as f:

    # 先写入原有配置
    f.write(existing_content)

    # 写入rule-providers部分
    for filename in file_list:
        name_without_extension = os.path.splitext(filename)[0]
        f.write(f'  {name_without_extension}: {{<<: *class, url: \"{uri}{filename}\"}}\n')
