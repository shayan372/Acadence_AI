
import streamlit as st
import pandas as pd

from database import initialize_database, add_task, get_tasks, delete_task
from priority_engine import analyze_tasks
from workload_analyzer import analyze_workload
from ai_assistant import generate_academic_recommendation


st.set_page_config(
    page_title="Acadence AI",
    page_icon="🎓",
    layout="wide"
)

initialize_database()


if "daily_hours" not in st.session_state:
    st.session_state.daily_hours = 4


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🎓 Acadence AI")

    st.caption("Academic Productivity Intelligence")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "📋 My Tasks",
            "🎯 Priority Center",
            "📊 Workload Analysis",
            "🤖 AI Assistant",
            "📈 Analytics"
        ]
    )

    st.divider()

    st.subheader("Study Capacity")

    daily_hours = st.number_input(
        "Daily study hours available",
        min_value=1.0,
        max_value=24.0,
        value=float(st.session_state.daily_hours),
        step=0.5
    )

    st.session_state.daily_hours = daily_hours


tasks = get_tasks()


# =========================================================
# OVERVIEW
# =========================================================

if page == "🏠 Overview":

    st.title("🎓 Acadence AI")
    st.subheader("Academic Overview")

    st.write(
        "Your intelligent academic command center — understand your workload, priorities, and next best action at a glance."
    )

    if tasks.empty:

        st.info(
            "No academic tasks added yet. "
            "Go to My Tasks to add your first task."
        )

    else:

        priority_results = analyze_tasks(tasks)

        priority_df = pd.DataFrame(priority_results)

        workload = analyze_workload(
            tasks,
            st.session_state.daily_hours
        )

        from datetime import date, timedelta

        upcoming_deadlines = 0

        if not tasks.empty:
            today = date.today()
            next_week = today + timedelta(days=7)

            for deadline in tasks["deadline"]:
                deadline_date = date.fromisoformat(str(deadline))

                if today <= deadline_date <= next_week:
                    upcoming_deadlines += 1

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "📚 Active Tasks",
                len(tasks[tasks["status"] != "Completed"])
            )

        with col2:
            st.metric(
                "⏰ Upcoming Deadlines",
                upcoming_deadlines
            )

        with col3:
            st.metric(
                "⏳ Remaining Work",
                f'{workload["required_hours"]} hrs'
            )

        with col4:
            st.metric(
                "📊 Workload Status",
                workload["status"]
            )

        st.divider()

        st.subheader("🎯 Recommended Next Action")

        top_task = priority_df.sort_values(
            "priority_score",
            ascending=False
        ).iloc[0]

        st.success(
            f'🤖 **Acadence AI recommends:** Focus on '
            f'**{top_task["task_name"]}** ({top_task["course"]}) '
            f'— Priority: **{top_task["priority"]}** '
            f'— Score: **{top_task["priority_score"]}**'
        )

        st.subheader("📊 Workload Snapshot")

        w1, w2, w3 = st.columns(3)

        w1.metric(
            "Required",
            f'{workload["required_hours"]} hrs'
        )

        w2.metric(
            "Available",
            f'{workload["available_hours"]} hrs'
        )

        w3.metric(
            "Capacity Difference",
            f'{workload["difference"]} hrs'
        )


        if workload["status"] == "Manageable":
            st.info(
                "💡 **AI Insight:** Your current workload is manageable. "
                "You have enough study capacity to complete your remaining work."
            )
        elif workload["status"] == "Busy":
            st.warning(
                "⚠️ **AI Insight:** Your workload is getting tight. "
                "Consider starting your highest-priority task first."
            )
        else:
            st.error(
                "🚨 **AI Insight:** Your workload is above your available capacity. "
                "Prioritize urgent tasks and review your schedule."
            )


# =========================================================
# MY TASKS
# =========================================================

elif page == "📋 My Tasks":

    st.title("My Academic Tasks")

    st.write(
        "Add assignments, exams, projects and other academic work."
    )

    with st.form("task_form"):

        task_name = st.text_input("Task Name")

        course = st.text_input("Course / Subject")

        task_type = st.selectbox(
            "Task Type",
            [
                "Assignment",
                "Exam",
                "Quiz",
                "Project",
                "Presentation",
                "Study Task"
            ]
        )

        deadline = st.date_input("Deadline")

        estimated_hours = st.number_input(
            "Estimated Hours Required",
            min_value=0.5,
            max_value=100.0,
            value=2.0,
            step=0.5
        )

        progress = st.slider(
            "Current Progress",
            0,
            100,
            0
        )

        importance = st.selectbox(
            "Importance",
            ["Low", "Medium", "High"]
        )

        status = st.selectbox(
            "Status",
            [
                "Not Started",
                "In Progress",
                "Completed"
            ]
        )

        submitted = st.form_submit_button("Add Task")

        if submitted:

            if not task_name or not course:

                st.error(
                    "Please enter both task name and course."
                )

            else:

                add_task(
                    task_name,
                    course,
                    task_type,
                    deadline,
                    estimated_hours,
                    progress,
                    importance,
                    status
                )

                st.success(
                    "Task added successfully!"
                )

                st.rerun()

    st.divider()

    st.subheader("Your Tasks")

    tasks = get_tasks()

    if tasks.empty:

        st.info("No tasks available.")

    else:

        st.dataframe(
            tasks[
                [
                    "id",
                    "task_name",
                    "course",
                    "task_type",
                    "deadline",
                    "estimated_hours",
                    "progress",
                    "importance",
                    "status"
                ]
            ],
            use_container_width=True
        )

        for _, task in tasks.iterrows():
            col1, col2 = st.columns([5, 1])

            with col1:
                st.write(
                    f"**{task['task_name']}** — {task['course']}"
                )

            with col2:
                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{task['id']}"
                ):
                    delete_task(int(task["id"]))
                    st.success("Task deleted successfully!")
                    st.rerun()


# =========================================================
# PRIORITY CENTER
# =========================================================

elif page == "🎯 Priority Center":

    st.title("Priority Center")

    st.write(
        "Acadence ranks your academic tasks based on "
        "urgency, importance, progress and workload."
    )

    if tasks.empty:

        st.info(
            "Add tasks first to generate priority intelligence."
        )

    else:

        results = analyze_tasks(tasks)

        priority_df = pd.DataFrame(results)

        priority_df = priority_df.sort_values(
            "priority_score",
            ascending=False
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Critical",
            len(
                priority_df[
                    priority_df["priority"] == "Critical"
                ]
            )
        )

        c2.metric(
            "High",
            len(
                priority_df[
                    priority_df["priority"] == "High"
                ]
            )
        )

        c3.metric(
            "Medium",
            len(
                priority_df[
                    priority_df["priority"] == "Medium"
                ]
            )
        )

        c4.metric(
            "Low",
            len(
                priority_df[
                    priority_df["priority"] == "Low"
                ]
            )
        )

        st.divider()

        st.subheader("Priority Ranking")

        st.dataframe(
            priority_df[
                [
                    "task_name",
                    "course",
                    "deadline",
                    "progress",
                    "importance",
                    "priority_score",
                    "priority"
                ]
            ],
            use_container_width=True
        )

        top_task = priority_df.iloc[0]

        st.success(
            f'### Recommended Next Task\n'
            f'**{top_task["task_name"]}** — '
            f'{top_task["course"]}\n\n'
            f'Priority level: **{top_task["priority"]}** | '
            f'Score: **{top_task["priority_score"]}**'
        )


# =========================================================
# WORKLOAD ANALYSIS
# =========================================================

elif page == "📊 Workload Analysis":

    st.title("Workload Analysis")

    st.write(
        "Analyze whether your remaining academic work "
        "fits within your available study capacity."
    )

    if tasks.empty:

        st.info(
            "Add some academic tasks first."
        )

    else:

        workload = analyze_workload(
            tasks,
            st.session_state.daily_hours
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Required Work",
            f'{workload["required_hours"]} hrs'
        )

        col2.metric(
            "Available Capacity",
            f'{workload["available_hours"]} hrs'
        )

        col3.metric(
            "Capacity Difference",
            f'{workload["difference"]} hrs'
        )

        col4.metric(
            "Status",
            workload["status"]
        )

        st.divider()

        st.subheader("Workload Interpretation")

        if workload["status"] == "Critical":

            st.error(
                "Your workload is critically high compared "
                "with your available study capacity."
            )

        elif workload["status"] == "Overloaded":

            st.warning(
                "You have more work than available study capacity."
            )

        elif workload["status"] == "Busy":

            st.warning(
                "Your workload is manageable but your "
                "available capacity is getting tight."
            )

        elif workload["status"] == "Manageable":

            st.success(
                "Your current workload appears manageable."
            )

        else:

            st.success(
                "Your tracked academic work is complete."
            )

        st.divider()

        st.subheader("Capacity Overview")

        chart_data = pd.DataFrame({
            "Category": [
                "Required Work",
                "Available Capacity"
            ],
            "Hours": [
                workload["required_hours"],
                workload["available_hours"]
            ]
        })

        st.bar_chart(
            chart_data.set_index("Category")
        )


# =========================================================
# AI ASSISTANT
# =========================================================

elif page == "🤖 AI Assistant":

    st.title("🤖 AI Academic Assistant")

    st.write(
        "Your personal academic intelligence layer — "
        "Acadence analyzes your workload, priorities, and capacity "
        "to generate practical recommendations for what to focus on next."
    )

    st.info(
        "🧠 **Powered by AI:** Acadence combines your task priorities "
        "and workload analysis to provide personalized academic guidance."
    )

    if tasks.empty:

        st.info(
            "Add academic tasks first so Acadence can "
            "generate personalized recommendations."
        )

    else:

        priority_results = analyze_tasks(tasks)

        workload = analyze_workload(
            tasks,
            st.session_state.daily_hours
        )

        recommendation = generate_academic_recommendation(
            tasks,
            workload,
            priority_results
        )

        st.subheader("🧠 Academic Intelligence")

        st.success(
            recommendation["summary"]
        )

        st.subheader("🎯 Recommended Actions")

        for index, action in enumerate(
            recommendation["actions"],
            start=1
        ):

            st.write(
                f"**{index}.** {action}"
            )

        st.divider()

        st.subheader("📌 Current Academic Situation")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Remaining Work",
            f'{workload["required_hours"]} hrs'
        )

        col2.metric(
            "Available Capacity",
            f'{workload["available_hours"]} hrs'
        )

        col3.metric(
            "Workload Status",
            workload["status"]
        )


# =========================================================
# ANALYTICS
# =========================================================

elif page == "📈 Analytics":

    st.title("Academic Analytics")

    if tasks.empty:

        st.info(
            "Add tasks to generate academic analytics."
        )

    else:

        st.subheader("Task Distribution")

        type_counts = tasks["task_type"].value_counts()

        st.bar_chart(type_counts)

        st.subheader("Progress Overview")

        progress_data = tasks[
            ["task_name", "progress"]
        ].set_index("task_name")

        st.bar_chart(progress_data)
