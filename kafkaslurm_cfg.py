from os.path import expanduser, join
import faust
import socket
#from kafka.coordinator.assignors.range import RangePartitionAssignor
#from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor


#PREFIX = join(expanduser("~"), 'my_kafka_slurm')
#SHARED_TMP = PREFIX + '/tmp'
DEBUG = True
CLUSTER_NAME = 'pol_cluster'
# CLUSTER_AGENT_CLASS = 'my_cluster_agent.MyClusterAgent'
BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_SECURITY_PROTOCOL = 'PLAINTEXT'


# KAFKA_SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
# KAFKA_SASL_MECHANISM = 'PLAIN'
# KAFKA_USERNAME = 'user'
# KAFKA_PASSWORD = 'pass'
# KAFKA_FAUST_BROKER_CREDENTIALS = faust.SASLCredentials(username=KAFKA_USERNAME, password=KAFKA_PASSWORD)

#KAFKA_PARTITION_ASSIGNMENT_STRATEGY = [RoundRobinPartitionAssignor, RangePartitionAssignor]
CLUSTER_JOB_NAME_SUFFIX = '_POL'
TOPIC_NEW = 'pol-new'
TOPIC_STATUS = 'pol-jobs'
TOPIC_DONE = 'pol-done'
TOPIC_ERROR = 'pol-error'
TOPIC_HEARTBEAT = 'pol-heartbeat'
CLUSTER_AGENT_NEW_GROUP = 'pol_agent_new'
MONITOR_AGENT_NEW_GROUP = socket.gethostname() + '_monitor_agent_new'
WORKER_NAME = 'my_worker_' + socket.gethostname()
WORKER_AGENT_CLASS = 'my_worker_agent.MyWorkerAgent'
WORKER_AGENT_MAX_WORKERS = 4
WORKER_JOB_TIMEOUT = 360000 # in seconds
CLUSTER_JOB_TIMEOUT = 360000 # in seconds
HEARTBEAT_INTERVAL = 300.0 # in seconds, set to 0 to disable heartbeat
#PYTHON_VENV = # if set overrides the default PREFIX/venv location

# / The parameters below are used to run a command directly on Kafka to query for new and waiting jobs
BOOTSTRAP_SERVERS_LOCAL = 'localhost:9092'
KAFKA_HOME = '/opt/kafka'
# /

#POLL_INTERVAL = 20.0,
MONITOR_AGENT_URL = 'http://localhost:6067/'
MONITOR_AGENT_CONTEXT_PATH ='mon/'
# MONITOR_HEARTBEAT_INTERVAL_MS = 3000

SLURM_PARTITION ='long'
# SLURM_MEM = '15gb'            # MEMORY REQUIRED FOR SLURM JOB
# SLURM_EXCLUDE = 'node1'       # Exclude some nodes from submission (optional)
SLURM_JOB_TYPE = 'gpu'  # GPU, CPU
SLURM_RESOURCES_REQUIRED = 1  # #OF CPUS OR GPUS PER JOB

# MONITOR_ONLY_DO_NOT_SUBMIT = True
WORKER_AGENT_URL = 'http://localhost:6068/'
WORKER_AGENT_CONTEXT_PATH ='/'
PREFIX = '/home/pol/dev/ilbsm/ksa_demo'
LOGS_DIR = PREFIX + '/logs'
