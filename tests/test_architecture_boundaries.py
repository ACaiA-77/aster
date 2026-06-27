from pathlib import Path


def test_core_modules_stay_below_entropy_budget():
    root = Path(__file__).resolve().parents[1]
    budgets = {
        "aster/core/runtime.py": 950,
        "aster/core/runtime_events.py": 90,
        "aster/core/runtime_consumers.py": 90,
        "aster/core/artifacts.py": 130,
        "aster/core/task_state.py": 140,
        "aster/core/todo_ledger.py": 120,
        "aster/core/worker_manager.py": 220,
        "aster/core/context_manager.py": 420,
        "aster/core/context_usage.py": 120,
        "aster/core/compact.py": 180,
        "aster/core/engine.py": 470,
        "aster/core/model_errors.py": 100,
        "aster/core/permissions.py": 140,
        "aster/core/tool_policy.py": 90,
        "aster/core/plan_mode.py": 140,
        "aster/core/tool_executor.py": 181,
        "aster/core/tool_profiles.py": 80,
        "aster/core/turn_history.py": 250,
        "aster/features/skills.py": 220,
        "aster/features/skills_bundled.py": 120,
        "aster/features/skills_runtime.py": 140,
        "aster/tools/registry.py": 360,
        "aster/tools/todos.py": 80,
        "aster/tools/agents.py": 90,
    }

    for relative_path, max_lines in budgets.items():
        line_count = len((root / relative_path).read_text(encoding="utf-8").splitlines())
        assert line_count <= max_lines, f"{relative_path} has {line_count} lines, budget is {max_lines}"
