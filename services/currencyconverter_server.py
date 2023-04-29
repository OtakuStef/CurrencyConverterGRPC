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
"""The Python implementation of the gRPC Currency Converter server."""

from concurrent import futures
import logging

import grpc
import currencyconverter_pb2
import currencyconverter_pb2_grpc
import currencyConversion


def calculate(request):
    return currencyConversion.convertCurrency("USD", request.value, request.currency)


class CurrencyConverter(currencyconverter_pb2_grpc.CurrencyConverterServicer):

    def ConvertCurrency(self, request, context):
        return currencyconverter_pb2.CurrencyReply(converted_currency=calculate(request))


def serve():
    port = '8501'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    currencyconverter_pb2_grpc.add_CurrencyConverterServicer_to_server(CurrencyConverter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
