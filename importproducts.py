#API to connect with ODOO
import xmlrpclib
import csv

server = "http://localhost:8069"
database = "dietfacts"
user = "admin"
pwd = "admin"

common = xmlrpclib.ServerProxy( '%s/xmlrpc/2/common' % server)

#print (common.version())
#Run this code below(with print) to see if it is working. Should return
#some server and version information

uid = common.authenticate(database, user, pwd, {})

#print (uid) #should return 1

OdooApi = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)

product_count = OdooApi.execute_kw(database, uid, pwd, 'product.template', 'search_count',[[]])

print product_count


