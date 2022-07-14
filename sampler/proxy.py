import sys

class Proxy:
    def __init__(self, proxy_from, n=1):
        self.n = n
        self.proxy_from = proxy_from

    def __getattr__(self, name):
        gen = self.__annotations__[name] 
        if isinstance(gen, Proxy):
            return gen.generate()
        else:
            return gen

    def generate(self):
        results = []
        if callable(self.n):
            n = self.n()
        else:
            n = self.n

        for nn in range(n):
            o = self.proxy_from(**dict([[field, self.__annotations__[field]()] for field in self.proxy_from.__annotations__]))
            results.append(o)
        return results

    def __call__(self):
        return self.generate()

class ExplicitProxy(Proxy):
     def __init__(self, n=1):
        cls = self.__annotations__["decorating"]
        super().__init__(cls, n)    