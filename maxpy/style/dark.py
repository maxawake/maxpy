import matplotlib as mpl

dark = "#1e1e2e"  # background
fg = "#e0e0e0"  # foreground text and lines
grid = "#787878"


mpl.rcParams.update(
    {
        # Figure and axes backgrounds
        "figure.facecolor": dark,
        "axes.facecolor": dark,
        # Save background
        "savefig.facecolor": dark,
        # Spines, ticks, labels
        "axes.edgecolor": fg,
        "axes.labelcolor": fg,
        "xtick.color": fg,
        "ytick.color": fg,
        "text.color": fg,
        # Grid
        "axes.grid": True,
        "grid.color": grid,
        "grid.alpha": 0.4,
        "grid.linestyle": ":",
        # Legend
        "legend.facecolor": dark,
        "legend.edgecolor": fg,
    }
)
