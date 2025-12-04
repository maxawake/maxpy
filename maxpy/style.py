import matplotlib.pyplot as plt

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
plt.rcParams["font.size"] = 14

plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.alpha"] = 0.7
plt.rcParams["grid.linewidth"] = 0.5


plt.rcParams["figure.dpi"] = 150
plt.rcParams["figure.figsize"] = (6, 4)  # Default figure size

plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", ["#1982C4", "#F8A517", "#589F2B", "#FF595E", "#6A4C93"])

plt.rcParams["lines.linewidth"] = 2.0

plt.rcParams["legend.fontsize"] = 12


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
