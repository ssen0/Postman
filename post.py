import urllib.request
import json
import datetime
now = datetime.datetime.now()
#url指定
url = 'http://192.168.65.20:3001/tests'
#header作成
req_header = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-api-key': '774a2175-e19a-4983-a100-4014255c8d2e',
}
#body作成
req_data = json.dumps({
    'name':"test",
})
#リクエスト処理
req = urllib.request.Request(url, data=req_data.encode(), method='POST', headers=req_header)
try:
  with urllib.request.urlopen(req) as response:
    res_time = datetime.datetime.now()
    body = json.loads(response.read())
    header = response.getheaders()
    status = response.getcode()
    print(body)
    time = res_time - now
    print(time)
    #print(header)
    #print(status)
except urllib.error.URLError as e:
  print(e.reason)