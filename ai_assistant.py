import os
from groq import Groq


def generate_academic_recommendation(tasks, workload, priority_results):

    if tasks.empty:
        return {
            "summary": "No academic tasks have been added yet.",
            "actions": [
                "Add your academic tasks first.",
                "Enter realistic estimated hours.",
                "Update your task progress regularly."
            ]
        }

    top_task = sorted(
        priority_results,
        key=lambda x: x["priority_score"],
        reverse=True
    )[0]

    try:
        client = Groq(api_key=os.environ["GROQ_API_KEY"])

        prompt = f"""
You are Acadence AI, an academic productivity assistant.

Student tasks:
{tasks.to_dict(orient="records")}

Workload:
{workload}

Priority analysis:
{priority_results}

Give the student practical advice.

Return exactly:

SUMMARY: one short sentence

ACTION 1: practical action
ACTION 2: practical action
ACTION 3: practical action
"""

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        text = response.choices[0].message.content

        lines = text.split("\n")

        summary = ""
        actions = []

        for line in lines:

            if line.startswith("SUMMARY:"):
                summary = line.replace("SUMMARY:", "").strip()

            elif line.startswith("ACTION"):
                action = line.split(":", 1)[1].strip()
                actions.append(action)

        return {
            "summary": summary,
            "actions": actions[:3]
        }

    except Exception as e:
        print("GROQ ERROR:", e)

        return {
            "summary": f"Your highest-priority task is '{top_task['task_name']}'.",
            "actions": [
                f"Focus on '{top_task['task_name']}' first.",
                f"Your current workload status is {workload['status']}.",
                "Keep updating your task progress."
            ]
        }