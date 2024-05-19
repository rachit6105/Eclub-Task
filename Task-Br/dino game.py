# Python code
#
c = 0
a = 0
b = 0
d = 0
basic.show_leds("""
  . . . . .
  . . . . .
  . . . . .
  # . . . .
  # . . . .
  """)

def on_forever():
  global a
  global b
  if a == 0 and b == c or a == 0 and b == d:
    basic.show_leds("""
      # # # # #
      # # # # #
      # # # # #
      # # # # #
      # # # # #
      """)
  else:
    a = 4
    b = randint(0, 4)
    led.plot(a, b)
    basic.pause(500)
    while a != 0:
      led.unplot(a, b)
      a = (a - 1)
      led.plot(a, b)
      basic.pause(500)
    led.unplot(0, b)
basic.forever(on_forever)

def on_button_pressed_a():
  global c
  global d
  basic.clear_screen()
  c = 3
  d = 4
  for index in range(3):
    led.plot(0, c)
    led.plot(0, d)
    basic.pause(100)
    led.unplot(0, d)
    c += -1
    d += -1
  led.plot(0, 0)
  basic.pause(500)
  for index2 in range(3):
    led.plot(0, c)
    led.plot(0, d)
    basic.pause(100)
    led.unplot(0, c)
    c += 1
    d += 1
  led.plot(0, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
  basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    # . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)



