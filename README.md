# EpicEvents, P12
## Installation
clone the repo 
```sh
git https://github.com/raltheo/oc_p12.git
cd oc_p12
```
create new virtual environnement
```sh
py -m venv env
or
python -m venv env
or
python3 -m venv env
```
activate 
```sh
env\Scripts\activate.bat (on windows cmd)
env\Scripts\activate.ps1 (on windows powershell)
source env/bin/activate (on linux/mac)
```
install requirements
```sh
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
(for exit from virtual environnement)
```sh
deactivate
```
* * *

## Usage
### Run the app
```bash
py -m app.main
```
### Run Test
```bash
pytest .\tests\test_integration.py --cov=app
```


### Users for testing :
```sh
#(username:password)
admin@example.com:admin # administrator
support@example.com:support
commercial@example.com:commercial
gestion@example.com:gestion
```

* * *
