import os

os.getcwd()
#os.chdir('..')
#os.getcwd()


from keycache import Keycache


# channel =
# keybus('
k = Keycache( identifier='wow' , private_key='whwo')


# WRITE BLOBS TEST:
#keycache.generate( pubkey='default', privkey=docsec.get('default') )
#keycache.generate( pubkey='miccco',  privkey=docsec.get('miccco') )

#e=keycache.get('coinbasepro')
# keycache.sec() # default / key
# keycache.sec( 'miccco')
#a= keycache.get('coinbasepro')


#from mesh.models.alias import Alias


# WOW ALIAS
#a = Alias( identifier='default' )
#a.scope()
#keycache.set( 'coinspace' , {'un':'megauser', 'pw':'learnforever'} )
#a = keycache.get( 'coinspace' )




#keycache.set_cred('defaultx','defaultx')
#keycache.set_alias('default1x2')
#keycache.set_pass('default1x2')

k.add( 'coinspace' , {'un':'megauser', 'pw':'learnforever'}   )
blob = k.get( 'coinspace' )
print( blob )

