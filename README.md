# Kafka-Slurm-Agent Demo project

This project demonstrates how to use the [kafka-slurm-agent](https://github.com/prubach/kafka-slurm-agent) distributed streaming engine.

In this example this engine is used to run the knot detection software [topoly](https://topoly.cent.uw.edu.pl/) to detect 
knots using the *homfly* polynomial on protein structures downloaded from the [AlphaFold database](https://alphafold.ebi.ac.uk/).

## Installation

Use the standard ``pip`` tool to install. The recommended way is to use a Python virtual environment:

``python3 -m venv venv``
``source venv/bin/activate``
``pip install -r requirements.txt``

## Running the demo

### Kafka

For development and testing I recommend using Kafka in Docker. At the moment only Kafka 3.x is supported (Kafka 4.x won't work due to the lack of support in aiokafka used by faust-streaming).
You can use the provided script:

``./run_kafka_docker.sh``

### Configuration

Please adjust the config file.
1. Modify the configuration of the connection to **Apache Kafka**. The default one assumes that kafka is running on *localhost* and default port (*9092*) and doesn't use authentication or SSL.
     In the comments you will find parameters necessary to connect to **Kafka** configured using SASL and plaintext password. If you use this type of connection please uncomment also the line that starts with:
``# KAFKA_FAUST_BROKER_CREDENTIALS``
2. Make sure that ``PREFIX`` points to the location of your project
3. Change the names of topics used for your project to avoid any conflict with projects sharing the same kafka instance.
4. If you want to use a SLURM cluster please change the job ``CLUSTER_JOB_NAME_SUFFIX = '_KSA'`` to avoid conflicts with other projects running on your slurm cluster. The jobs managed by **cluster-agent** will be named *"JOBID_SUFFIX"* where the JOBID is the identifier that you assign when submitting a job and SUFFIX is handled by this configuration parameter.

### Run

1. Open a new terminal and start the **worker-agent** (``./start_worker_agent``). You can also run it in the background using ``./worker_agent start``.
2. Open a new terminal and start the **monitor-agent** (``./start_monitor_agent``). You can also run it in the background using ``./monitor_agent start``.
3. Submit new jobs using the ``submitter.py``
4. While the submitted jobs are running you can monitor the statuses at: http://localhost:6067/mon/stats/ on the host on which you've started the **monitor-agent**.
5. The output should be visible on the console of the **monitor-agent**.
