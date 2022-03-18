# Web.py and MVC

### Install

```bash
$ pip3 install -r requirements.

Collecting web.py
  Downloading web.py-0.62.tar.gz (1000 kB)
  ...
```

### Run Webapp

```bash
$ python3 app.py

http://0.0.0.0:8080/
```

### Run Webapp with Ghunicorn

```bash
$ gunicorn --bind 0.0.0.0:8080 app:wsgiapp

[2022-02-26 22:01:24 +0000] [5573] [INFO] Starting gunicorn 20.1.0
[2022-02-26 22:01:24 +0000] [5573] [INFO] Listening at: http://0.0.0.0:8080 (5573)
[2022-02-26 22:01:24 +0000] [5573] [INFO] Using worker: sync
[2022-02-26 22:01:24 +0000] [5575] [INFO] Booting worker with pid: 5575
```

### History

1. v0.1 (Contiene la estructura base de las carpetas de una aplicación web con MVC).
2. v0.2 (Se optimizó el código y se actualizo layout.html).
3. v0.3 (Se actualizao README.md style.css y app.py).