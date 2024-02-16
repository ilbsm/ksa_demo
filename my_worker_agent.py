from kafka_slurm_agent.kafka_modules import WorkerAgent

class MyWorkerAgent(WorkerAgent):
	def __init__(self):
		super().__init__()
		self.script_name = 'run.py'
		self.job_name_suffix = '_MYJOBS'

	def get_job_name(self, input_job_id):
		return str(input_job_id) + self.job_name_suffix
