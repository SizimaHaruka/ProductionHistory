
def sumcheck(data):
    length = len(data)
    sumdata = 0
    for c in data[0:length-3]:
        sumdata += c
    sumdata = sumdata % 0x100
    if sumdata == data[length-3]:
        return 1
    else:
        return 0