#!/usr/bin/env python3
# Tools Name : HTTP TO API USERGRID
# Author : XSVSCyb3rID
# Sites : https://xsvscyb3r.id
# Email : xsvscyb3r@proton.me
# Github : github.com/XSVSCyb3rID

import requests

# Fungsi untuk mengirim permintaan POST
def send_post(url, data):
    response = requests.post(url, json=data)
    return response

# Fungsi untuk mengirim permintaan GET
def send_get(url):
    response = requests.get(url)
    return response

# Fungsi untuk mengirim permintaan PUT
def send_put(url, data):
    response = requests.put(url, json=data)
    return response

# Buat user Hack3r
url1 = "https://api.usergrid.com/management/organizations/my-org/users"
data1 = {"username": "Hack3r", "name": "Hack3r", "email": "hack3rhack3r@gmail.com", "password": "334435gF4571411726C9FURKrbx336289431AD8EC9"}
response1 = send_post(url1, data1)
print("Response 1:", response1.text)

# Buat user Jim Admin
url2 = "https://api.usergrid.com/management/organizations/my-org/users"
data2 = {"username": "jim.admin", "name": "Jim Admin", "email": "jim.admin@gmail.com", "password": "test12345"}
response2 = send_post(url2, data2)
print("Response 2:", response2.text)

# Dapatkan feed Jim Admin
url3 = "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/feed"
response3 = send_get(url3)
print("Response 3:", response3.text)

# Reactivate user Jim Admin
url4 = "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/reactivate"
response4 = send_get(url4)
print("Response 4:", response4.text)

# Aktivasi user Jim Admin dengan token
url5 = "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/activate"
params = {"token": "33dd0563-cd0c-11e1-bcf7-12313d1c4491"}
response5 = send_get(url5, params=params)
print("Response 5:", response5.text)

# Reset password Jim Admin
url6 = "https://api.usergrid.com/management/organizations/my-org/users/resetpw"
data6 = {"recaptcha_response_field": "Atistophanes tseFia", "recaptcha_challenge_field": "Atistophanes tseFia", "email": "jim.admin@gmail.com"}
response6 = send_post(url6, data6)
print("Response 6:", response6.text)

# Dapatkan link reset password
url7 = "https://api.usergrid.com/management/organizations/my-org/users/resetpw"
response7 = send_get(url7)
print("Response 7:", response7.text)

# Ubah password Jim Admin
url8 = "https://api.usergrid.com/management/users/jim.admin/password"
data8 = {"oldpassword": "test123", "newpassword": "mynewpassword"}
response8 = send_put(url8, data8)
print("Response 8:", response8.text)

# Update data user Jim Admin
url9 = "https://api.usergrid.com/management/organizations/my-org/users/jim.admin"
data9 = {"city": "San Francisco", "state": "California"}
response9 = send_put(url9, data9)
print("Response 9:", response9.text)

# Dapatkan data user Jim Admin
url10 = "https://api.usergrid.com/management/organizations/my-org/users/jim.admin"
response10 = send_get(url10)
print("Response 10:", response10.text)

