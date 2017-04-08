def colorprint(text, color, bgcolor, *options):
    import os
    bef = "\x1B["
    bg = bef + bgcolorcode(bgcolor)
    cc = bef + colorcode(color)
    styles = optioncode(*options)
    end = bef + "0m"

    os.system("echo \"" + styles + bg + cc + text + end + "\"")

def optioncode(*options):
    option = ""
    alloptions = ["bold", "dim", "underline", "blink", "reverse", "hidden"]
    allcodes = ["\x1B[1m", "\x1B[2m", "\x1B[4m", "\x1B[5m", "\x1B[7m", "\x1B[8m"]
    for i in range(len(options)):
        for a in range(len(alloptions)):
            if (alloptions[a] in options[i]):
                option = option + allcodes[a]
    return option


def colorcode(color):
    colorsA = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "light gray"]
    colorsB = ["dark gray", "light red", "light green", "light yellow", "light blue", "light magenta", "light cyan", "white"]
    if color == "default":
        option = 39
    else:
        if (color in colorsA):
            option = colorsA.index(color) + 30
        elif (color in colorsB):
            option = colorsB.index(color) + 90
        else:
            option = 404
    return str(option) + "m"

def bgcolorcode(color):
    colorsA = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "light gray"]
    colorsB = ["dark gray", "light red", "light green", "light yellow", "light blue", "light magenta", "light cyan", "white"]
    if color == "default":
        option = 49
    else:
        if (color in colorsA):
            option = colorsA.index(color) + 40
        elif (color in colorsB):
            option = colorsB.index(color) + 100
        else:
            option = 404
    return str(option) + "m"

