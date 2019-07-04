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

#filter = [[('categ_id.name','=','Diet Items')]]

# var         | object | method   | base    |auth| pass  |model            | method
#product_count = OdooApi.execute_kw(database, uid, pwd, 'product.template', 'search_count', filter)

filter2 = [[('largemeal','=',True)]]

meals_count = OdooApi.execute_kw(database, uid, pwd, 'res.users.meal', 'search_count', filter2)

print (meals_count) #will return all the record in that table