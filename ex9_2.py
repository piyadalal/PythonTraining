def frange(start, stop=None, step=0.25):
    """
    Floating-point range generator that works like range().

    If only one argument is provided, it's treated as stop, and start defaults to 0.
    """
    # Handle single argument case
    if stop is None:
        stop = float(start)
        start = 0.0
    else:
        start = float(start)
        stop = float(stop)

    step = float(step)

    # Protect against step=0
    if step == 0:
        return

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step
