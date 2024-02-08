import json
import os
from dotenv import load_dotenv
from databricks_cli.runs.api import RunsApi
from databricks_cli.jobs.api import JobsApi
load_dotenv()
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi
import logging
 
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

class DataBricksProp:

    @staticmethod
    def api_client(): 
      host =  os.getenv('DATABRICKS_HOST')
      token =  os.getenv('DATABRICKS_TOKEN')
      return ApiClient(
        host  = host,
        token = token )


    @staticmethod
    def to_json(cluster):
      return {
        'cluser_name' : cluster['cluster_name'],
        'cluster_id'  :  cluster['cluster_id']
      }



    def lista_cluster(self):
      api_client     = DataBricksProp.api_client()
      clusters_api   = ClusterApi(api_client)
      clusters_list  = clusters_api.list_clusters()
      return {
              'elements': [DataBricksProp.to_json(elemento) for elemento in clusters_list['clusters'] ]
          }


    def execute_job(self, job):
       api_client = DataBricksProp.api_client()
       jobs_api   = JobsApi(api_client) 
       job_id = 232059402031692
       jar_params = {
        'arg1': 'value1',
        'arg2': 'value2'
       }
       python_params = {}

       spark_submit_params = {
          'master': 'yarn',
          'deploy-mode': 'client',
          'executor-memory': '4g'
       }
       notebook_params = {
        'param1': 'value1',
        'param2': 'value2'
       }

        # run the job
       result = jobs_api.run_now(
        job_id              = job_id,
        notebook_params     = notebook_params,
        jar_params          = [],
        python_params       = None,
        spark_submit_params = None)
       return result


    def create_job(self, job):
       api_client = DataBricksProp.api_client()
       job_json = job.dict()
       jobs_api   = JobsApi(api_client) 
       result = jobs_api.create_job(job_json)
       return result



    def list_job(self):
      pass

    def schedulle(self):
      pass

    def downloadfile(self):
      pass

    def uploadfile(self):
      pass

    def downloadmultiplefile(self):
      pass


    def getexecutedjob(self):
      pass


