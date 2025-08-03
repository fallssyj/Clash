#!/bin/sh

# 下载并执行 feed.sh
wget -O - https://gh-proxy.com/github.com/nikkinikki-org/OpenWrt-nikki/raw/refs/heads/main/feed.sh | ash

# 安装相关软件包
opkg update
opkg install nikki
opkg install luci-app-nikki
opkg install luci-i18n-nikki-zh-cn
opkg install luci-app-ttyd
opkg install luci-theme-argon
opkg install luci-app-argon-config
opkg install openssh-sftp-server

echo "所有应用已安装完成！"
