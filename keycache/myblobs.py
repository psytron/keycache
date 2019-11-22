
from . import blobstore
import os


class MyBlobs:

    def __init__(self , *args, **kwargs):
        print('New Key Cache instance')
        if not os.path.exists('vm'):
            os.mkdir('vm')
        self.default_alias=kwargs.get('alias','default')
        self.default_pass=kwargs.get('priv','default')
        self.blobs = {}


    def generate( self,  pubkey='default' , privkey='default'):
        print( 'generate()' )
        self.blobs = blobstore.generate( pubkey , privkey )

    def add(self , domain ,  blob_in):
        self.blobs[domain]=blob_in
        blobstore.writeblob( self.default_alias , self.default_pass , self.blobs )


    def get( self, domain ):
        if( domain in self.blobs ):
            return self.blobs[ domain ]
        else:
            #pxpx = docsec.get('dxdx', default='NONE' , alias=alias )
            self.blobs = blobstore.readblob( self.default_alias , self.default_pass )
            if domain in self.blobs:
                return self.blobs[ domain ]
            else:
                print(' No Credential for this domain on this alias. ')

    def get_all(self):
        if self.blobs:
            return self.blobs
        else:
            self.blobs = blobstore.readblob( self.default_alias , self.default_pass )
            return self.blobs

