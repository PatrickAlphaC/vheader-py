import sys
import pyperclip


def main():
    # Collect input arguments and join them into a single string
    input_text = " ".join(sys.argv[1:])

    # Calculate the formatted output
    padding = " " * ((64 - len(input_text)) // 2)
    output = (
        "# ------------------------------------------------------------------\n"
        f"# {padding}{input_text.upper()}\n"
        "# ------------------------------------------------------------------"
    )

    # Print the header to the console
    print(output)

    # Copy the header to the clipboard
    pyperclip.copy(output)


if __name__ == "__main__":
    main()
