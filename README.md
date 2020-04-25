### Keycache
Keycache is encrypted key:value store for your sensitive credentials


Usage:
    
    # SPECIFIC
    k2 = Keycache( 
        alias='some_namespace' , 
        private_key='pull_this_from_secure_message_bus' , 
        path='vm/cache' )
    
    # ADD VALUES 
    k2.add('some_namespace' , { 'key1':'val1' , 'key2':'val2'} )
    
    # SAVE TO DISK 
    k2.save() 

