import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

EVENT_HUB_CONNECTION_STR = "Endpoint=sb://xxxxxxxxxxxx.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxx"
EVENT_HUB_NAME = "mytopic"

async def run():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name =EVENT_HUB_NAME
    )
    async with producer:
        event_data_batch = await   producer.create_batch()

        for i in range(100):
            event_data_batch.add(EventData(f"event {i} "))
        
        await producer.send_batch(event_data_batch)

asyncio.run(run())    
