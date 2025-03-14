# Widths for the standard 14 fonts as described on page 416 of the PDF 1.7 standard
STANDARD_WIDTHS = {
    "Helvetica": {  # 4 fonts, includes bold, oblique and boldoblique variants
        " ": 278,
        "!": 278,
        '"': 355,
        "#": 556,
        "$": 556,
        "%": 889,
        "&": 667,
        "'": 191,
        "(": 333,
        ")": 333,
        "*": 389,
        "+": 584,
        ",": 278,
        "-": 333,
        ".": 278,
        "/": 278,
        "0": 556,
        "1": 556,
        "2": 556,
        "3": 556,
        "4": 556,
        "5": 556,
        "6": 556,
        "7": 556,
        "8": 556,
        "9": 556,
        ":": 278,
        ";": 278,
        "<": 584,
        "=": 584,
        ">": 584,
        "?": 611,
        "@": 975,
        "A": 667,
        "B": 667,
        "C": 722,
        "D": 722,
        "E": 667,
        "F": 611,
        "G": 778,
        "H": 722,
        "I": 278,
        "J": 500,
        "K": 667,
        "L": 556,
        "M": 833,
        "N": 722,
        "O": 778,
        "P": 667,
        "Q": 944,
        "R": 667,
        "S": 667,
        "T": 611,
        "U": 278,
        "V": 278,
        "W": 584,
        "X": 556,
        "Y": 556,
        "Z": 500,
        "[": 556,
        "\\": 556,
        "]": 556,
        "^": 278,
        "_": 278,
        "`": 278,
        "a": 278,
        "b": 278,
        "c": 333,
        "d": 556,
        "e": 556,
        "f": 556,
        "g": 556,
        "h": 556,
        "i": 556,
        "j": 556,
        "k": 556,
        "l": 556,
        "m": 556,
        "n": 278,
        "o": 278,
        "p": 556,
        "q": 556,
        "r": 500,
        "s": 556,
        "t": 556,
        "u": 278,
        "v": 500,
        "w": 500,
        "x": 222,
        "y": 222,
        "z": 556,
        "{": 222,
        "|": 833,
        "}": 556,
        "~": 556,
    },
    "Times": {  # 4 fonts, includes bold, oblique and boldoblique variants
        " ": 250,
        "!": 333,
        '"': 408,
        "#": 500,
        "$": 500,
        "%": 833,
        "&": 778,
        "'": 180,
        "(": 333,
        ")": 333,
        "*": 500,
        "+": 564,
        ",": 250,
        "-": 333,
        ".": 250,
        "/": 564,
        "0": 500,
        "1": 500,
        "2": 500,
        "3": 500,
        "4": 500,
        "5": 500,
        "6": 500,
        "7": 500,
        "8": 500,
        "9": 500,
        ":": 278,
        ";": 278,
        "<": 564,
        "=": 564,
        ">": 564,
        "?": 444,
        "@": 921,
        "A": 722,
        "B": 667,
        "C": 667,
        "D": 722,
        "E": 611,
        "F": 556,
        "G": 722,
        "H": 722,
        "I": 333,
        "J": 389,
        "K": 722,
        "L": 611,
        "M": 889,
        "N": 722,
        "O": 722,
        "P": 556,
        "Q": 722,
        "R": 667,
        "S": 556,
        "T": 611,
        "U": 722,
        "V": 722,
        "W": 944,
        "X": 722,
        "Y": 722,
        "Z": 611,
        "[": 333,
        "\\": 278,
        "]": 333,
        "^": 469,
        "_": 500,
        "`": 333,
        "a": 444,
        "b": 500,
        "c": 444,
        "d": 500,
        "e": 444,
        "f": 333,
        "g": 500,
        "h": 500,
        "i": 278,
        "j": 278,
        "k": 500,
        "l": 278,
        "m": 722,
        "n": 500,
        "o": 500,
        "p": 500,
        "q": 500,
        "r": 333,
        "s": 389,
        "t": 278,
        "u": 500,
        "v": 444,
        "w": 722,
        "x": 500,
        "y": 444,
        "z": 389,
        "{": 348,
        "|": 220,
        "}": 348,
        "~": 469,
    },
}

# 4 fonts, includes bold, oblique and bold oblique variants
STANDARD_WIDTHS[
    "Courier"
] = dict.fromkeys(STANDARD_WIDTHS["Times"], 600)  # fixed width
STANDARD_WIDTHS["ZapfDingbats"] = dict.fromkeys(STANDARD_WIDTHS["Times"], 1000)  # 1 font
STANDARD_WIDTHS["Symbol"] = dict.fromkeys(STANDARD_WIDTHS["Times"], 500)  # 1 font
# add aliases per table H.3 on page 1110 of the PDF 1.7 standard
STANDARD_WIDTHS["CourierNew"] = STANDARD_WIDTHS["Courier"]
STANDARD_WIDTHS["Arial"] = STANDARD_WIDTHS["Helvetica"]
STANDARD_WIDTHS["TimesNewRoman"] = STANDARD_WIDTHS["Times"]
