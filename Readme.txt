18-06-2024

- EC2 doesnt allow installing pandas system wide
- Environment is externally managed

- We tried using venv
- Somehow venv environment is not getting activated due to inadequate permissions on the 
activate .bash file.
- without activating venv airflow is not being identified as a module.


Solutions:

try building airflow from source at system level.
try activating venv using sudo
try updating permissions on activate.bash
try running airflow in docker---
	You may need to build the container image locally
	Could lead to less resources on a t2 micro 




19-06-2024:
Airflow:
airflow can be installed after activating venv
Login with username: admin  password: Qk8sCYmRqbvr2dzv

Connect to fresh instance 
sudo apt install python3-pip
sudo apt install python3-venv
create environments directory
create virtual env using
sudo python3 -m venv <path_to_env>

airflow can be installed after activating venv

Ensure you use the environment specific python3 and environment specific pip
<path_to_env>/bin/python3 <path_to_env>/bin/pip install pandas
airflow command works only after the environment is activated.

-To access the airflow server we need to allow all inbound traffic from all sources to ec2.
- However, when we do that we are not able to connect via ssh. I mean connection is slow.

Solutions:
try making it work the first time.
try rebooting the instance and connect to it after editing the security group.