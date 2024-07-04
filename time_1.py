import time

x1: float = 1.8
x2: float = -1.8
y1: float = 1.8
y2: float = -1.8
c_real: float = -0.62667
c_imag: float = -0.32193


def calc_pure_python(desired_width, max_iteration):
    x_step:float = (x2-x1) / desired_width
    y_step:float = (y1-y2) / desired_width

    # debug ! #
    x:list =[]
    y:list =[]
    ycoord:float = y2
    while ycoord >y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord:float = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs:list= []
    cs:list = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("len of x: ", len(x))
    print("total: " , len(zs))

    start_time = time.time()
    output = calculate_z_serial_purepython(max_iteration, zs,cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + "took" , secs, "seconds")

    assert sum(output) == 33219980

def calculate_z_serial_purepython(maxiter:int, zs:list, cs:list)->list:
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z*z +c
            n+=1
        output[i] = n
    return output


if __name__ == "main":
    calc_pure_python(1000, 300)
