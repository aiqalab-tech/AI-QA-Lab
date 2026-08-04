from src.planners.workflow_optimizer import optimize_execution_plan

execution_plan = [

    {"step": "Login"},

    {"step": "Login"},

    {"step": "Open Dashboard"},

    {"step": "Open Dashboard"},

    {"step": "Transfer Funds"},

    {"step": "Transfer Funds"},

    {"step": "Verify Success"}

]

optimized = optimize_execution_plan(execution_plan)

print("\nOptimized Workflow")
print("----------------------")

for step in optimized:
    print(step)