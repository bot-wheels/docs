# Rocket-learn setup

## Installing Redis on Windows

### 1. Install Windows Subsystem for Linux (WSL) from PowerShell

```powershell
wsl --install
```

### 2. From Start, search for _Turn Windows features on or off_ and then select _Windows Subsystem for Linux_

### 3. Once installed, you can run bash on Ubuntu by typing _bash_ from a Windows Command Prompt, then you can install recent stable versions of Redis from the official packages.redis.io APT repository

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
sudo apt-get install make
sudo apt-get install gcc
```

### 4. After installation, start the Redis server

```bash
sudo systemctl start redis-server
```

Then test if it's running with:

```bash
$ redis-cli
$ 127.0.0.1:6379> SET foo bar
OK
$ 127.0.0.1:6379> GET foo
"bar"
```

You can also check if the server is running in the background with:

```bash
ps aux | grep redis
```

and you should see something like this:

```bash
redis      26030  3.5  0.2 141256 16216 ?        Ssl  14:43   0:00 /usr/bin/redis-server 127.0.0.1:6379
```

To shut down server type:

```bash
sudo systemctl stop redis-server
```

## Safety measures

In order to use Redis safely we need to set up it properly
and apply appropriate countermeasures. Firstly, we will turn off
redis-server autostart on system startup with:

```bash
sudo update-rc.d redis-server disable
```

Secondly, we will block the port that Redis is using with a firewall.
By default, that port is 6379 (the port number was displayed next to the IP address
while we were testing if the redis-server was running).

### 1. Install ufw

```bash
sudo apt-get install ufw
```

### 2. Allow local access (typically 127.0.0.1) to Redis and block external access to port 6379

```bash
sudo ufw deny 6379
sudo ufw allow from 127.0.0.1 to any port 6379
```

### 3. Enable or reload ufw (if necessary)

Enable it with:

```bash
sudo ufw enable
```

If ufw was already enabled, you can reload it to apply the new rules:

```bash
sudo ufw reload
```

### 4. Check the firewall status

```bash
sudo ufw status
```

You should see something like this:

```bash
Status: active

To                         Action      From
--                         ------      ----
6379                       ALLOW       127.0.0.1
6379                       DENY        Anywhere
6379 (v6)                  DENY        Anywhere (v6)
```

Lastly, we will configure Redis to require a password before allowing any client to execute commands.

### 1. Locate the Redis Configuration File

```bash
sudo find / -name "redis.conf" 2>/dev/null
```

you should see something like:

```bash
/etc/redis/redis.conf
```

### 2. Edit the Configuration File

```bash
sudo nano /etc/redis/redis.conf
```

### 3. Find the following line in the configuration file

```bash
# requirepass foobared
```

### 4. Uncomment it (by removing the # at the beginning) and change the password "foobared" to your desired password

### 5. Save and exit the file (in Nano, you can press Ctrl+X, then Y, and then Enter)

### 6. Restart the Redis server to apply the changes

```bash
sudo systemctl restart redis-server
```

### 7. You can test if this works

```bash
$ redis-cli
127.0.0.1:6379> ping
(error) NOAUTH Authentication required.
127.0.0.1:6379> AUTH Mystrongpassword
OK
127.0.0.1:6379> ping
PONG
```

## Using Redis in the project

In the project directory alongside this documentation, there also should be 2 files called
"learner-botwheels-example.py" and "worker-bothweels-example.py". Those two examples were taken from
the rocket-learn repository and modified, so they could be used as tests to see if the setup works correctly.
In order to use them, you need to create a Wandb account and use your credentials in the "learner_botwheels-example.py" in lines:

```python
wandb.login(key="Your wandb API key goes here")
logger = wandb.init(project="demo", entity="Your wandb username goes here")
```

Then, in both files you need to insert your Redis password in line:

```python
redis = Redis(host='localhost', password="Your Redis server password goes here", port=6379)
```

Lastly, if it isn't already inside the project directory, you can clone rocket-learn repo with:

```cmd
git clone https://github.com/Rolv-Arild/rocket-learn.git
```

The two files need to be located in the same directory as the rocket-learn. </br>
Start up, in order:

- the Redis server
- the Learner
- the Workers
