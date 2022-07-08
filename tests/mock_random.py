def make_cycler():
    val = [-1]

    def inc():
        if val[0] == 9:
            val[0] = -1
        val[0] += 1
        return val[0]
    return inc


cycler_0_9 = make_cycler()
