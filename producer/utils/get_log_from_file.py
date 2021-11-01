import os
import sys

sys.path.append("../")
import linecache


def get_raw_log_from_HDFS_application(log_count):
    raw_log_payload = {}
    raw_log_payload["raw_LOG"] = linecache.getline(
        os.environ.get("LOG_FILE_PATH"), log_count
    )
    return raw_log_payload
