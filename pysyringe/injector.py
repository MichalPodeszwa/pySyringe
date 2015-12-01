from functools import wraps
from inspect import signature
from .container import IOCContainer


_container = IOCContainer()


def _get_filled_arguments(func, *args, **kwargs):
    function_signature = signature(func)
    ba = function_signature.bind_partial(*args, **kwargs)

    return ba.arguments



def inject(**dec_kwargs):

    def _wrapper_f(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):

            filled_arguments = _get_filled_arguments(f, *args, **kwargs)

            for arg_name, cls in dec_kwargs.items():
                if arg_name not in filled_arguments:
                    kwargs[arg_name] = _container.get_instance(cls)

            return f(*args, **kwargs)
        return _wrapper

    return _wrapper_f


def inject_value(**dec_kwargs):

    def _wrapper_f(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):

            filled_arguments = _get_filled_arguments(f, *args, **kwargs)

            for arg_name, val in dec_kwargs.items():
                if arg_name not in filled_arguments:
                    kwargs[arg_name] = val

            return f(*args, **kwargs)
        return _wrapper

    return _wrapper_f
