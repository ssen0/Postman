import urllib.request
import json
import datetime
now = datetime.datetime.now()
#url指定
url = 'http://192.168.63.174:8181/api/push_notification'
#header作成
req_header = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-api-key': '774a2175-e19a-4983-a100-4014255c8d2e',
}
#body作成
req_data = json.dumps({
   'dateTime': now.strftime("%Y/%m/%d %H:%M:%S"),
   'camNo': 1,
   'state': "起床",
})

# req_data2 = json.dumps({
#    'dateTime': now.strftime("%Y/%m/%d %H:%M:%S"),
#    'camNo': 3,
#    'state': "離床",
# })

# req_data3 = json.dumps({
#    'dateTime': now.strftime("%Y/%m/%d %H:%M:%S"),
#    'camNo': 1,
#    'state': "離床",
# })

#リクエスト処理
req = urllib.request.Request(url, data=req_data.encode(), method='POST', headers=req_header)
try:
  with urllib.request.urlopen(req) as response:
    res_time = datetime.datetime.now()
    # body = json.loads(response.read())
    # header = response.getheaders()
    # status = response.getcode()
    print(response.read())
    time = res_time - now
    print(time)
    #print(header)
    #print(status)
except urllib.error.URLError as e:
  print(e.reason)

# req2 = urllib.request.Request(url, data=req_data2.encode(), method='POST', headers=req_header)
# try:
#   with urllib.request.urlopen(req2) as response:
#     res_time = datetime.datetime.now()
#     # body = json.loads(response.read())
#     # header = response.getheaders()
#     # status = response.getcode()
#     print(response.read())
#     #print(header)
#     #print(status)
# except urllib.error.URLError as e:
#   print(e.reason)

# req3 = urllib.request.Request(url, data=req_data3.encode(), method='POST', headers=req_header)
# try:
#   with urllib.request.urlopen(req3) as response:
#     res_time = datetime.datetime.now()
#     # body = json.loads(response.read())
#     # header = response.getheaders()
#     # status = response.getcode()
#     print(response.read())
#     #print(header)
#     #print(status)
# except urllib.error.URLError as e:
#   print(e.reason)