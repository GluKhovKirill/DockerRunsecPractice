import os


class Config:
    host = os.getenv("MYSQL_IP", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    d_name = os.getenv("MYSQL_RBPO_DATABASE", "RuncsecPractice")

