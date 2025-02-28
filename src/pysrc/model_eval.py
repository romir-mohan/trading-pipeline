from pysrc.data_client import DataClient
from pysrc.model import Model
from time import sleep

client = DataClient()
model = Model()
counter = 1

while counter <= 30:
    print("Tick #: " + str(counter))

    data = client.get_data()
    model.predict(data)

    counter += 1
