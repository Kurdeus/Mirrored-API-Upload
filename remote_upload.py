import requests




class Mirrpred_Upload:
	def __init__(self, api_key):
		self.api_key = api_key
		self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}

	def Remote_URL(self, ddl):
		data = {'api_key': self.api_key}
		info  = requests.post(url = "https://www.mirrored.to/api/v1/get_upload_info", data=data, headers=self.headers).json()
		data['upload_id'] = info['message']['upload_id']
		data['remote_url'] = ddl
		requests.post(url = "https://www.mirrored.to/api/v1/api_remote_upload", data=data, headers=self.headers)
		data['mirrors'] = 'anonfiles,uptobox,zippyshare,mediafire'
		res = requests.post(url = "https://www.mirrored.to/api/v1/finish_upload", data=data, headers=self.headers).json()
		return res



