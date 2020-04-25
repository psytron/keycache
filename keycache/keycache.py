
import io, json, yaml
from . import blobstore
import os


class Keycache:

    def __init__(self , *args, **kwargs):
        print('New Key Cache instance')
        if not os.path.exists('vm'):
            os.mkdir('vm')
        self.default_alias=kwargs.get('alias','default')
        self.default_pass=kwargs.get('private_key','default')
        self.config_path=kwargs.get('config_path','vm/cache')
        self.blob_path=kwargs.get('blob_path','vm')
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
    

    def load_config( self, path_in=False ):
        if path_in:
            self.config_path = path_in
        ipath = self.config_path +'/'+self.default_alias+'.yml'
        with open( ipath , "rb") as fIn:
            config_list = yaml.load(fIn, Loader=yaml.FullLoader)
            print('Read Config Success')
        config_dict = { x['domain']:x for x in config_list }
        self.creds = config_dict



    def add(self , namespace ,  kvs_in ):
        self.creds[ namespace ]=kvs_in
    def add_all(self , blob_dict ):
        for b in blob_dict:
            print( b )


    def load_blob(self):
        self.creds = blobstore.readblob( self.default_alias , self.default_pass )

    def save(self):
        blobstore.writeblob( self.default_alias , self.default_pass , self.creds , self.blob_path )


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

