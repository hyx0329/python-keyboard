
import supervisor


def usb_is_connected():
    if hasattr(supervisor.runtime, 'usb_connected'):
        return supervisor.usb_connected

    @micropython.asm_thumb
    def mem(r0):
        """Read memory from the address"""
        ldr(r0, [r0, 0])
    return mem(0x40000438) == 0x3


def do_nothing(*args, **kargs):
	pass
