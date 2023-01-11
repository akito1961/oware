""" Necessary Utility Function For QoF"""

def int_to_text(num:int) -> str:
    if num < 10:
        return " " + str(num)
    else:
        return str(num)

