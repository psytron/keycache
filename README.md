### Keycache
Keycache is an AES encrypted key:value store for your sensitive credentials. It can be used for database passwords, API-keys, private certificates or anything you don't want floating around on your filesystem. The module works as both static singleton and class instance for multiple simultaneous stores.


Install:
```bash    
pip install git+git://github.com/psytron/keycache.git#egg=keycache
```

Simple Usage:
```python
import keycache
keycache.add('name_space', {'key1':'val1'} )
keycache.save()
```


Multi Usage:

```python
from keycache import Keycache

k1 = Keycache( 
    alias='api_workers',                        # Blob namespace
    private_key='key_from_secure_message_bus',  # Encryption key
    config_path='config/my_secrets.yml' ,       # File with API Keys
    blobs_path='blobs/dir' )                    # Where to store encrypted blobs

k1.add('some_namespace' , { 'key1':'val1' , 'key2':'val2'} )
k1.save() 
```
