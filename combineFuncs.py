def combineFuncs(self, *funcs):
    def combinedFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedFunc
