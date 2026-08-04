def optimize_execution_plan(execution_plan):

    optimized_plan = []

    previous_step = None

    for item in execution_plan:

        current_step = item["step"]

        if current_step != previous_step:
            optimized_plan.append(item)

        previous_step = current_step

    return optimized_plan