#
import numpy as np
import time
import cudf
from dask_cuda import LocalCUDACluster
import dask_cudf as dd
from dask.distributed import Client, progress, wait
import utils as bigdf
from distributed.scheduler import logger
import socket
from time import sleep

if __name__ == '__main__' :


    filename=bigdf.get_filename()
    print(f" input file= {filename}")

    print('Launching CUDA Cluster')
    cluster = LocalCUDACluster() # rmm_pool_size = '28GiB')
    client = Client(cluster)
    print(client)
    host = client.run_on_scheduler(socket.gethostname)
    port = client.scheduler_info()['services']['dashboard']
    login_node_address = "login.leonardo.cineca.it" # Provide address/domain of login node
    print(f"ssh -N -L {port}:{host}:{port} {login_node_address}",flush=True)
    sleep(30)


    t1=time.time()
    print("Reading csv into dask dataframe")
    ddf=bigdf.read_csv("dask_cudf",filename)
    ddf.persist()
    t2="{:.4f}".format(time.time()-t1)
    print(f"Time taken for dask df read {t2}")
    t1=time.time()
    print(ddf.describe(datetime_is_numeric=True).compute())
    t2="{:.4f}".format(time.time()-t1)
    print(f"Time taken for dask df describe {t2}")
