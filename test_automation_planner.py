from src.planners.automation_planner import create_execution_plan

execution_plan = create_execution_plan("Money Transfer")

print("\nAutomation Execution Plan")
print("---------------------------")

for item in execution_plan:
    print(item)