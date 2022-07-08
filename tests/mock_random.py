def make_incrementer():
    val = [0]
    def inc():
        val[0] += 1
        return val[0]
    return inc

mock_random = make_incrementer()