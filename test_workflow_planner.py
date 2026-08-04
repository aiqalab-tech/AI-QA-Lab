from src.planners.workflow_planner import plan_workflow

workflow = plan_workflow("Money Transfer")

print("\nWorkflow")
print("------------------")

for step in workflow:
    print(step)