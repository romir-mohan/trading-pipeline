from pysrc.data_client import DataClient
from pysrc.model import Model
from time import sleep

client = DataClient()
model = Model()
counter = 1

while counter <= 15:
    print("Tick #: " + str(counter))

    data = client.get_data()
    model.predict(data)

    for waitCount in range(5):
        print(".", end="", flush=True)
        sleep(1)
        waitCount += 1
    print("\n")

    counter += 1
