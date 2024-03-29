## Keycache
Keycache is an AES encrypted key:value store for your sensitive credentials. It can be used for database passwords, API-keys, private certificates or anything you don't want floating around on your filesystem. The module works as both static singleton and class instance for multiple simultaneous stores.
```bash    
pip install keycache
```


<b>Basic Usage: </b> This example uses automatic defaults for all parameters. It generates an encryption key derived from a hardware identifier, a default path for blobs ( ./blobs/ ), and default name for current blob ( default )
```python
from keycache import Keycache
k1 = Keycache()
k1.add('some_namespace', { 'key1':'val1' , 'key2':'val2'} )
k1.save()
```



<b>Specific Usage: </b>
```python
k2 = Keycache( 
    alias='api_workers',                        # Blob name
    private_key='key_from_secure_message_bus',  # Encryption key
    blob_path ='blobs/dir' )                   # Where to store encrypted blobs

k2.add('some_namespace' , { 'key1':'val1' , 'key2':'val2'} )
k2.save() 
```


<b>Loading from file: </b> If you want to distribute the credentials to other machines while keeping a central configuration file on your local host you can use this method. Just ensure you keep your credentials file out of your repository and deploy directory.

```python
k3 = Keycache()
k3.load_config('path/to/config.yml')
k3.save() 
```

