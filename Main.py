import DisplayStrategy as ds
import time
# Display adapter change this to the specific strategy to use.
x = ds.LCDDisplay()

for i in range(100):
    x.show_msg("hello: " + i)
    time.sleep(1)