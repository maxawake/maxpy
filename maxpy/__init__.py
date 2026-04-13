from .style import *


def align_cbar(ax, im, fig, label, pad=0.0, size=5, orientation="vertical"):
    from .style import align_cbar as _align_cbar

    _align_cbar(ax, im, fig, label, pad, size, orientation)
