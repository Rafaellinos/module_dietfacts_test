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

#filter2 = [[('largemeal','=',True)]]

#meals_count = OdooApi.execute_kw(database, uid, pwd, 'res.users.meal', 'search_count', filter2)

#print (meals_count) #will return all the record in that table

filename= "importdata.csv"

reader = csv.reader(open(filename, 'rb'))

args = [[('name','=','Diet Items')]]

categ_id = OdooApi.execute_kw(database, uid, pwd, 'product.category', 'search', args) #return list obj

for row in reader: # for each row in csv file
    #print row
    productname = row[0] #Adding the two vars in csv
    calories = row[1]

    filter = [[('name', '=', productname)]] 
    # use the filter to seach the product
    product_id = OdooApi.execute_kw(database, uid, pwd, 'product.template', 'search', filter)
    # if not exist, the record will be added on the data base
    if not product_id:
        record = [{'name': productname, 'calories': calories, 'categ_id': categ_id[0]}]
        OdooApi.execute_kw(database, uid, pwd, 'product.template', 'create', record)
        print ('Produt: '+ productname+ ' created!')
    elif produt_id:
        record = {'calories': calories, 'categ_id': categ_id[0]}
        OdooApi.execute_kw(database, uid, pwd, 'product.template', 'write', [product_id, record])
        print ('Produt: '+ productname + ' found and updated!')
        # identifies the ID(produt_id) and then, update it
    else:
        print ('The product '+ productname + ' already exists on the system!')