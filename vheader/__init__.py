import sys
import pyperclip


def main():
    output = transform_to_header(" ".join(sys.argv[1:]))
    # Copy the header to the clipboard
    print(output)
    pyperclip.copy(output)
    return


def transform_to_header(input_text) -> str:
    # Calculate the formatted output
    padding = " " * ((64 - len(input_text)) // 2)
    output = (
        "# ------------------------------------------------------------------\n"
        f"# {padding}{input_text.upper()}\n"
        "# ------------------------------------------------------------------"
    )
    return output


if __name__ == "__main__":
    main()
