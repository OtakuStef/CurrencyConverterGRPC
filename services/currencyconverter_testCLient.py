# Copyright 2015 gRPC authors.
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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import currencyconverter_pb2
import currencyconverter_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to convert the currency ...")
    # with grpc.insecure_channel('localhost:8501') as channel:
    with grpc.insecure_channel('13.50.231.174:8501') as channel:
        stub = currencyconverter_pb2_grpc.CurrencyConverterStub(channel)
        response = stub.ConvertCurrency(currencyconverter_pb2.CurrencyRequest(currency="EUR", value=40))
    print("Currency Converted: " + str(response.converted_currency))


if __name__ == '__main__':
    logging.basicConfig()
    run()
