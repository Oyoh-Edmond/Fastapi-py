Install Fastiapi packages

``
pip install fastapi[all]
``

To view all the packages installed

``
pip freeze
``

Create a <name.py> file your directory and import fastiapi 

>For more info, Check out [FastiApi Documentation](https://fastapi.tiangolo.com/tutorial/first-steps/)

To start your app
``
uvicorn <name-of-file>:<name-of-instance>
``

# What i learnt
### Post request
> Import body library

How to send data to the body using postman then extract that data within the path operations.

## Schema
>from pydantic import BaseModel 
