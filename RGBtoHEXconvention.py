def rgb(r, g, b):
    r, g, b = list(map(lambda x: '00' if x < 0 else ('FF'if x > 255 else (hex(x)[2:].upper() if len(hex(x)[2:]) >= 2 else '0' + hex(x)[2:].upper())), [r,g,b]))
    return r + g + b