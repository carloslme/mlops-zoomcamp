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
