### Keycache
Keycache is encrypted key:value store for your sensitive credentials


Install:
    
    pip install git+git@github.com:psytron/keycache.git#egg=keycache



Usage:
    
    from keycache import Keycache
      
    k1 = Keycache( 
        alias='api_workers',                        # Blob namespace
        private_key='key_from_secure_message_bus',  # Encryption key
        config_path='config/my_secrets.yml' ,       # File with API Keys
        blobs_path='blobs/dir' )                    # Where to store encrypted blobs
    
    k1.add('some_namespace' , { 'key1':'val1' , 'key2':'val2'} )
    k1.save() 

