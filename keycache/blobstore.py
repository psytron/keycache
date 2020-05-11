

import io, json, yaml
from os import stat, remove
import pyAesCrypt as crypsav




# need to convert private key config to blob
# need  alias_in , pass_in
def generate( alias_in , pass_in ):
    ipath='vm/cache/'+alias_in+'.yml'
    bufferSize = 64 * 1024 # buffer size - 64K
    with open( ipath , "rb") as fIn:
        with open( 'vm/'+alias_in , "wb") as fOut:
            crypsav.encryptStream(fIn, fOut, pass_in , bufferSize ) # encryption/decryption
            print('Success')



def writeblob( alias_in, pw_in, obj_in , save_path ):
    bufferSize = 64 * 1024 # 64K
    blobpath = save_path+'/'+alias_in
    with open( blobpath , "wb") as fOut:
        fIn = io.BytesIO( yaml.dump( obj_in ).encode('utf8') )
        crypsav.encryptStream(fIn, fOut, pw_in , bufferSize ) # encryption/decryption
        print('Success')




def readblob( alias_in  , pw_in , alias='default' , blob_path='vm' ):
    bufferSize = 64 * 1024 # 64K
    blobpath = blob_path+'/'+alias_in
    try:
        with open( blobpath , "rb") as fIn:  # decrypt #
            fOut = io.BytesIO()                        #
            encFileSize = stat( blobpath ).st_size     #
            #print(' attempt rxrx:', len(str(pw_in)) , 'blobpath:',blobpath , pw_in[:2])  #
            crypsav.decryptStream(fIn, fOut, pw_in , bufferSize, encFileSize)
            data_cluster = yaml.load( fOut.getvalue() , Loader=yaml.FullLoader )
            #credential_node = data_cluster    #['operators'][0]['credentials']
            #aliases[alias_in]={}
            # WRITE ALL PROPERTIES INSIDE CLUSTER NAMED BY DOMAIN
            #for cred in data_cluster:
            #    aliases[alias_in][ cred['domain'] ]= cred
            #    if 'key' in cred:
            #        cred['apiKey']=cred['key']
            fOut.close()
        return data_cluster
    except Exception as e:
        # no file 
        print( e )