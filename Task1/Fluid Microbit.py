# Python code
#
#At first I was trying to derive a matrix operation which woul dtake input as roll and pitch angles and giev out the the leds that has to 
#be lit i almost devised it but then i realised i have to implememt it in tinkercad which is a really bad software and i just went along with 
#codeblocks to do it so basically (as you can see) put forward many ifs statement for differnet angle making my microbit not fluid but pseudofluid like
# https://www.tinkercad.com/things/lz8GxSab7wW-fluid-motion

def on_forever():
  if input.rotation(Rotation.Pitch) >= 0:
    if input.rotation(Rotation.Roll) > -5 and input.rotation(Rotation.Roll) <= 5:
      basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        """)
    if input.rotation(Rotation.Roll) > 5 and input.rotation(Rotation.Roll) <= 30:
      basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . # # #
        . # # # #
        """)
    if input.rotation(Rotation.Roll) > 30 and input.rotation(Rotation.Roll) <= 70:
      basic.show_leds("""
        . . . . #
        . . . . #
        . . . # #
        . . # # #
        . . # # #
        """)
    if input.rotation(Rotation.Roll) > 70 and input.rotation(Rotation.Roll) <= 90:
      basic.show_leds("""
        . . . # #
        . . . # #
        . . . # #
        . . . # #
        . . . # #
        """)
    if input.rotation(Rotation.Roll) > -30 and input.rotation(Rotation.Roll) <= -5:
      basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        # # # . .
        # # # # .
        """)
    if input.rotation(Rotation.Roll) > -70 and input.rotation(Rotation.Roll) <= -30:
      basic.show_leds("""
        . . . . .
        # . . . .
        # # . . .
        # # # . .
        # # # . .
        """)
    if input.rotation(Rotation.Roll) > -90 and input.rotation(Rotation.Roll) <= -70:
      basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        """)
  else:
    if input.rotation(Rotation.Roll) > -5 and input.rotation(Rotation.Roll) <= 5:
      basic.show_leds("""
        . # # # .
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        """)
    if input.rotation(Rotation.Roll) > 5 and input.rotation(Rotation.Roll) <= 30:
      basic.show_leds("""
        . # # # #
        . . # # #
        . . . . #
        . . . . .
        . . . . .
        """)
    if input.rotation(Rotation.Roll) > 30 and input.rotation(Rotation.Roll) <= 70:
      basic.show_leds("""
        . . # # #
        . . # # #
        . . . # #
        . . . . #
        . . . . .
        """)
    if input.rotation(Rotation.Roll) > 70 and input.rotation(Rotation.Roll) <= 90:
      basic.show_leds("""
        . . . # #
        . . . # #
        . . . # #
        . . . # #
        . . . # #
        """)
    if input.rotation(Rotation.Roll) > -30 and input.rotation(Rotation.Roll) <= -5:
      basic.show_leds("""
        # # # # .
        # # # . .
        # . . . .
        . . . . .
        . . . . .
        """)
    if input.rotation(Rotation.Roll) > -70 and input.rotation(Rotation.Roll) <= -30:
      basic.show_leds("""
        # # # . .
        # # # . .
        # # . . .
        # . . . .
        . . . . .
        """)
    if input.rotation(Rotation.Roll) > -90 and input.rotation(Rotation.Roll) <= -70:
      basic.show_leds("""
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        # # . . .
        """)
basic.forever(on_forever)

def on_gesture_shake():
  basic.show_leds("""
    . . . . #
    . . . . .
    . . . . #
    . . # # #
    . # # # #
    """)
  basic.pause(2)
  basic.show_leds("""
    . . . . .
    . . # . .
    . . . # .
    # # # . #
    # # # # #
    """)
  basic.pause(2)
  basic.show_leds("""
    . . . . .
    # . . . .
    # # . . .
    # # . # .
    # # # # .
    """)
  basic.pause(2)
  basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    . # # # #
    """)
input.on_gesture(Gesture.Shake, on_gesture_shake)
