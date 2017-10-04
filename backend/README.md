# Who's Hungry API Server

This is the backend API server to handle Who's Hungry requests.

## API Development

Follow the steps below to start developing on the API server.

### With Docker

If you have Docker and Docker Compose installed, you can run the entire application 
using the command below.

```bash
$ make debug
```

### Without Docker

If you are not using Docker, you will need to have `virtualenv` installed.

To develop this server, clone the repo, and move into the `backend` directory.

#### Create the Virtual Environment

Create the virtual environment the Python interpreter will live in.

```bash
$ virtualenv -p python3 venv
```

You can then `source` into the virtual environment to use it.

```bash
$ source venv/bin/activate
```

Then install any dependencies that are needed.

```bash
$ pip install -r requirements.txt
```

#### Running the server

After installing the virtual environment, you can start the server using the 
command below.

```bash
$ make local
```


