from home.rmohan.intern-project.src.pysrc.data_client import DataClient
from home.rmohan.intern-project.src.pysrc.model import Model
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
