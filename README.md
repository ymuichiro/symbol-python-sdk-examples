## Setup

Set up python.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a .env to the root of the project. Here is an example

```.env
PRIVATE_KEY=<your-private-key>
NODE=mikun-testnet2.tk
```

## Start Sample Script

```bash
python main.py
```

example output.

```bash
% python main.py

Enter recipient address: TARDV42KTAIZEF64EQT4NXT7K55DHWBEFIXVJQY
Enter amount: 0.1
[2023-09-17 13:47:31] [INFO    ] - Announced transaction: packet 9 was pushed to the network via /transactions (base.py:56)
[2023-09-17 13:47:52] [INFO    ] - Announce Successfule. Transaction hash is F51E5AD661E6DEB6E52B8743071F66119D5278CB6B2A3991C58F85975B97DBFD. from TAILJXZJA3JQZ5YN7DUAWS7M4K7RT7UX275PQRI to TARDV42KTAIZEF64EQT4NXT7K55DHWBEFIXVJQY (main.py:28)
```