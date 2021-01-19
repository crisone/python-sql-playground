# SQLalchemy test field

## Python dependency

For mac

```bash
pip3 install sqlalchemy
brew install postgresql
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```

## Run

首先修改 client.py 中的服务器地址，用户名，密码，数据库名

```bash
python example.py
```

## Reference

* [Using PostgreSQL through SQLAlchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)
