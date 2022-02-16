#utf-8
import shodan
SHODAN_API_KEY = "SkVS0RAbiTQpzzEsahqnq2Hv6SwjUfs3"
api = shodan.Shodan(SHODAN_API_KEY)
file_object = open('ip.txt', 'w')
try:
    results = api.search('Apache -country:CN')
    print 'Results found: %s' % results['total']
    for result in results['matches']:         
            print ("%s:%s"%(result['ip_str'],result['port']))
            file_object.writelines(result['ip_str']+":"+result['port']+'\n')
except shodan.APIError, e:
    print 'Error: %s' % e
file_object.close()