from styler import mutable_print
from time import sleep

mutable = mutable_print(".")

sleep(0.5)
mutable("..")

sleep(0.5)
mutable("...")

sleep(0.5)
mutable("Done!\n")