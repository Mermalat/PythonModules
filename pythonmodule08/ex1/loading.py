import importlib
import importlib.metadata
import importlib.util
import sys


REQUIRED_PACKAGES: dict[str, str] = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
}


def get_version(package_name: str) -> str:
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def is_package_available(package_name: str) -> bool:
    if importlib.util.find_spec(package_name) is None:
        return False
    return True


def load_required_modules() -> dict[str, object]:
    try:
        modules: dict[str, object] = {
            "numpy": importlib.import_module("numpy"),
            "pandas": importlib.import_module("pandas"),
            "matplotlib": importlib.import_module("matplotlib"),
        }
        return modules
    except ImportError:
        return {}


def check_dependencies() -> list[str]:
    missing_packages: list[str] = []

    print("Checking dependencies:")
    for package_name, description in REQUIRED_PACKAGES.items():
        if not is_package_available(package_name):
            print(f"[MISSING] {package_name} - {description}")
            missing_packages.append(package_name)
            continue
        version = get_version(package_name)
        print(f"[OK] {package_name} ({version}) - {description}")

    return missing_packages


def show_dependency_instructions(missing_packages: list[str]) -> None:
    print("Missing dependencies detected:")
    for package_name in missing_packages:
        print(f"- {package_name}")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Install with Poetry:")
    print("poetry install")
    print("Then run this program again.")


def show_package_manager_comparison() -> None:
    print("Dependency management comparison:")
    print("pip uses requirements.txt for a flat dependency list.")
    print("Poetry uses pyproject.toml to manage metadata and lock files.")


def simulate_matrix_data(numpy_module: object) -> dict[str, object]:
    random_module = getattr(numpy_module, "random")
    random_generator = random_module.default_rng(seed=101)
    signal = random_generator.normal(loc=50.0, scale=12.0, size=1000)
    anomaly = random_generator.integers(low=0, high=2, size=1000)
    latency = signal + (anomaly * random_generator.normal(18.0, 4.0, 1000))
    data: dict[str, object] = {
        "signal_strength": signal,
        "anomaly_flag": anomaly,
        "latency_ms": latency,
    }
    return data


def analyze_data(modules: dict[str, object]) -> None:
    numpy_module = modules["numpy"]
    pandas_module = modules["pandas"]
    pyplot = importlib.import_module("matplotlib.pyplot")

    print("Analyzing Matrix data...")
    data = simulate_matrix_data(numpy_module)
    dataframe_constructor = getattr(pandas_module, "DataFrame")
    dataframe = dataframe_constructor(data)

    print(f"Processing {len(dataframe)} data points...")
    summary = dataframe[["signal_strength", "latency_ms"]].mean()
    print(f"Average signal strength: {summary['signal_strength']:.2f}")
    print(f"Average latency: {summary['latency_ms']:.2f} ms")

    print("Generating visualization...")
    figure, axis = pyplot.subplots(figsize=(8, 5))
    axis.scatter(
        dataframe["signal_strength"],
        dataframe["latency_ms"],
        c=dataframe["anomaly_flag"],
        cmap="coolwarm",
        alpha=0.7,
        edgecolors="none",
    )
    axis.set_title("Matrix Signal Analysis")
    axis.set_xlabel("Signal Strength")
    axis.set_ylabel("Latency (ms)")
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    pyplot.close(figure)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    missing_packages = check_dependencies()

    show_package_manager_comparison()
    if missing_packages:
        show_dependency_instructions(missing_packages)
        sys.exit(1)

    try:
        modules = load_required_modules()
        if not modules:
            print("Dependencies changed while loading modules.")
            sys.exit(1)
        analyze_data(modules)
    except Exception as error:
        print(f"Analysis interrupted safely: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
