import falcon
from marshmallow import Schema, fields

def with_body_params(**kwargs):
    
    def decorator(func):

        def wrapper(*args):

            schema = type('schema', (Schema,) , {**kwargs})

            load = schema().load(args[1].media)

            if load.errors:
                raise falcon.HTTPError(falcon.HTTP_METHOD_NOT_ALLOWED)

            args[1].parsed = load.data

            return func(*args)
        
        return wrapper
    
    return decorator




