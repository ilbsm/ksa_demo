from kafka_slurm_agent.kafka_modules import JobSubmitter

js = JobSubmitter()
prots = ['E9Q4N7-F1', 'E9Q7C4-F1', 'E9Q842-F1', 'E9Q9R9-F1', 'Q15149-F7', 'Q15149-F8', 'Q15149-F9']

# check (default: True) - don't submit if was already computed
# ignore_error_status (default: False) - don't submit if previously generated an error
#results = js.send('12324', 'run.py', {'RESOURCES_REQUIRED': 1, 'JOB_TYPE': 'gpu'})
results = js.send_many(prots, 'run.py', {'RESOURCES_REQUIRED': 1, 'JOB_TYPE': 'cpu', 'MY_VAR': 500}, ignore_error_status=True,  check=False)
print(results)