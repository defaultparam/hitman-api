# Hitman API
- This repository contains a set of microservices, that can aid in following scenarios:
	- Challenge tracking
	- Offline mission planning
	- Others: Extend the feel of Hitman universe through a simulated puzzle game featuring easters (or something like that... Got an idea? open an issue)

> As of now, only challenge tracker is being worked upon.

ETA for challenge tracker API? Check back in Jan 2025

## Installation

Make sure you have python 3.10+ installed.

Boot into a virtual env
```bash
python3 -m venv .venv
```

Clone the repository
```bash
git clone <THIS_URL>
```

Install the dependencies
```bash
pip install fastapi[standard] # This installs some extra packages such as fastapi-cli.
```

Run the API with fastapi command line utility
```bash
fastapi dev ./challenge_tracker/main.py
```

If you would like to contribute to the project, kindly open a PR

_I will leave you to prepare ;)_
