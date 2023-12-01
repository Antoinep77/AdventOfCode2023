from datetime import datetime
from tools.fetch import pullProblem

today = datetime.today()
pullProblem(today.day)