# Example protos
Installing gRPC:
REQ: Python 3.7 or higher
- python -m pip install --upgrade pip
- python -m pip install grpcio
- python -m pip install grpcio-tools

Build gRPC files with the following command (parent folder of /protos):
python -m grpc_tools.protoc -I./protos --python_out=./services --pyi_out=./services --grpc_python_out=./services ./protos/currencyconverter.proto

## Contents

- [currencyconverter.proto]
  - Proto for currency converter gRPC connection
