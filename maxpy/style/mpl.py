from fractions import Fraction as frac

import cmasher
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

CMAP = plt.get_cmap("cmr.lavender")
CMAP_DIV = plt.get_cmap("cmr.redshift")


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


def default_style():
    print("Applying default Matplotlib style...")
    plt.rcParams["text.usetex"] = True

    plt.rcParams["text.latex.preamble"] = r"""
    \usepackage{lmodern}
    \usepackage[T1]{fontenc}
    \usepackage{mathptmx}      % Times (serif)
    \usepackage{amsmath}       % Math packages
    \usepackage{bm}            % Bold math
    """

    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = ["Computer Modern Roman"]
    plt.rcParams["font.size"] = 12

    plt.rcParams["grid.linestyle"] = "--"
    plt.rcParams["grid.alpha"] = 0.7
    plt.rcParams["grid.linewidth"] = 0.5

    # plt.rcParams["figure.dpi"] = 150
    plt.rcParams["figure.figsize"] = (6, 4)  # Default figure size

    # plt.rcParams["xtick.major.size"] = 20
    # plt.rcParams["ytick.major.size"] = 20
    # plt.rcParams["xtick.minor.size"] = 10
    # plt.rcParams["ytick.minor.size"] = 10
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["xtick.minor.width"] = 1.0
    plt.rcParams["ytick.minor.width"] = 1.0

    plt.rcParams["axes.linewidth"] = 1.5
    plt.rcParams["axes.prop_cycle"] = plt.cycler("color", ["#1982C4", "#F8A517", "#589F2B", "#FF595E", "#6A4C93"])

    plt.rcParams["lines.linewidth"] = 2.0

    plt.rcParams["legend.fontsize"] = 12

    plt.margins(0)


def dark_mode(background="#1e1e2e", fg="#e0e0e0", grid="#787878"):
    plt.rcParams["figure.facecolor"] = background
    plt.rcParams["axes.facecolor"] = background
    plt.rcParams["savefig.facecolor"] = background
    plt.rcParams["axes.edgecolor"] = fg
    plt.rcParams["axes.labelcolor"] = fg
    plt.rcParams["xtick.color"] = fg
    plt.rcParams["ytick.color"] = fg
    plt.rcParams["text.color"] = fg
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = grid
    plt.rcParams["grid.alpha"] = 0.4
    plt.rcParams["grid.linestyle"] = ":"
    plt.rcParams["legend.facecolor"] = background
    plt.rcParams["legend.edgecolor"] = fg


def disable_latex():
    plt.rcParams["text.usetex"] = False
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
    plt.rcParams["font.size"] = 12


def align_cbar(ax, im, fig, label, pad=0.0, orientation="vertical"):
    divider = make_axes_locatable(ax)
    place = "top" if orientation == "horizontal" else "right"
    cax = divider.append_axes(place, size="5%", pad=pad)
    fig.colorbar(im, cax=cax, label=label, orientation=orientation)


if __name__ == "__main__":
    # Test the style by creating a sample plot
    import numpy as np

    xlin = np.linspace(-1, 1, 100)
    plt.plot(xlin, np.sinh(xlin), label="sinh(x)")
    plt.plot(xlin, np.sin(xlin), label="sin(x)")
    plt.plot(xlin, xlin**2, label="$x^2$")
    plt.plot(xlin, xlin**3, label="$x^3$")
    plt.plot(xlin, 1 / (1 + xlin**2), label=r"$\frac{1}{1+x^2}$")
    plt.grid()
    plt.legend()
    plt.xlabel("$x$ in $\\Omega$")
    plt.ylabel("$f(x) \\in \\int_0^\\infty \\xi\\cdot\\mathrm{{d}}A$")
    plt.title("Various Mathematical Functions")
    plt.show()

    x, y = np.meshgrid(xlin, xlin)
    z = np.sinh(np.sqrt(x**2 + y**2))
    plt.contourf(x, y, z, levels=50, cmap=CMAP)
    plt.colorbar(label="$\\sinh(\\sqrt{x^2 + y^2})$")
    plt.xlabel("$x$ in $\\Omega$")
    plt.ylabel("$y$ in $\\Omega$")
    plt.title("Contour Plot of $\\sinh(\\sqrt{x^2 + y^2})$")
    plt.show()
