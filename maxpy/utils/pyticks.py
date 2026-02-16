from fractions import Fraction as frac
import matplotlib.ticker as tck
import numpy as np


def pi_axis_formatter(val, pos, denomlim=10, pi=r"\pi"):
    """
    format label properly
    for example: 0.6666 pi --> 2π/3
               : 0      pi --> 0
               : 0.50   pi --> π/2
    """
    minus = "-" if val < 0 else ""
    val = abs(val)
    ratio = frac(val / np.pi).limit_denominator(denomlim)
    n, d = ratio.numerator, ratio.denominator

    fmt2 = "%s" % d
    if n == 0:
        fmt1 = "0"
    elif n == 1:
        fmt1 = pi
    else:
        fmt1 = r"%s%s" % (n, pi)

    fmtstring = "$" + minus + (fmt1 if d == 1 else r"{%s}/{%s}" % (fmt1, fmt2)) + "$"

    return fmtstring


def set_pi_ticks(ax, base=np.pi / 4, axis="x"):
    if axis == "x":
        ax.xaxis.set_major_formatter(tck.FuncFormatter(pi_axis_formatter))
        ax.xaxis.set_major_locator(tck.MultipleLocator(base=base))
    elif axis == "y":
        ax.yaxis.set_major_formatter(tck.FuncFormatter(pi_axis_formatter))
        ax.yaxis.set_major_locator(tck.MultipleLocator(base=base))
