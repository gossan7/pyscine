import sys
import importlib


REQUIRED_PACKAGES = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computations"),
    ("matplotlib.pyplot", "Visualization"),
]


def check_dependencies():
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


def analyze_data(pandas, numpy, matplotlib):
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


def main():
    deps = check_dependencies()
    if deps is None:
        sys.exit(1)

    analyze_data(
        pandas=deps["pandas"],
        numpy=deps["numpy"],
        matplotlib=deps["matplotlib.pyplot"],
    )


if __name__ == "__main__":
    main()
