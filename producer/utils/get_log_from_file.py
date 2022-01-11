import linecache
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../settings/.env.local")
load_dotenv(dotenv_path)

def get_raw_log_from_HDFS_application(log_count):
    raw_log_payload = dict()
    raw_log_payload["raw"] = linecache.getline(
        os.environ.get("LOG_FILE_PATH"), log_count
    )
    return raw_log_payload
