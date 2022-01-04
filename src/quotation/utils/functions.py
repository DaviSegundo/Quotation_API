from datetime import datetime, timedelta

def working_days(days: int):
    dates = []
    today = datetime.utcnow()

    for i in range(days):
        day = today - timedelta(days=i)
        day = day.date()
        dates.append(day)

    for idx, date in enumerate(dates):
        if date.weekday() == 6:
            for i in range(idx, len(dates)):
                dates[i] = dates[i] - timedelta(days=2)
        if date.weekday() == 5:
            for i in range(idx, len(dates)):
                dates[i] = dates[i] - timedelta(days=1)

    return dates

if __name__ == '__main__':
    print(working_days(12))
