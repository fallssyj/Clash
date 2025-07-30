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

with open(output_filename, 'w', encoding='utf-8') as f:
    # 写入rules部分
    f.write('rules:\n')
    for filename in file_list:
        name_without_extension = os.path.splitext(filename)[0]
        f.write(f'  - RULE-SET,{name_without_extension} / Domain, \n')
    
    f.write('\n')  # 空行分隔不同部分
    f.write('rule-anchor:\n')
    f.write('  ip: &ip {type: http, interval: 86400, behavior: ipcidr, format: mrs}\n')
    f.write('  domain: &domain {type: http, interval: 86400, behavior: domain, format: mrs}\n')
    f.write('  class: &class {type: http, interval: 86400, behavior: classical, format: text}\n')
    f.write('\n')  # 空行分隔不同部分
    # 写入rule-providers部分
    f.write('rule-providers:\n')
    for filename in file_list:
        name_without_extension = os.path.splitext(filename)[0]
        f.write(f'  {name_without_extension} / Domain: {{<<: *class, url: \"{uri}{filename}\"}}\n')
