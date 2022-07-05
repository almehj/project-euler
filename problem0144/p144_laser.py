#!/usr/bin/env python
import math
from math import cos, acos, sqrt


# ellipse = 4x^2 + y^2 = 100


def normalize(v):
    mag = sqrt(sum([x ** 2 for x in v]))
    return tuple([x / mag for x in v])


def dot_product(a, b):
    return sum([x * y for (x, y) in zip(a, b)])


def vec_sum(v1, v2):
    return tuple([x1 + x2 for (x1, x2) in zip(v1, v2)])


def vec_diff(v1, v2):
    return tuple([x1 - x2 for (x1, x2) in zip(v1, v2)])


def scale_vec(v, constant):
    return tuple([constant * x for x in v])


def convert_to_unit_circle(v):
    """Hard wired for this problem to map from 4x^2 + y^2 = 100"""
    return v[0] / 5, v[1] / 10


def find_next(x0, v, eps):
    x1 = vec_sum(x0, scale_vec(v, .01))
    r = sqrt(dot_product(x1,x1))
    if r > 1:
        v = scale_vec(v,-1)

    k = 2
    dk = 1
    x1 = vec_sum(x0, scale_vec(v, k))
    diff = dot_product(x1, x1) - 1
    while abs(diff) > eps:
        if (diff > 0 and dk > 0) or \
                (diff < 0 and dk < 0):
            dk = -dk / 2
        k += dk
        x1 = vec_sum(x0, scale_vec(v, k))
        diff = dot_product(x1, x1) - 1

    return x1


def main():
    x0 = convert_to_unit_circle((0, 10.1))
    x1 = convert_to_unit_circle((1.4, -9.6))

    n = 0
    while True:
        print(x1[0], x1[1])

        incident_uvec = normalize(vec_diff(x1, x0))
        radius_uvec = normalize(x1)
        normal_uvec = (-radius_uvec[1], radius_uvec[0])

        proj_para = scale_vec(normal_uvec, dot_product(normal_uvec, incident_uvec))
        proj_perp = vec_diff(incident_uvec, proj_para)

        out_uvec = vec_diff(proj_perp, proj_para)
        check_dp = dot_product(out_uvec, out_uvec)

        x0 = x1
        x1 = find_next(x1, out_uvec, 1.e-6)

        n += 1

        if x1[1] > 0 and abs(x1[0]) < (.01/5):
            print(x1[0], x1[1])
            break

    print(n)


if __name__ == "__main__":
    main()
