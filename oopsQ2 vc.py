class vowels:
    def _init_(self,n):
        self.n=n
    def check(self):
        l=['a','e','i','o','u']
        for x in self.n:
            if x in l == l:
                print(x,'is vowel.')
            else:
                print(x,'is consonant.')
v=vowels('elephant')
v.check()