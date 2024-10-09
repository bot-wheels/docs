# Docs

![Proof HTML](https://github.com/groupplants/docs/actions/workflows/proof-html.yml/badge.svg)

## How to run

### Visit our website

We're hosting our documentation online, here is the link:  
[Documentation](https://bot-wheels.github.io/docs)

### Docker

1. **Install Docker**: Ensure that Docker is installed and running on your computer. You can download it from the [official Docker website](https://www.docker.com/get-started).
2. **Run the Documentation Server**:  
   Use the following command to start the documentation server with Docker. This command mounts your current directory to the `/docs` directory in the container and starts the MkDocs server with the Material theme:

    ```bash
    docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
    ```

   **Note**: If you are using a Windows command prompt, replace `${PWD}` with `%cd%`. If you're using PowerShell, use `${PWD}`.

### Python

1. **Install Python**: Ensure that Python is installed on your computer. You can download it from the [official Python website](https://www.python.org/downloads/). It's recommended to use Python 3.6 or higher.

2. **Install Project Dependencies**:  
   Navigate to the project directory and install the required dependencies using the following command:

    ```bash
    python -m pip install -r requirements.txt
    ```

3. **Run the Documentation Server**:  
   Start the local MkDocs server using the command below. This will serve your documentation site locally and enable live reloading for changes.

    ```bash
    python -m mkdocs serve
    ```

   After running this command, you should see output indicating that the server is running, and you can view your documentation in a web browser at the address provided (typically `http://127.0.0.1:8000/`).

## Markdown Linter - markdownlint

We use [markdownlint](https://github.com/DavidAnson/markdownlint) to ensure that our Markdown files follow consistent style and quality standards.

### Why Markdownlint is Used

- **Consistency**: Markdownlint helps maintain a consistent style across all Markdown documentation files.
- **Error Prevention**: It detects common formatting issues, such as inconsistent headings, incorrect list formatting, and missing line breaks, improving the overall readability of the documentation.
- **Code Quality**: Ensuring that the Markdown follows standards makes collaboration easier and the documentation clearer.

### Merge Request Requirements

All merge requests (MRs) must pass the `markdownlint` check before they can be merged into the main branch. This ensures that:

1. All Markdown files adhere to the established style guidelines.
2. The documentation is consistently formatted and free of common errors.

Before submitting a merge request, make sure to run:

```bash
markdownlint '**/*.md'
```

The GitHub Actions pipeline will automatically run `markdownlint` during the merge process to enforce this requirement.

### How to Implement markdownlint in Your IDE

To make it easier to comply with Markdown linting rules, you can install `markdownlint` in your favorite IDE. Below are the instructions for Visual Studio Code and PyCharm:

#### Visual Studio Code

1. **Install the markdownlint Extension**:
   Open the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS) and search for `markdownlint`. Click **Install** on the extension titled "markdownlint" by David Anson.

2. **Configure markdownlint**:
   If you want to disable certain rules (like line length), create a `markdownlint.json` configuration file in the root of your project, and VSCode will automatically apply these rules.

3. **Live Linting**:
   Once installed, `markdownlint` will automatically highlight any issues in your Markdown files as you edit them in Visual Studio Code.

#### PyCharm

1. **Install markdownlint-cli**:
   PyCharm does not have a built-in Markdown linter, but you can integrate `markdownlint-cli` via the terminal.

   - Open the terminal in PyCharm and run:

     ```bash
     npm install -g markdownlint-cli
     ```

2. **Run markdownlint**:
   You can run `markdownlint` directly from the PyCharm terminal by running the following command to check your Markdown files:

   ```bash
   markdownlint '**/*.md'
   ```

3. **Configure markdownlint**:
   Add a `markdownlint.json` file to your project’s root to configure the rules that `markdownlint` follows, ensuring PyCharm respects those rules when you run the linter manually.

## Special thanks

- [flaticon.com](https://www.flaticon.com/free-icon/3d-car_10473321?term=car&page=1&position=42&origin=tag&related_id=10473321) - provided us with documentation favicon
