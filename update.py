import requests
import  sys


GFWlist_url = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list'
BanAD_url = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list'
BanProgramAD_url = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list'
OpenAi_url = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/OpenAi.list'

def getGfwlist():
  try:
    res = requests.get(GFWlist_url)
    if res.status_code != 200:
      return
    f = open(sys.path[0] + '/ProxyGFWlist.list',mode='w',encoding='utf-8')
    f.write(res.text)
    f.close()
  except Exception as e:
    print(e)

def getBanAD():
  try:
    res = requests.get(BanAD_url)
    if res.status_code != 200:
      return
    f = open(sys.path[0] + '/BanAD.list',mode='w',encoding='utf-8')
    f.write(res.text)
    f.close()
  except Exception as e:
    print(e)

def getBanProgramAD():
  try:
    res = requests.get(BanProgramAD_url)
    if res.status_code != 200:
      return
    f = open(sys.path[0] + '/BanProgramAD.list',mode='w',encoding='utf-8')
    f.write(res.text)
    f.close()
  except Exception as e:
    print(e)

def getOpenAi():
  try:
    res = requests.get(OpenAi_url)
    if res.status_code != 200:
      return
    f = open(sys.path[0] + '/OpenAi.list.list',mode='w',encoding='utf-8')
    f.write(res.text)
    f.close()
  except Exception as e:
    print(e)

def main():
  getGfwlist()
  getBanAD()
  getBanProgramAD()


if __name__ == '__main__':
  main()