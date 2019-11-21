import os

os.getcwd()
#os.chdir('..')
#os.getcwd()


import keycache
from bizutil import docsec

# channel =
# keybus('

keycache.set_pass( docsec.get('default') )
keycache.set_alias('default')

# WRITE BLOBS TEST:
keycache.generate( pubkey='default', privkey=docsec.get('default') )
keycache.generate( pubkey='miccco',  privkey=docsec.get('miccco') )

e=keycache.get('coinbasepro')
# keycache.sec() # default / key
# keycache.sec( 'miccco')
#a= keycache.get('coinbasepro')


from mesh.models.alias import Alias


# WOW ALIAS
a = Alias( identifier='default' )
a.scope()
keycache.set( 'coinspace' , {'un':'megauser', 'pw':'learnforever'} )
a = keycache.get( 'coinspace' )




#keycache.set_cred('defaultx','defaultx')
#keycache.set_alias('default1x2')
#keycache.set_pass('default1x2')

keycache.set( 'coinspace' , {'un':'megauser', 'pw':'learnforever'}   )
blob = keycache.get( 'coinspace' )
print( blob )

l=3
keycache.set( 'mongo' , {'kun':'megauser', 'kpw':'learnforever'}   )
blob = keycache.get( 'mongo' )


d=4
keycache.set_alias('test1')
keycache.set_pass('test1')

keycache.set( 'mongo' , {'kun':'megauser' ,'kpw':'learnforever'}   )
blob = keycache.get( 'mongo' )


#   signalmesh.run()   #
#  signalmesh.nodes()  #