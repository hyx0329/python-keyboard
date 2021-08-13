from keyboard.action_code import *

from .default import kb_layer1_function, kb_layer2_media, kb_layer3_kbcontrol, kb_layer4_restore, kb_layer5_mouse
from .default import ___, FNL1, L2D, L3B, LSFT4, RSFT4, L5S, SCC


# layer 0
kb_layer0_base = (
	ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
	TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
	CAPS,  A, L5S, L2D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
	LSFT4, Z,   X,   C,   V, L3B,   N,   M, ',', '.', '/',         RSFT4,
	LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT, FNL1, RCTRL
)

kb_layer0_base_plain = (
	ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
	TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
	CAPS,  A,   S,   D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
	LSFT4, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         RSFT4,
	LCTRL, LALT, LGUI,          SPACE,            RGUI, RALT, FNL1, RCTRL
)


# compose up
keymap = (
	kb_layer0_base,
	kb_layer1_function,
	kb_layer2_media,
	kb_layer3_kbcontrol,
	kb_layer4_restore,
	kb_layer5_mouse
)

keymap_plain = (
	kb_layer0_base_plain,
	kb_layer1_function
)
