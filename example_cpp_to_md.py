# Copyright 2024 Damien SIX (damien@robotsix.net)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys


def extract_code_examples(cpp_folder):
    examples = {}
    example_pattern = re.compile(r'// (START_EXAMPLE|END_EXAMPLE) ([\w,]+)')

    for root, _, files in os.walk(cpp_folder):
        for file in files:
            if file.endswith('.cpp') or file.endswith('.h'):
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()

                current_examples = set()
                for line in lines:
                    match = example_pattern.match(line.strip())
                    if match:
                        tag, example_names = match.groups()
                        example_names = example_names.split(',')
                        if tag == 'START_EXAMPLE':
                            current_examples.update(example_names)
                            for example_name in example_names:
                                if example_name not in examples:
                                    examples[example_name] = []
                            continue
                        elif tag == 'END_EXAMPLE':
                            for example_name in example_names:
                                if example_name in current_examples:
                                    current_examples.remove(example_name)
                            continue
                    for example_name in current_examples:
                        examples[example_name].append(line)
    return examples


def insert_code_into_docs(md_folder, examples):
    insert_pattern = re.compile(r'<!-- INSERT_EXAMPLE: (\w+) -->')

    for root, _, files in os.walk(md_folder):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()

                matches = insert_pattern.findall(content)
                for example_name in matches:
                    if example_name in examples:
                        example_code = ''.join(examples[example_name])
                        content = content.replace(
                            f'<!-- INSERT_EXAMPLE: {example_name} -->', f'```cpp\n{example_code}\n```')

                with open(os.path.join(root, file), 'w') as f:
                    f.write(content)


def main(cpp_folder, md_folder):
    examples = extract_code_examples(cpp_folder)
    insert_code_into_docs(md_folder, examples)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_cpp_folder> <path_to_md_folder>")
        sys.exit(1)

    cpp_folder = sys.argv[1]
    md_folder = sys.argv[2]
    main(cpp_folder, md_folder)
