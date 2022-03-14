let tracking_values = 0
basic.showIcon(IconNames.Happy)
let strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)
strip.clear()
basic.forever(function () {
    strip.showRainbow(1, 360)
    tracking_values = k_Bit.LineTracking()
    if (tracking_values == 1) {
        k_Bit.Motor(MotorObs.LeftSide, MotorDir.Forward, 40)
        k_Bit.Motor(MotorObs.RightSide, MotorDir.Back, 40)
    } else if (tracking_values == 2) {
        k_Bit.Motor(MotorObs.LeftSide, MotorDir.Back, 40)
        k_Bit.Motor(MotorObs.RightSide, MotorDir.Forward, 40)
    } else if (tracking_values == 3) {
        k_Bit.run(DIR.RunForward, 25)
    } else {
        k_Bit.carStop()
    }
})
