import storage

if hasattr(storage, "disable_usb_drive"):
    # disable usb drive
    # available in newer versions
    storage.disable_usb_drive()
