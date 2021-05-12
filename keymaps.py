from keyboard import *

# keymaps only define the keycode to send, and
# won't change the internal keycode

___ = TRANSPARENT
BOOT = BOOTLOADER
PWDN = SHUTDOWN
L1 = LAYER_TAP(1)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))

L2E = LAYER_TAP(2, E)
L3X = LAYER_TAP(3, X)
L5O = LAYER_TAP(5, O)

L2D = LAYER_TAP(2, D)
L3B = LAYER_TAP(3, B)
L5S = LAYER_TAP(5, S)

# TAP key
SCC = MODS_TAP(MODS(RCTRL), ';')  # Semicolon & Ctrl

# Combined
SINS = MODS_KEY(MODS(SHIFT), INSERT)

## common layer 1
kb_layer1 = (
	'`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
	MACRO(1), ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
	MACRO(2),LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___, MACRO(0),
	MACRO(3), ___, ___, ___, ___,BOOT, ___, ___, ___, ___, ___,           ___,
	MACRO(4), ___, ___,                ___,               ___, ___, ___,  ___
)

## common layer 2
kb_layer2 = (
	'`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
	___, ___, ___, ___, ___, ___,HOME,PGUP, INSERT, ___,SINS,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
	___, ___, ___, ___, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
	___, ___, ___, ___, ___, ___,PGDN,END, ___, ___, ___,           ___,
	___, ___, ___,                ___,               ___, ___, ___,  ___
)

## common layer 3
kb_layer3 = (
	BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
	RGB_MOD, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
	RGB_TOGGLE,HUE_RGB,RGB_HUE,SAT_RGB,RGB_SAT,___,___,___,___,___,___,___,___,
	___, ___, ___, ___, ___, ___, ___, ___,VAL_RGB,RGB_VAL, ___,           ___,
	___, ___, ___,                ___,               ___, ___, ___,  ___
)

kb_layer_mouse = (
	___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
	___, ___, ___, ___, ___, ___,MS_W_UP,MS_UL,MS_UP,MS_UR, ___, ___, ___, ___,
	___, ___, ___, ___, ___, ___,MS_BTN1,MS_LT,MS_DN,MS_RT,MS_BTN2, ___,      ___,
	___, ___, ___, ___, ___, ___,MS_W_DN,MS_DL,MS_DN,MS_DR, ___,           ___,
	___, ___, ___,                ___,               ___, ___, ___,  ___
)

kb_layer1_dvorak_mod = (
	'`', F11,  F7,  F5,  F3,  F1,  F9, F10,  F2,  F4,  F6,  F8, F12, DEL,
	MACRO(1), ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
	MACRO(2),LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___, MACRO(0),
	MACRO(3), ___, ___, ___, ___,BOOT, ___, ___, ___, ___, ___,           ___,
	MACRO(4), ___, ___,                ___,               ___, ___, ___,  ___
)

kb_layer2_dvorak_mod = (
	'`', F11,  F7,  F5,  F3,  F1,  F9, F10,  F2,  F4,  F6,  F8, F12, DEL,
	___, ___, ___, ___, ___, ___,HOME,PGUP, ___, ___,SINS,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
	___, ___, ___, ___, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
	___, ___, ___, ___, ___, ___,PGDN,END, ___, ___, ___,           ___,
	___, ___, ___,                ___,               ___, ___, ___,  ___
)


# Keymaps

keymap_qwerty = (
	# layer 0
	(
		ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
		TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
		CAPS,  A, L5S, L2D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
		LSFT4, Z,   X,   C,   V, L3B,   N,   M, ',', '.', '/',         RSFT4,
		LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT,  L1, RCTRL
	),

	# layer 1  # layer 2  # layer 3
	kb_layer1, kb_layer2, kb_layer3,

	# layer 4
	(
		'`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___,   S,   D, ___, ___, ___, ___, ___, ___, ';', ___,      ___,
		___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
		___, ___, ___,                ___,               ___, ___, ___,  ___
	),

	# layer 5
	kb_layer_mouse
)


keymap_qwerty_plain = (
	# layer 0
	(
		ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
		TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
		CAPS,  A,   S,   D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
		LSHIFT,Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',        RSHIFT,
		LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT,  L1, RCTRL
	),

	# layer 1
	kb_layer1
)


keymap_dvorak = (
	# layer 0
	(
		ESC, '[',   7,   5,   3,   1,   9,   0,   2,   4,   6,   8, ']', BACKSPACE,
		TAB, '/', ',', '.',   P,   Y,   F,   G,   C,   R,   L, '"', '=', '|',
		CAPS,  A, L5O, L2E,   U,   I,   D,   H,   T,   N,   S, '-',    ENTER,
		LSFT4, ';',   Q,   J,   K, L3X,   B,   M,   W,   V,   Z,       RSFT4,
		LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT,  L1, RCTRL
	),

	# layer 1  # layer 2  # layer 3
	kb_layer1, kb_layer2, kb_layer3,

	# layer 4
	(
		'`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___,   O,   E, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
		___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
		___, ___, ___,                ___,               ___, ___, ___,  ___
	),

	# layer 5
	kb_layer_mouse
)

keymap_norman = (
	# layer 0
	(
		ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
		TAB,   Q,   W,   D,   F,   K,   J,   U,   R,   L, ';', '[', ']', '|',
		CAPS,  A, L5S, L2E,   T,   G,   Y,   N,   I,   O,   H, '"',    ENTER,
		LSFT4, Z,   X,   C,   V, L3B,   P,   M, ',', '.', '/',         RSFT4,
		LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT,  L1, RCTRL
	),

	# layer 1  # layer 2  # layer 3
	kb_layer1, kb_layer2, kb_layer3,

	# layer 4
	(
		'`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
		___, ___,   S,   E, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
		___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
		___, ___, ___,                ___,               ___, ___, ___,  ___
	),

	# layer 5
	kb_layer_mouse
)