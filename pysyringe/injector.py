from functools import wraps
from inspect import signature
from .container import IOCContainer


_container = IOCContainer()


def inject(**dec_kwargs):

    def _wrapper_f(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):

            function_signature = signature(f)
            ba = function_signature.bind_partial(*args, **kwargs)

            for arg_name, cls in dec_kwargs.items():
                if arg_name not in ba.arguments:
                    kwargs[arg_name] = _container.get_instance(cls)

            return f(*args, **kwargs)
        return _wrapper

    return _wrapper_f
