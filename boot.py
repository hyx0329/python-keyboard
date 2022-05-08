import storage

try:
    # disable usb drive
    # available in newer versions
    storage.disable_usb_drive()
except AttributeError:
    # make root read-only on boot
    storage.remount('/', 0)
