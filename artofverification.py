geturl = raw_input().split('?')[1]
geturl, key = geturl.split('&key=')
geturl, role = geturl.split('&role=')
geturl, profile = geturl.split('&profile=')
geturl, pwd = geturl.split('&pwd=')
geturl, un = geturl.split('username=')
 
print "username: %s"%un
print "pwd: %s"%pwd
print "profile: %s"%profile
print "role: %s"%role
print "key: %s"%key
