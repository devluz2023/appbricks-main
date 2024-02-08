from pydantic import BaseModel

class Notebook_task(BaseModel):
    notebook_path: str

class EmailNotifications(BaseModel):
    on_success: list
    on_failure: list

class Job(BaseModel):
    name: str
    existing_cluster_id: str | None = None
    notebook_task: Notebook_task
    email_notifications :EmailNotifications

class Task(BaseModel):
    name:str

class Scheduller(BaseModel):
    name:str

class NotebokParams(BaseModel):
    name:str
    age:str

class PythonParams(BaseModel):
    name:str
    age:str

class JarParams(BaseModel):
    name:str
    age:str 

class ExecuteJob(BaseModel):
      job_id:str
      notebook_params:NotebokParams
      jar_params:JarParams
      spark_submit_params:PythonParams
      python_params:PythonParams

