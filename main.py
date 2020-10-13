def on_forever():
    for y in range(5):
        for x in range(5):
            led.plot(x, y)
            basic.pause(500)
basic.forever(on_forever)
