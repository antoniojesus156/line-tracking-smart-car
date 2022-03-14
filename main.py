tracking_values = 0
basic.show_icon(IconNames.HAPPY)
strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)
strip.clear()

def on_forever():
    global tracking_values
    strip.show_rainbow(1, 360)
    tracking_values = k_Bit.line_tracking()
    if tracking_values == 1:
        k_Bit.motor(MotorObs.LEFT_SIDE, MotorDir.FORWARD, 40)
        k_Bit.motor(MotorObs.RIGHT_SIDE, MotorDir.BACK, 40)
    elif tracking_values == 2:
        k_Bit.motor(MotorObs.LEFT_SIDE, MotorDir.BACK, 40)
        k_Bit.motor(MotorObs.RIGHT_SIDE, MotorDir.FORWARD, 40)
    elif tracking_values == 3:
        k_Bit.run(DIR.RUN_FORWARD, 25)
    else:
        k_Bit.car_stop()
basic.forever(on_forever)
