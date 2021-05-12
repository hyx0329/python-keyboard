import storage

# make root read-only on boot
storage.remount('/', 0)