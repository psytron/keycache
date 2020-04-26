

# github.com/psytron/keycache
# USAGE :
# keycache.set_system_encrypt_key( sysfinger.generate() )
# keycache.get('healthity' , alias='healthify')
# future usage
# levels.set( 'alias L 0' ,'domain L 1' )
# def set( self , 'level_0' , 'level_1'):
#   print(' next level ')


#NSTANCE OF CREDS for STATIC LOCAL USE: 
from .keycache import Keycache
inst = Keycache( alias='default' , priv='default' )
set_pass = inst.set_pass
get = inst.get
generate= inst.generate






'''
aliases = {}
from . import blobstore
import os

# MAKE DIR FOR BLOBS
if not os.path.exists('vm'):
    os.mkdir('vm')

default_alias = 'default'
default_pass  = 'default'  # sysfinger # OR 'default' # hardware autolocked 
def set_alias( alias_in ):
    global default_alias
    default_alias=alias_in

def set_pass( pass_in ):
    global default_pass
    default_pass=pass_in

def generate( pubkey='default' , privkey='default'):
    """Generates encrypted blob on disk
        pubkey String: incoming public key
        privkey String: incoming private key"""
    blobstore.generate( pubkey , privkey )

def get( domain ):
    global aliases
    alias = default_alias
    if( alias in aliases ) and domain in aliases[alias]:
        return aliases[ alias ][ domain ]
    else:
        #pxpx = docsec.get('dxdx', default='NONE' , alias=alias )
        aliases[ alias ] = blobstore.readblob( alias , default_pass )
        if domain in aliases[ alias ]:
            return aliases[ alias ][ domain ]
        else:
            print(' No Credential for ',domain,' on this alias: ',alias)

def get_all( alias=default_alias , priv=default_pass ):
    global aliases
    if alias in aliases:
        return aliases[ alias ]
    else:
        aliases[ alias ]= blobstore.readblob( alias , default_pass )
        return  aliases[ alias ]

def set( domain , obj ):
    obj['domain']=domain # add own domain into hash
    # In The Future Version this should hash the filename before writing the blob.
    if( default_alias in aliases ) and (domain in aliases[default_alias]):
        aliases[ default_alias ][ domain ]=obj
    elif( default_alias in aliases ) and (domain not in aliases[ default_alias ]):
        aliases[ default_alias ][domain]=obj
        out_blob = aliases[ default_alias ]
        blobstore.writeblob( default_alias , default_pass , out_blob )
            #return blobstore.readblob(  default_alias , default_pass )

    elif( default_alias not in aliases) :
        aliases[ default_alias ]={}
        aliases[ default_alias ][domain]=obj
        blobstore.writeblob( default_alias , default_pass , aliases[ default_alias ] )
            #return blobstore.readblob(  default_alias , default_pass )

    return aliases[ default_alias ][ domain ]
    # THIS Tries to load Alias blob OR default from disk
    # IF doesn't exist: it creates blob
    # and writes file and saves and then returns unencrypted keyval based on provided passphrase






'''