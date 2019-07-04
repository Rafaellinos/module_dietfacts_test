#API to connect with ODOO
import xmlrpclib
import csv

server = "http://localhost:8069"
database = "dietfacts"
user = "admin"
pwd = "admin"

common = xmlrpclib.ServerProxy( '%s/xmlrpc/2/common' % server)

print (common.version())


