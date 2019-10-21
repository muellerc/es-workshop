from datetime import datetime, timedelta

last_hours = datetime.now() + timedelta(hours=-1)
path = '_snapshot/logs-xyz-index-snapshot-repo/' + last_hours.strftime("%Y-%m-%d-%H") 

print(path)