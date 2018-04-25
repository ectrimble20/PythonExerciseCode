

# Convert a RGB value into Hex
def rgb(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(*map(lambda x: min(255, max(0, x)), [r, g, b])).upper()


def rgb_2(r, g, b):
    rnd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rnd(r), rnd(g), rnd(b))


def rgb_3(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))


def rgb_4(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))


