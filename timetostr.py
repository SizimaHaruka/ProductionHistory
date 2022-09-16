def time_to_str(sec):
    sec = int(sec + 0.5)
    h = sec // 3600
    m = (sec - h * 3600) // 60
    s = sec - h * 3600 - m * 60

    return f"{h:02}:{m:02}:{s:02}"