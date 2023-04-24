# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import currencyconverter_pb2 as currencyconverter__pb2


class CurrencyConverterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConvertCurrency = channel.unary_unary(
                '/currencyconverter.CurrencyConverter/ConvertCurrency',
                request_serializer=currencyconverter__pb2.CurrencyRequest.SerializeToString,
                response_deserializer=currencyconverter__pb2.CurrencyReply.FromString,
                )


class CurrencyConverterServicer(object):
    """The greeting service definition.
    """

    def ConvertCurrency(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurrencyConverterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConvertCurrency': grpc.unary_unary_rpc_method_handler(
                    servicer.ConvertCurrency,
                    request_deserializer=currencyconverter__pb2.CurrencyRequest.FromString,
                    response_serializer=currencyconverter__pb2.CurrencyReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'currencyconverter.CurrencyConverter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CurrencyConverter(object):
    """The greeting service definition.
    """

    @staticmethod
    def ConvertCurrency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/currencyconverter.CurrencyConverter/ConvertCurrency',
            currencyconverter__pb2.CurrencyRequest.SerializeToString,
            currencyconverter__pb2.CurrencyReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
