def _get_tex_for_symbol(units, symbol):
    # Try to recover the registry TeX form first.
    # In unyt, unit registries store a LaTeX representation per symbol.
    try:
        entry = units.registry.lut[symbol]

        # Different unyt versions may store this a bit differently.
        # Commonly the TeX form is near the end of the tuple.
        for item in reversed(entry):
            if isinstance(item, str) and ("\\" in item or item.startswith(r"\rm")):
                return item
    except Exception:
        pass

    # Fallback for a few common special cases.
    special = {
        "Msun": r"M_\odot",
        "Rsun": r"R_\odot",
        "Lsun": r"L_\odot",
    }
    if symbol in special:
        return special[symbol]

    # Default fallback
    return rf"\mathrm{{{symbol}}}"


def latex_units(expr):
    units = expr.units

    parts = []

    for base, power in units.expr.as_powers_dict().items():
        symbol = str(base)
        tex = _get_tex_for_symbol(units, symbol)

        if power == 1:
            parts.append(tex)
        else:
            parts.append(rf"{tex}^{{{power}}}")

    return r"$\left(" + r"\,".join(parts) + r"\right)$"
