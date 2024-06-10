# Example CPP to MD

This script automates the process of extracting C++ code examples from source files and inserting them into Markdown documentation files.

## How It Works

1. **Extract Code Examples:**
   - The script scans through all `.cpp` and `.h` files in the specified C++ folder.
   - It looks for specially marked comments indicating the start and end of code examples.
   - The format for these markers is:
     ```cpp
     // START_EXAMPLE example_name
     // END_EXAMPLE example_name
     ```
   - Multiple example names can be specified by separating them with commas:
     ```cpp
     // START_EXAMPLE example1,example2
     // END_EXAMPLE example1,example2
     ```
   - The code between each pair of start and end markers is collected and stored.

2. **Insert Code Examples into Documentation:**
   - The script scans through all `.md` files in the specified Markdown folder.
   - It looks for placeholders where code examples should be inserted, in the format:
     ```markdown
     <!-- INSERT_EXAMPLE: example_name -->
     ```
   - If a matching example is found, the placeholder is replaced with the corresponding code example, wrapped in a C++ code block:
     ````markdown
     ```cpp
     // Example code here
     ```
     ````

## Usage

1. **Prepare Your Source and Documentation Files:**
   - In your C++ source files, mark the start and end of code examples using the `START_EXAMPLE` and `END_EXAMPLE` comments.
   - In your Markdown documentation files, add placeholders where you want the code examples to be inserted.

2. **Run the Script:**
   - Ensure you have Python installed.
   - Execute the script with the paths to your C++ and Markdown folders as arguments:
    ```bash
    python3 example_cpp_to_md.py <cpp_example_dir> <md_doc_dir>
    ```
    or with Docker:
    ```bash
    docker run -v <cpp_example_dir>:/examples -v <md_doc_dir>:/docs:rw robotsix/cpp_to_md:master
    ```

## Example

### C++ Source File (`example.cpp`)
```cpp
// START_EXAMPLE: example1
int add(int a, int b) {
    return a + b;
}
// END_EXAMPLE: example1
```

### Markdown Documentation File (`docs.md`)
```markdown
# Example Documentation

Here is an example of the `add` function:

<!-- INSERT_EXAMPLE: example1 -->
```

### Resulting Markdown Documentation File (`docs.md`)
After running the script, `docs.md` will be updated to:
````markdown
# Example Documentation

Here is an example of the `add` function:

```cpp
int add(int a, int b) {
    return a + b;
}
```
````
