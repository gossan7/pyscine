import sys
import importlib
from typing import Dict
from types import ModuleType


REQUIRED_PACKAGES = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computations"),
    ("matplotlib.pyplot", "Visualization"),
]


def check_dependencies() -> Dict[str, ModuleType] | None:
    """
    Verify that all required third-party packages are installed
    and importable.

    This function attempts to import each package listed in
    REQUIRED_PACKAGES and reports its availability and version.
    Successfully imported modules are collected and returned.

    Returns:
        dict | None:
            - A dictionary mapping package names to imported modules
              if all dependencies are available.
            - None if one or more dependencies are missing.

    Side Effects:
        Prints status messages to stdout indicating which packages
        are available or missing.
    """
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    loaded = {}
    failed = False

    for pkg, string in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {string} ready")
            loaded[pkg] = module
        except ImportError:
            print(f"[MISSING] {pkg} is not installed")
            failed = True
    print()

    if failed:
        print("One or multiple missing packages.")
        print("Install with: pip install -r requirements.txt")
        print("Or use: poetry install\n")
    return None if failed else loaded


def analyze_data(
        pandas: ModuleType,
        numpy: ModuleType,
        matplotlib: ModuleType
) -> None:
    """
    Generate synthetic data, perform basic analysis, and
    produce a visualization.

    This function:
        - Creates a normally distributed random signal
        - Computes a rolling mean over the signal
        - Plots the raw signal and rolling mean
        - Saves the resulting plot to disk

    Args:
        pandas: The pandas module used for data manipulation.
        numpy: The numpy module used for numerical computations.
        matplotlib: The matplotlib.pyplot module used for plotting.

    Side Effects:
        Writes an image file named 'matrix_analysis.png' to the
        current working directory and prints progress messages
        to stdout.
    """
    print("Analyzing Matrix data...")

    data = numpy.random.normal(loc=0, scale=1, size=1000)
    df = pandas.DataFrame({"signal": data})

    print("Processing 1000 data points...")

    df["rolling_mean"] = df["signal"].rolling(window=50).mean()

    print("Generating visualization...\n")

    matplotlib.figure()
    matplotlib.plot(df["signal"], label="Signal")
    matplotlib.plot(df["rolling_mean"], label="Rolling Mean")
    matplotlib.legend()
    matplotlib.title("Matrix Signal Analysis")
    matplotlib.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """
    Script entry point.

    This function checks for required dependencies and, if all
    are available, runs the data analysis workflow. The program
    exits with a non-zero status code if dependencies are missing.
    """
    deps = check_dependencies()
    if deps is None:
        sys.exit(1)

    analyze_data(
        pandas=deps["pandas"],
        numpy=deps["numpy"],
        matplotlib=deps["matplotlib.pyplot"],
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
