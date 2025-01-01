import inspect


def context_data(_func=None, *, key=None):
    def _context_data(func):
        def wrapper(self):
            return func(self, self.request)

        wrapper._is_context_data = True
        wrapper._context_key = key or func.__name__
        return wrapper

    if callable(_func):
        return _context_data(_func)
    else:
        return _context_data


class ContextDataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if getattr(method, "_is_context_data", False) is True:
                key = getattr(method, "_context_key", name)
                context[key] = method()
        return context
