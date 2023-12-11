import southpaw

#getting access to the API with the appropriate information
basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'
x_auth_token = 'eyasdffdsaasjhkdfbfkhdsbakjbasdkjfbnfkjdsaetgdffgdfdgs'
fanduel_email = 'calebcaulk02@gmail.com'
fanduel_password = 'fakeFanduelPassword'

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token, x_auth_token)