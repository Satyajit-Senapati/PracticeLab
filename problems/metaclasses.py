"""metaclasses.py

Problem Statement:
Implement a Python module that demonstrates metaclass usage, showing how
classes can customize class creation and enforce constraints on subclasses.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: metaclasses, type creation, class construction, custom
behaviors, validation, advanced object model
Real-world Use Case: Enforcing interface contracts, registering plugin
implementations, object-relational mapping, and framework-level class
customization.
Input Description: Classes accept type definitions and attribute values for
subclass creation.
Output Description: The module returns classes and instances whose creation is
influenced by metaclass constraints and registration.
Example Inputs and Outputs:
    MyPlugin().run() -> "MyPlugin executed"
    PluginRegistryMeta.plugins -> ['MyPlugin', 'AnotherPlugin']
Constraints: Use metaclasses sparingly, keep metaclass behavior clear, and
avoid excessive complexity in class creation.
Brute Force Approach: Use manual registration and runtime validation.
Optimized Approach: Use metaclasses to enforce constraints at class creation
time.
Time Complexity: O(1) for class creation logic, O(n) for registry enumeration.
Space Complexity: O(n) for registered plugin lists.
Step-by-step Dry Run:
    class MyPlugin(BasePlugin): ...
    registry records MyPlugin name
    return plugin instance
Edge Cases: invalid subclass definitions, duplicate registration, and missing
required methods.
Common Mistakes: confusing metaclass responsibilities, using metaclasses for
simple cases, and failing to call super() in metaclass methods.
Follow-up Interview Questions:
    1. What is a metaclass in Python?
    2. When should you use a metaclass instead of a decorator?
    3. How does Python determine a class's metaclass?
Alternative Approaches: Use class decorators, explicit registration methods,
or mixins for shared behavior.
Expected Output: The script prints plugin registration and demonstrates
metaclass enforcement.
Key Takeaways: Metaclasses allow powerful customization of class creation but
should be used intentionally for framework-level behaviors.
"""

from __future__ import annotations

from typing import Dict, List, Type


class PluginRegistryMeta(type):
    """Metaclass that registers plugin subclasses and enforces required methods."""

    plugins: List[str] = []

    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: Dict[str, object]) -> type:
        if name != "BasePlugin" and "run" not in namespace:
            raise TypeError("Plugin subclasses must implement a run() method")

        cls = super().__new__(mcs, name, bases, namespace)
        if name != "BasePlugin":
            mcs.plugins.append(name)
        return cls


class BasePlugin(metaclass=PluginRegistryMeta):
    """Base class for plugin implementations."""

    def run(self) -> str:
        raise NotImplementedError("Plugin subclasses must implement run()")


class MyPlugin(BasePlugin):
    """A valid plugin implementation that registers automatically."""

    def run(self) -> str:
        return "MyPlugin executed"


class AnotherPlugin(BasePlugin):
    """Another valid plugin implementation."""

    def run(self) -> str:
        return "AnotherPlugin executed"


def main() -> None:
    """Main function demonstrating metaclass-based plugin registration."""
    plugin_instance = MyPlugin()
    another_instance = AnotherPlugin()
    registered_plugins = PluginRegistryMeta.plugins

    print("Plugin run result:", plugin_instance.run())
    print("Another plugin run result:", another_instance.run())
    print("Registered plugins:", registered_plugins)


if __name__ == "__main__":
    main()
