from datetime import datetime

events = [
    {"name": "Event 1", "date": "2023-06-10"},
    {"name": "Event 2", "date": "2024-01-15"},
    {"name": "Event 3", "date": "2022-11-05"},
    {"name": "Event 4", "date": "2023-12-20"}
]


def sort_by_date_desc(data):
    return sorted(
        data, 
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), 
        reverse=True)


sorted_events = sort_by_date_desc(events)

for p in sorted_events:
    print(p)