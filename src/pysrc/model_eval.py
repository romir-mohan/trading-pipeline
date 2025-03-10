from pysrc.data_client import DataClient
from pysrc.model import Model
from time import sleep

client = DataClient()
model = Model()
counter = 1

while counter <= 30:
    print("Tick #: " + str(counter))

    data = client.get_data()

    for features, midprice in data:
        model.predict((features, midprice))

    for waitCount in range(20):
        print(".", end="", flush=True)
        sleep(1)
        waitCount += 1
    print("\n")

    counter += 1
