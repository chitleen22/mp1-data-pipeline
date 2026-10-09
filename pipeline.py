from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)
import argparse
import logging
import sys

logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", required=True,
                        help="Path to input file")
    parser.add_argument("--output", "-o", required=True,
                        help="Path to output file")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose logging")
    parser.add_argument("--config", required=True,
                        help="Path to config YAML file")
    return parser.parse_args()


def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(
        f"Arguments parsed: input={args.input}, output={args.output}, config={args.config}")

    if not validate_input(args.input):
        sys.exit(1)

    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    validation = config.get("validation", {})
    required_columns = validation.get("required_columns", [])
    numeric_columns = validation.get("numeric_columns", [])

    try:
        validated_data = validate_dataframe(
            data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)

    logger.info(
        f"Validation complete: {len(data)} -> {len(validated_data)} rows")

    original_data = validated_data.copy()

    try:
        processed_data = process_data(validated_data, config)
    except ValueError:
        sys.exit(1)

    logger.info(
        f"Processing complete: {len(original_data)} -> {len(processed_data)} rows")

    output_path = save_data(processed_data, args.output)
    logger.info(f"Saved cleaned data to {output_path}")

    report = create_cleaning_report(original_data, processed_data)
    print("Cleaning report:")
    print(report)


if __name__ == "__main__":
    main()
