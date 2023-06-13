# Setup

* Create the environment

```bash
conda create -n prefect-ops python=3.9.12
conda activate prefect-ops
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Start prefect server

```bash
prefect server start
```

* Configure Prefect to communicate with the server -Open a new tab and activate the environment-

```bash
conda activate prefect-ops
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
```

# Prefect flow deployment

1. Run Prefect

    ```bash
    prefect server start
    ````

2. Go to the Prefect UI and create a Work Pool called `dev`. In the `Type` of worker to run within this work pool select `Process`.
3. In another CLI tab, change to the root directory, and run the following command to create the project:

    ```bash
    prefect project init
    ````

3. Deploy the flow using this command:

    ```bash
    prefect deploy 03-orchestration/3.4/orchestrate.py:main_flow -n taxi -p dev
    ```

    Ensure the path to the python script is correct, and you include the flow name (`main_flow` in this example)
4. Create the worker in the CLI using the following command:

    ```bash
    prefect worker start -p dev 
    ```

5. Go to the Prefect UI and run manually the deployment, in this case it was `Deployments/taxi_2`.
