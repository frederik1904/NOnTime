import DisplayStrategy as ds
import time

# Display adapter change this to the specific strategy to use.
x = ds.ConsoleDisplay()

for i in range(100):
    x.show_msg(f"hello: {i}")
    time.sleep(1)
