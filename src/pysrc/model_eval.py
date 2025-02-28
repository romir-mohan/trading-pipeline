import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from pysrc.data_client import DataClient
from pysrc.model import Model
from time import sleep

client = DataClient()
model = Model()
counter = 1

while counter <= 75:
    print("Tick #: " + str(counter))

    data = client.tick()
    model.predict(data)

    for waitCount in range(60):
        print(".", end="", flush=True)
        sleep(1)
        waitCount += 1
    print("\n")

    counter += 1
