x = 0
y = 0

def on_forever():
    global x, y
    x = 4
    y = 0
    while True:
        led.plot(x, y)
        basic.pause(200)
        basic.clear_screen()
        while True:
            led.plot(3, 0)
            led.plot(4, 1)
            basic.pause(200)
            basic.clear_screen()
            while True:
                led.plot(2, 0)
                led.plot(3, 1)
                led.plot(4, 2)
                basic.pause(200)
                basic.clear_screen()
                while True:
                    led.plot(1, 0)
                    led.plot(2, 1)
                    led.plot(3, 2)
                    led.plot(4, 3)
                    basic.pause(200)
                    basic.clear_screen()
                    while True:
                        led.plot(0, 0)
                        led.plot(1, 1)
                        led.plot(2, 2)
                        led.plot(3, 3)
                        led.plot(4, 4)
                        led.plot(5, 5)
                        basic.pause(200)
                        basic.clear_screen()
                        while True:
                            led.plot(0, 1)
                            led.plot(1, 2)
                            led.plot(2, 3)
                            led.plot(3, 4)
                            basic.pause(200)
                            basic.clear_screen()
                            while True:
                                led.plot(0, 2)
                                led.plot(1, 3)
                                led.plot(2, 4)
                                basic.pause(200)
                                basic.clear_screen()
                                while True:
                                    led.plot(0, 3)
                                    led.plot(1, 4)
                                    basic.pause(200)
                                    basic.clear_screen()
                                    while True:
                                        led.plot(0, 4)
                                        basic.pause(200)
                                        basic.clear_screen()
basic.forever(on_forever)
