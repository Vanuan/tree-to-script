#!/usr/bin/env python3
import sys
import subprocess
from typing import List, Optional
from .serializers import BashArraySerializer
from .tree_parser import parse_tree_to_nodes, validate_tree_structure
from .command_generator import generate_commands

def generate_commands_from_tree(tree_lines: List[str]) -> List[str]:
    """
    Convert tree structure lines into shell commands.

    Args:
        tree_lines: List of strings in tree format

    Returns:
        List of shell commands (mkdir, touch) to recreate the structure
    """
    # Parse the tree structure first
    nodes = parse_tree_to_nodes(tree_lines)

    # Validate tree structure
    if not validate_tree_structure(nodes):
        raise ValueError("Invalid tree structure")

    commands = generate_commands(nodes)
    return commands

def tree_to_commands(tree_input: Optional[str] = None, serializer=BashArraySerializer()) -> None:
    """
    Read tree structure from a file or stdin and output serialized commands.

    Args:
        tree_input: Path to file containing tree structure or None to read from stdin.
        serializer: Serializer instance to format output.
    """
    if tree_input:
        # Read from file
        with open(tree_input, 'r') as f:
            lines = f.readlines()
    else:
        # Read from stdin
        lines = sys.stdin.readlines()

    commands = generate_commands_from_tree(lines)
    print(serializer.serialize(commands))

def run_commands(commands: List[str], cwd: str = None) -> None:
    """
    Execute a list of shell commands in the specified working directory.

    Args:
        commands: List of shell commands to execute.
        cwd: Working directory where commands will be executed (default: current directory).
              This must be a string (not a Path object).
    """
    for cmd in commands:
        subprocess.run(cmd, shell=True, cwd=str(cwd) if cwd else None, check=True)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [<tree_file>]")
        print("If no file is provided, input is read from stdin.")
        sys.exit(1)

    # Read from file if provided, otherwise read from stdin
    tree_file = sys.argv[1] if len(sys.argv) == 2 else None
    tree_to_commands(tree_file)
