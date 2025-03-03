# TreeToScript

Welcome to **TreeToScript**, a utility for transforming directory tree structures from text into actionable shell commands or executing them directly. This tool is perfect for setting up project file structures, automating file system operations, or documenting directory layouts.

## Features

- **Tree Structure Parsing**: Converts text representations of directory structures into commands.
- **Command Generation**: Generates shell commands (`mkdir`, `touch`) to replicate the given structure.
- **Validation**: Ensures the tree structure is valid, checking for proper nesting and syntax.
- **Special Character Support**: Handles file and directory names with spaces, special characters, and Unicode.
- **Comment Support**: Ignores comments within the tree structure text.
- **Serialization**: Outputs commands in various formats like Bash arrays or YAML.
- **Command Execution**: Provides options to either generate commands or execute them directly with caution.


## Installation

### Python Requirement
Python 3.7 or higher.

### From PyPI
```bash
pip install tree-to-script
```

### From Source
```bash
git clone <repository-url>
cd tree-to-script
python setup.py install
```


## Usage

### Input Format
Your input should be a text file or `stdin` describing a directory tree:

```
project/
├── src/
│   ├── main.py
│   └── util/
│       └── helper.py
├── tests/
│   └── test_main.py
└── README.md
```


### Running TreeToScript

#### To Generate Commands:
```bash
python3 -m tree_to_script.main example_tree.txt
```

#### To Execute Commands Directly:
Add the `--no-dry` flag to run commands immediately:
```bash
python3 -m tree_to_script.main example_tree.txt --no-dry
```

#### For `stdin` Input:
```bash
echo "project/
├── src/
│   ├── main.py
└── README.md" | python3 -m tree_to_script.main --no-dry
```


### Output

By default, the output is a Bash array of commands:
```bash
commands=(
  'mkdir -p project'
  'mkdir -p project/src'
  'touch project/src/main.py'
  'mkdir -p project/src/util'
  'touch project/src/util/helper.py'
  'mkdir -p project/tests'
  'touch project/tests/test_main.py'
  'touch project/README.md'
)
```


### Serialization Formats

Choose your output format:

```bash
python3 -m tree_to_script.main example_tree.txt --serializer yaml
```

Output in YAML:
```yaml
commands:
  - mkdir -p project
  - mkdir -p project/src
  - touch project/src/main.py
  - mkdir -p project/src/util
  - touch project/src/util/helper.py
  - mkdir -p project/tests
  - touch project/tests/test_main.py
  - touch project/README.md
```


### Command Execution

**Warning**: When using `--no-dry`, commands are executed directly. Be cautious about:

- **Permissions**: Ensure you have the necessary permissions to create directories and files.
- **Environment**: Avoid running in sensitive environments where unintended changes could be harmful.
- **Error Handling**: The tool will attempt to handle errors gracefully, but always check the output for any issues.


## Debugging

Debug the parsed tree:

```python
from tree_to_script.debug import print_tree
from tree_to_script.tree_parser import parse_tree_to_nodes

nodes = parse_tree_to_nodes(tree_lines)
print_tree(nodes)
```


## Testing

### Unit Tests
```bash
python3 -m unittest tree_to_script.test_tree_parser
python3 -m unittest tree_to_script.test_complex_structure
```

### Integration Tests
```bash
python3 -m unittest tree_to_script.test_integration
```


## Examples

### Example 1: Basic Tree

**Input (`example_tree.txt`)**:
```
project/
├── src/
│   ├── main.py
│   └── util/
│       └── helper.py
```

**Command**:
```bash
python3 -m tree_to_script.main example_tree.txt
```

**Output**:
```bash
commands=(
  'mkdir -p project'
  'mkdir -p project/src'
  'touch project/src/main.py'
  'mkdir -p project/src/util'
  'touch project/src/util/helper.py'
)
```

**To Execute**:
```bash
python3 -m tree_to_script.main example_tree.txt --no-dry
```


### Example 2: Special Characters

**Input (`special_chars.txt`)**:
```
documents/
├── my report.pdf
└── notes 2023.txt
```

**Command**:
```bash
python3 -m tree_to_script.main special_chars.txt
```

**Output**:
```bash
commands=(
  'mkdir -p documents'
  "touch 'documents/my report.pdf'"
  "touch 'documents/notes 2023.txt'"
)
```

**To Execute**:
```bash
python3 -m tree_to_script.main special_chars.txt --no-dry
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Version

Current version: **0.0.0**
