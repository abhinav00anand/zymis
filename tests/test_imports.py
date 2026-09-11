import importlib


def test_package_imports() -> None:
    """Ensure that core Zymis modules import without errors.

    This test imports the top-level package and a few key submodules. If any
    import raises an exception, the test will fail, surfacing regressions
    early.
    """
    # List of module paths to import
    modules = [
        "zymis",
        "zymis.agents.base.agent",
        "zymis.compiler.python",
        "zymis.bootstrap.registry",
    ]

    for module_name in modules:
        try:
            importlib.import_module(module_name)
        except Exception as exc:
            # Re-raise with a clear message for pytest output
            raise AssertionError(f"Failed to import {module_name}: {exc}") from exc
