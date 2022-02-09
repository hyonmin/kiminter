from datetime import datetime, timedelta

dates = [(datetime.today() - timedelta(days=i)).strftime('%d-%m-%Y') for i in range(5)]

print(datetime.today() - timedelta(days=1))