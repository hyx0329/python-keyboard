# from keyboard import *
from keyboard import Keyboard
from keymaps import keymaps
import microcontroller
import storage

keyboard = Keyboard()
log = keyboard.log

default_keymap = keymaps['qwerty_mod']
keymap_qwerty_plain = keymaps['qwerty_plain']
keymap_dvorak = keymaps['dvorak']
keymap_norman = keymaps['norman']

def macro_handler(dev, n, is_down):
	# TODO: use dictionary to register callbacks instead
	if is_down:
		log('You pressed macro #{}\n'.format(n))
		if n == 0:
			log('Switch to default layout\n')
			dev.kbd.keymap = default_keymap
			dev.kbd.setup()
		elif n == 1:
			log('Switch to Qwerty(plain) layout\n')
			dev.kbd.keymap = keymap_qwerty_plain
			dev.kbd.setup()
		elif n == 2:
			log('Switch to Dvorak layout\n')
			dev.kbd.keymap = keymap_dvorak
			dev.kbd.setup()
		elif n == 3:
			log('Switch to Norman layout\n')
			dev.kbd.keymap = keymap_norman
			dev.kbd.setup()
		else:
			pass
	else:
		log('You released macro #{}\n'.format(n))

def pairs_handler(dev, n):
	if n == 0:
		dev.kbd.log('Power-off pair key detected\n')
		microcontroller.reset()
	elif n == 1:
		dev.kbd.log('Remount storage read-write\n')
		storage.remount('/', 1)
	elif n == 2:
		log('Remount storage read-only\n')
		storage.remount('/', 0)
	else:
		dev.kbd.log('You just triggered pair keys #{}\n'.format(n))


### initialize keyboard

keyboard.keymap = default_keymap
# keyboard.profiles = dict()
keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# Pairs
# Only related to position, not keycode
keyboard.pairs = [
	{0, 40}, #0 ESC+ENTER       Poweroff
	{0, 13}, #1 ESC+BACKSPACE   Remount RW
	{0, 53}  #2 ESC+LCTRL       Remount RO
]

# ESC(0)    1(1)   2(2)   3(3)   4(4)   5(5)   6(6)   7(7)   8(8)   9(9)   0(10)  -(11)  =(12)  BACKSPACE(13)
# TAB(27)   Q(26)  W(25)  E(24)  R(23)  T(22)  Y(21)  U(20)  I(19)  O(18)  P(17)  [(16)  ](15)   \(14)
# CAPS(28)  A(29)  S(30)  D(31)  F(32)  G(33)  H(34)  J(35)  K(36)  L(37)  ;(38)  "(39)      ENTER(40)
#LSHIFT(52) Z(51)  X(50)  C(49)  V(48)  B(47)  N(46)  M(45)  ,(44)  .(43)  /(42)            RSHIFT(41)
# LCTRL(53)  LGUI(54)  LALT(55)               SPACE(56)          RALT(57)  MENU(58)  Fn(59)  RCTRL(60)

# Uncomment line below to disable serial debug output
# keyboard.verbose = False

keyboard.run()
