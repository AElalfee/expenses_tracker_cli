from datetime import date, datetime
import calendar


def get_year(date: date):
    return datetime.strptime(date, "%Y-%m-%d").date().year


def get_month(date: date):
    return datetime.strptime(date, "%Y-%m-%d").date().month


def get_month_name(month: int) -> str:
    if 1 <= month <= 12:
        return calendar.month_name[month]
    else:
        return "Month must be between 1 and 12."


def today():
    return date.today()


def get_amount(amount: str) -> float:
    return float(amount.replace("AED ", ""))
