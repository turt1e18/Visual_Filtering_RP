# decimal 색상표를 RGB로 변환
def decimal2RGB(decimal=int) :
    red, green, blue = (decimal // 256 // 256 % 256,
                        decimal // 256 % 256,
                        decimal % 256)
    return red, green, blue

# decimal 색상표를 RGB로 변환
def RGB2decimal(red=int, green=int, blue=int) :
    decimal = (red*(256)**2 + green*256 + blue)
    return decimal