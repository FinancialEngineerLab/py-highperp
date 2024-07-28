import time

@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    with profile.timestamp("create_output_list"):
        output = [0] * len(zs)
    time.sleep(1)
    with profile.timestamp("calculate_output"):
        for i in range(len(zs)):
            n = 0
            z = zs[i]
            c = cs[i]
            while n < maxiter and abs(z) < 2:
                z = z*z +c
                n += 1
            output[i] = n
    return output


def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total

def fn_terse(upper=1_000_000):
    return sum(range(upper))

assert fn_expressive() = fn_terse(), "expect identical results from both functions" # debugg


def test_some_fn():
    assert some_fn(2) == 4
    assert some_fn(1) == 1
    assert some_fn(-1) == 1

@profile
def some_fn(useful_input):
    time.sleep(1)
    return useful_input ** 2

# fake profile decorator
if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func

if __name__ == "__main__":
    print(f"some_fn(2) == {some_fn(2)}")

