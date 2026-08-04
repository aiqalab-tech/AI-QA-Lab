from src.planners.workflow_planner import plan_workflow

def create_execution_plan(feature):

    workflow = plan_workflow(feature)

    execution_plan = []

    for step in workflow:

        execution_plan.append({
            "step": step,
            "status": "pending",
            "automation": True
        })

    return execution_plan