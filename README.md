# event-hubs

Practice lab based on the tutorial and code from

https://github.com/pedrojunqueira/PytalistaYT/tree/master/Python/kafka


Notes:

1) Setup Resource group that can be deleted at the end of the test.
2) Setup Storage account. To store events in Azure blob storage. Assign role (Storage Blob Data Contributor) to Azure account if necessary and run into issues setting up topics.
3) Setup Event hub instances (topics). One hub for Azure SDK client and one for confluent-kafka.
4) Run pip install -r requirements.txt 
5) Source using source setup.sh
6) Activate virtual environment.

**Test**
**For Azure SDK client**
python producer.py 
python consumer.py

**For consluent Kakfa client**
~/../confluent$ python producer.py <topic>
~/../confluent$ python consumer.py <consumer group> <topic>
