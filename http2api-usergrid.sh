#!/usr/bin/bash
# Tools Name : HTTP TO API USERGRID
# Author : XSVSCyb3rID
# Sites : https://xsvscyb3r.id
# Email : xsvscyb3r@proton.me
# Github : github.com/XSVSCyb3rID

# Buat user Hack3r
curl -X -i POST "https://api.usergrid.com/management/organizations/my-org/users" -d '{"username":"Hack3r","name":"Hack3r","email":"hack3rhack3r@gmail.com","password":"334435gF4571411726C9FURKrbx336289431AD8EC9"}'

# Buat user Jim Admin
curl -X -i POST "https://api.usergrid.com/management/organizations/my-org/users" -d '{"username":"jim.admin","name":"Jim Admin","email":"jim.admin@gmail.com","password":"test12345"}'

# Dapatkan feed Jim Admin
curl -X GET "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/feed"

# Reactivate user Jim Admin
curl -X GET "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/reactivate"

# Aktivasi user Jim Admin dengan token
curl -X GET "https://api.usergrid.com/management/organizations/my-org/users/jim.admin/activate?token=33dd0563-cd0c-11e1-bcf7-12313d1c4491"

# Reset password Jim Admin
curl -X -i POST "https://api.usergrid.com/management/organizations/my-org/users/resetpw" -d '{"recaptcha_response_field":"Atistophanes tseFia","recaptcha_challenge_field":"Atistophanes tseFia","email":"jim.admin@gmail.com"}'

# Dapatkan link reset password
curl -X GET "https://api.usergrid.com/management/organizations/my-org/users/resetpw"

# Ubah password Jim Admin
curl -X -i PUT "https://api.usergrid.com/management/users/jim.admin/password" -d '{"oldpassword":"test123", "newpassword":"mynewpassword"}'

# Update data user Jim Admin
curl -X -i PUT "https://api.usergrid.com/management/organizations/my-org/users/jim.admin" -d '{"city":"San Francisco","state":"California"}'

# Dapatkan data user Jim Admin
curl -X GET "https://api.usergrid.com/management/organizations/my-org/users/jim.admin"
