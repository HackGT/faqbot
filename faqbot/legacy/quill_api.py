import requests
import json

def get_wl(at, ep):
	HEADERS = {'x-access-token': at}
	r = requests.get(ep, headers=HEADERS)
	j = json.loads(r.text)
	return j

def post_wl(lst, at, ep):
	HEADERS = {'x-access-token': at}
	j = {'emails': lst}
	r = requests.put(ep, headers=HEADERS, json=j)

	print r.text

	if r.status_code == 200:
		return True
	else:
		return False


if __name__ == "__main__":
	print post_wl(get_wl() + ['shreyask@mit.edu'])
