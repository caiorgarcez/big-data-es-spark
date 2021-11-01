import sys
from random import choices, randint
from string import ascii_letters, digits

sys.path.append("../")
account_chars: str = digits + ascii_letters
from logparser.logparser import Spell

input_dir = "log/"  # The input directory of log file

output_dir = "spell_output/"  # The output directory of parsing results
log_file = "HDFS_2k.log"  # The input log file name
log_format = "<Date> <Time> <Pid> <Level> <Component>: <Content>"  # HDFS log format
tau = 0.5  # Message type threshold (default: 0.5)
regex = []  # Regular expression list for optional preprocessing (default: [])

parser = Spell.LogParser(
    indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex
)
parser.parse(log_file)


# def get_logs_from_file(file_path):
#     with open(file_path, "rb") as log_file:
#         logs = log_file.read()


# def _random_account_id() -> str:
#     """Return a random account number made of 12 characters."""
#     return "".join(choices(account_chars, k=12))


# def _random_amount() -> float:
#     """Return a random amount between 1.00 and 1000.00."""
#     return randint(100, 100000) / 100


# def create_random_transaction() -> dict:
#     """Create a fake, randomised transaction."""
#     return {
#         "source": _random_account_id(),
#         "target": _random_account_id(),
#         "amount": _random_amount(),
#         # Keep it simple: it's all euros
#         "currency": "EUR",
#     }
