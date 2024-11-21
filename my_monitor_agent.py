from kafka_slurm_agent.monitor_agent import app, job_status, done_topic

#TODO Put your monitor agent code here


@app.agent(done_topic)
async def process_done(stream):
	async for msg in stream.events():
		print('Got {}: {}'.format(msg.key.decode('utf-8'), msg.value))
