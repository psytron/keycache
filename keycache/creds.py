
from . import blobstore
import os


class Creds:

    def __init__(self , *args, **kwargs):
        print('New Key Cache instance')
        if not os.path.exists('vm'):
            os.mkdir('vm')
        self.default_alias=kwargs.get('alias','default')
        self.default_pass=kwargs.get('priv','default')
        self.creds = {}


    def generate( self,  pubkey='default' , privkey='default'):
        print( 'generate()' )
        self.creds = blobstore.generate( pubkey , privkey )

    def add(self , domain ,  blob_in):
        self.creds[domain]=blob_in

    def add_all(self , blob_dict ):
        for b in blob_dict:
            print( b )

    def load_config(self):
        self.creds = blobstore.load_config( self.default_alias )


    def load_blob(self):
        self.creds = blobstore.readblob( self.default_alias , self.default_pass )

    def save(self):
        blobstore.writeblob( self.default_alias , self.default_pass , self.creds )


    def get( self, domain ):
        if( domain in self.creds ):
            return self.creds[ domain ]
        else:
            #pxpx = docsec.get('dxdx', default='NONE' , alias=alias )
            self.creds = blobstore.readblob( self.default_alias , self.default_pass )
            if domain in self.creds:
                return self.creds[ domain ]
            else:
                print(' No Credential for this domain on this alias. ')

    def get_all(self):
        if self.creds:
            return self.creds
        else:
            self.creds = blobstore.readblob( self.default_alias , self.default_pass )
            return self.creds

