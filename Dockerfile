FROM python:3.9.19-alpine
COPY example_cpp_to_md.py .
CMD python3 example_cpp_to_md.py examples docs