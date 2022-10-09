import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
MIRRORED_API = "YOUR_API_KAY"



def Remote_URL_Upload(link):
    data = {'api_key': MIRRORED_API}
    info  = requests.post(url="https://www.mirrored.to/api/v1/get_upload_info", data=data, headers=headers).json()
    data['upload_id'] = info['message']['upload_id']
    data['remote_url'] = link
    requests.post(url = "https://www.mirrored.to/api/v1/api_remote_upload", data=data, headers=headers)
    data['mirrors'] = 'anonfiles,uptobox,zippyshare,mediafire'
    res = requests.post(url = "https://www.mirrored.to/api/v1/finish_upload", data=data, headers=headers).json()
    return res


url = 'DDL'
response = Remote_URL_Upload(url)
print(response)
