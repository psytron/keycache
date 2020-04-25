### Keycache
Keycache is encrypted key:value store for your sensitive credentials


Install:
    
    pip install git+git@github.com:psytron/keycache.git#egg=keycache



Usage:
    
    from keycache.keycache import Keycache
      
    k1 = Keycache( 
        alias='some_namespace' , 
        private_key='pull_this_from_secure_message_bus' , 
        path='vm/cache' )
    
    # ADD VALUES 
    k1.add('some_namespace' , { 'key1':'val1' , 'key2':'val2'} )
    
    # SAVE TO DISK 
    k1.save() 

