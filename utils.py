from datetime import date, datetime


def get_year(date: date):
    return datetime.strptime(date, "%Y-%m-%d").date().year


def get_month(date: date):
    return datetime.strptime(date, "%Y-%m-%d").date().month


def today():
    return date.today()


def get_amount(amount: str) -> float:
    return float(amount.replace("AED ", ""))
