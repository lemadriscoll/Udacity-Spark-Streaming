import producer_server


def run_kafka_server():
    input_file = "police-department-calls-for-service.json"

    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="sf.police.calls",
        bootstrap_servers="localhost:9092",
        client_id="SF_Police_Calls_Server",
    )
    if producer.bootstrap_connected():
        print("Bootstrap Connected!")

    return producer


def feed():
    producer = run_kafka_server()

    try:
        producer.generate_data()
    except:
        print("Exception!")
        producer.counter=0
        producer.flush()
        producer.close()

if __name__ == "__main__":
    feed()