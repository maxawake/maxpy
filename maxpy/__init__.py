from .style import *


def align_cbar(ax, im, fig, label, pad=0.0, orientation="vertical"):
    from .style import align_cbar as _align_cbar

    _align_cbar(ax, im, fig, label, pad, orientation)
