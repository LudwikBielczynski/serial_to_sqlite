import functools

def execute_and_commit(func):

    @functools.wraps(func)
    def func_wrapper(self, *args, **kwargs):
        query = func(self, *args, **kwargs)
        self.connection.execute(query)
        self.connection.commit()

    return func_wrapper
