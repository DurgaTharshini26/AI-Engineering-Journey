import yaml


def load_test_cases(file_path):
    """
    Load test cases from a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        list: A list of test case dictionaries.

    Raises:
        FileNotFoundError: If the YAML file does not exist.
        ValueError: If the YAML format is invalid or missing 'test_cases'.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if "test_cases" not in data:
            raise ValueError("Missing 'test_cases' key in YAML file.")

        return data["test_cases"]

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")

    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format.\n{e}")