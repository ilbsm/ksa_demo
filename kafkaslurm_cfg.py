from os.path import expanduser, join
import faust
import socket
import os

PREFIX = os.path.dirname(__file__) # location of the project directory
LOGS_DIR = PREFIX + '/logs' # Must exist
#PYTHON_VENV = # if set overrides the default PREFIX/venv location - this is where KSA expects to find the Python Virtual Environment
#SHARED_TMP = PREFIX + '/tmp' # This folder must exist - it is used to temporary store JSON files with job input parameters
DEBUG = True

CLUSTER_NAME = 'demo_cluster' # Name of the Cluster, should reflect the name of your HPC cluster, jobs will show where they were computed
# CLUSTER_AGENT_CLASS = 'my_cluster_agent.MyClusterAgent' # (Optional) override the default class that implements the Cluster Agent

# Connection to Kafka
BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_SECURITY_PROTOCOL = 'PLAINTEXT'
#KAFKA_SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
#KAFKA_SASL_MECHANISM = 'PLAIN'
#KAFKA_USERNAME = 'demo'
#KAFKA_PASSWORD = 'pass'
#KAFKA_FAUST_BROKER_CREDENTIALS = faust.SASLCredentials(username=KAFKA_USERNAME, password=KAFKA_PASSWORD)

TOPIC_PREFIX = 'demo' # Each project should have a separate set of topics on kafka where the jobs, their statuses, results (done) and errors will be placed
TOPIC_NEW = f'{TOPIC_PREFIX}-new'
TOPIC_STATUS = f'{TOPIC_PREFIX}-jobs'
TOPIC_DONE = f'{TOPIC_PREFIX}-done'
TOPIC_ERROR = f'{TOPIC_PREFIX}-error'
TOPIC_HEARTBEAT = f'{TOPIC_PREFIX}-heartbeat'
CLUSTER_AGENT_NEW_GROUP = f'{TOPIC_PREFIX}_agent_new' # This group must be the same for all agents that should receive the jobs for the same project
MONITOR_AGENT_NEW_GROUP = socket.gethostname() + '_monitor_agent_new' # you can have multiple monitors,
# if the groups are different for them, then every one will obtain every result/status/error,
# if you set it to the same value then the results/statuses/errors will be distributed between all monitors randomly
HEARTBEAT_INTERVAL = 300.0 # in seconds, set to 0 to disable heartbeat

# Kafka advanced options
#from kafka.coordinator.assignors.range import RangePartitionAssignor
#from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor
#KAFKA_PARTITION_ASSIGNMENT_STRATEGY = [RoundRobinPartitionAssignor, RangePartitionAssignor]  # (Optional) override the way the kafka partitions are assigned


# Cluster Agent (SLURM)
#
# MONITOR_ONLY_DO_NOT_SUBMIT = True # set this to make the cluster agent only monitor existing jobs

CLUSTER_JOB_NAME_SUFFIX = '_DEMO' # All jobs on the slurm cluster will have this suffix, this is important for cluster agent to be able to identify jobs that it should manage
CLUSTER_JOB_TIMEOUT = 360000 # in seconds # default timeout for jobs, the timeout can be also specified per job in the job configuration
#POLL_INTERVAL = 20.0, # How often to poll for new jobs
SLURM_PARTITION ='all' # Name of Slurm partition to submit jobs to
# (Optional) - default job parameters, they can be set in the job configuration
# SLURM_MEM = '15gb'            # MEMORY REQUIRED FOR SLURM JOB - defaults
# SLURM_EXCLUDE = 'node1'       # Exclude some nodes from submission (optional)
# SLURM_JOB_TYPE = 'gpu'  # GPU, CPU
# SLURM_RESOURCES_REQUIRED = 1  # #OF CPUS OR GPUS PER JOB


# Worker Agent (Individual Workstations)
WORKER_NAME = 'my_worker_' + socket.gethostname()
WORKER_AGENT_CLASS = 'my_worker_agent.MyWorkerAgent' # (Optional) override the default class that implements the Worker Agent
WORKER_AGENT_MAX_WORKERS = 4
WORKER_JOB_TIMEOUT = 360000 # in seconds
WORKER_AGENT_URL = 'http://localhost:6068/'
WORKER_AGENT_CONTEXT_PATH ='/' # Worker agent context_path i.e. if set to /ctx/ the worker agent will serve at $WORKER_AGENT_URL/ctx/
#


# Monitor Agent related
MONITOR_AGENT_URL = 'http://localhost:6067/'
MONITOR_AGENT_CONTEXT_PATH ='mon/'
# MONITOR_HEARTBEAT_INTERVAL_MS = 3000
# / (Optional) The parameters below are used to run a command directly on Kafka to query for new and waiting jobs
#BOOTSTRAP_SERVERS_LOCAL = 'localhost:9092'
#KAFKA_HOME = '/opt/kafka'
# /
