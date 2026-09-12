
from datetime import datetime, date


def calculate_priority(task):

    """
    Calculate a priority score for an academic task.

    Score is based on:
    - Deadline urgency
    - Importance
    - Remaining work
    - Current progress
    """

    score = 0


    # ----------------------------------------
    # 1. DEADLINE URGENCY
    # ----------------------------------------

    deadline = datetime.strptime(
        str(task["deadline"]),
        "%Y-%m-%d"
    ).date()

    today = date.today()

    days_remaining = (deadline - today).days


    if days_remaining <= 1:
        score += 40

    elif days_remaining <= 3:
        score += 30

    elif days_remaining <= 7:
        score += 20

    elif days_remaining <= 14:
        score += 10

    else:
        score += 5


    # ----------------------------------------
    # 2. IMPORTANCE
    # ----------------------------------------

    importance_scores = {
        "High": 25,
        "Medium": 15,
        "Low": 5
    }

    score += importance_scores.get(
        task["importance"],
        0
    )


    # ----------------------------------------
    # 3. REMAINING WORK
    # ----------------------------------------

    progress = task["progress"]

    remaining_percentage = 100 - progress


    if remaining_percentage >= 80:
        score += 20

    elif remaining_percentage >= 50:
        score += 15

    elif remaining_percentage >= 25:
        score += 10

    else:
        score += 5


    # ----------------------------------------
    # 4. TASK EFFORT
    # ----------------------------------------

    estimated_hours = task["estimated_hours"]


    if estimated_hours >= 10:
        score += 15

    elif estimated_hours >= 5:
        score += 10

    else:
        score += 5


    # ----------------------------------------
    # PRIORITY LEVEL
    # ----------------------------------------

    if score >= 80:
        priority = "Critical"

    elif score >= 60:
        priority = "High"

    elif score >= 40:
        priority = "Medium"

    else:
        priority = "Low"


    return score, priority


def analyze_tasks(tasks):

    """
    Analyze multiple tasks and
    return priority information.
    """

    results = []

    for _, task in tasks.iterrows():

        score, priority = calculate_priority(task)

        results.append({
            "id": task["id"],
            "task_name": task["task_name"],
            "course": task["course"],
            "deadline": task["deadline"],
            "progress": task["progress"],
            "importance": task["importance"],
            "priority_score": score,
            "priority": priority
        })


    return results
