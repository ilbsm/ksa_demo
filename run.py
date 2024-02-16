import sys

from topoly import  homfly

from kafka_slurm_agent.kafka_modules import ClusterComputing

class MatrixComputing(ClusterComputing):
    def __init__(self, args):
        super().__init__(args)
        self.struct_name = self.input_job_id
        print(f'JOB CONFIG: {self.job_config}')
        print('JOB TYPE: {}'.format(self.job_config['slurm_pars']['JOB_TYPE']))
        print('MY VAR: {}'.format(self.job_config['slurm_pars']['MY_VAR']))

    def get_file_name(self):
        return f'cif/AF-{self.input_job_id}-model_v1.cif'

    def do_compute(self):
        homfly_res = homfly(self.get_file_name(), max_cross=100, tries=200)
        print(homfly_res)
        self.results['homfly'] = homfly_res
        self.rs.send(self.struct_name, self.results)
        print('Sent results: {}'.format(self.results))


if __name__ == '__main__':
    MatrixComputing(sys.argv).compute()
