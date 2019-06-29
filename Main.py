import DisplayStrategy as ds
import WeightStrategy as ws
import time

# Display adapter change this to the specific strategy to use.
display = ds.ConsoleDisplay()
weight = ws.FakeWeight(display)

weight.initialize_weights()
