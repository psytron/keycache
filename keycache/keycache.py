
from . import blobstore
import os


class Keycache:

    def __init__(self , *args, **kwargs):
        print('New Key Cache instance')
        if not os.path.exists('vm'):
            os.mkdir('vm')
        self.default_alias=kwargs.get('alias','default')
        self.default_pass=kwargs.get('priv','default')
        self.default_path=kwargs.get('path','vm/cache/')
        self.creds = {}


    def generate( self,  pubkey='default' , privkey='default'):
        """Generates encrypted blob on disk
        pubkey String: incoming public key
        privkey String: incoming private key"""
        self.creds = blobstore.generate( pubkey , privkey )

    def set_alias( self, alias_in ):
        self.default_alias=alias_in
    def set_pass( self , pass_in ):
        self.default_pass=pass_in
    def set_path( self, path_in ):
        self.conf_path = path_in
    
    def load_config(self):
        blob_path = self.default_path+'/'+self.default_alias+'.yml'
        self.creds = blobstore.load_config( blob_path )


    def add(self , domain ,  kvs_in):
        self.creds[domain]=kvs_in
    def add_all(self , blob_dict ):
        for b in blob_dict:
            print( b )


    def load_blob(self):
        self.creds = blobstore.readblob( self.default_alias , self.default_pass )

    def save(self):
        blobstore.writeblob( self.default_alias , self.default_pass , self.creds )


    def get( self, domain ):
        if( domain in self.creds ):
            return self.creds[ domain ]
        else:
            self.creds = blobstore.readblob( self.default_alias , self.default_pass )
            if domain in self.creds:
                return self.creds[ domain ]
            else:
                print(' No Credential for this domain on this alias. ')

    def get_all( self ):
        if self.creds:
            return self.creds
        else:
            self.creds = blobstore.readblob( self.default_alias , self.default_pass )
            return self.creds

