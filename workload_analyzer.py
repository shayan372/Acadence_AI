
from datetime import datetime, date


def calculate_remaining_hours(tasks):
    """Calculate total remaining work across all tasks."""

    total_remaining = 0

    for _, task in tasks.iterrows():

        estimated_hours = float(task["estimated_hours"])
        progress = float(task["progress"])

        remaining = estimated_hours * (1 - progress / 100)

        total_remaining += remaining

    return round(total_remaining, 2)


def calculate_available_hours(tasks, daily_hours):
    """
    Estimate available study capacity until
    the latest task deadline.
    """

    if tasks.empty:
        return 0

    deadlines = []

    for deadline in tasks["deadline"]:

        deadline_date = datetime.strptime(
            str(deadline),
            "%Y-%m-%d"
        ).date()

        deadlines.append(deadline_date)

    latest_deadline = max(deadlines)

    today = date.today()

    days_available = (latest_deadline - today).days + 1

    if days_available < 0:
        days_available = 0

    available_hours = days_available * daily_hours

    return round(available_hours, 2)


def analyze_workload(tasks, daily_hours):
    """
    Compare remaining academic work
    against available study capacity.
    """

    required_hours = calculate_remaining_hours(tasks)

    available_hours = calculate_available_hours(
        tasks,
        daily_hours
    )

    difference = round(
        available_hours - required_hours,
        2
    )


    # ----------------------------------------
    # WORKLOAD STATUS
    # ----------------------------------------

    if required_hours == 0:

        status = "Complete"

    elif available_hours == 0:

        status = "Critical"

    elif required_hours > available_hours * 1.25:

        status = "Critical"

    elif required_hours > available_hours:

        status = "Overloaded"

    elif required_hours > available_hours * 0.75:

        status = "Busy"

    else:

        status = "Manageable"


    return {
        "required_hours": required_hours,
        "available_hours": available_hours,
        "difference": difference,
        "status": status
    }
