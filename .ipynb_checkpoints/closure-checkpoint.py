def make_inc():
    val = [0]
    def inc():
        val[0] += 1
        return val[0]
    return inc

grr = make_inc()
print(grr())
print(grr())
print(grr())