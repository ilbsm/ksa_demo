import sys

from topoly import  homfly

from kafka_slurm_agent.kafka_modules import ClusterComputing

class MatrixComputing(ClusterComputing):
    def __init__(self, args):
        super().__init__(args)
        self.struct_name = self.input_job_id
        print(f'JOB CONFIG: {self.job_config}')

    def get_file_name(self):
        if '/' in self.input_job_id:
            self.organism = self.input_job_id.split('/')[0]
            p_id = self.input_job_id.split('/')[1]
            return self.organism + '/AF-{}-model_v1.cif'.format(p_id)
        else:
            return 'AF-{}-model_v1.cif'.format(self.input_job_id)

    def do_compute(self):
        homfly_res = homfly(self.get_file_name(), max_cross=100, tries=200)
        print(homfly_res)
        self.results['homfly'] = homfly_res
        self.rs.send(self.struct_name, self.results)
        print('Sent results: {}'.format(self.results))


if __name__ == '__main__':
    MatrixComputing(sys.argv).compute()
