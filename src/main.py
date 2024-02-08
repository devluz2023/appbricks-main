from src.databricks import DataBricksProp
from src.models import Job, ExecuteJob
from fastapi import FastAPI
from databricks_cli.runs.api import RunsApi
from databricks_cli.jobs.api import JobsApi
import redis

r = redis.Redis(host="redis123", port=6379)
app = FastAPI()

# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}


@app.get("/cluster")
def lista_cluster():
    token = DataBricksProp()
    return token.lista_cluster()

@app.post("/executejob")
def executejob(job:ExecuteJob):
    databricks = DataBricksProp()
    return databricks.execute_job(job)


@app.post("/createjob")
def createjob(job: Job):
    databricks = DataBricksProp()
    return databricks.create_job(job)


@app.get("/listjob")
def listjob():
    databricks = DataBricksProp()
    return databricks.list_job()

@app.get("/schedulle")
def schedulle():
    databricks = DataBricksProp()
    return databricks.schedulle()


@app.get("/dowloadfile")
def downloadfile():
    databricks = DataBricksProp()
    return databricks.downloadfile()

@app.get("/uploadfile")
def uploadfile():
    databricks = DataBricksProp()
    return databricks.uploadfile()

@app.get("/downloadmultiplesfile")
def downloadmultiplefile():
    databricks = DataBricksProp()
    return databricks.downloadmultiplefile()

@app.get("/getexecutejobfinshed")
def getexecutejobfinshed():
     databricks = DataBricksProp()
     return databricks.getexecutedjob()