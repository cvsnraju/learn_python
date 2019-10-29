class G:
    def __init__(self,s):
        self.s = s
    def __getattr__(self, t):
        return G(self.s + '.org')
    def __rmatmul__(self, other):
        return other + '*' + self.s
fun, games = 'operator', G('tricks')
print(fun@games.com)

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)