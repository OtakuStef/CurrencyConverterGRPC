# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: currencyconverter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63urrencyconverter.proto\x12\x11\x63urrencyconverter\"2\n\x0f\x43urrencyRequest\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"+\n\rCurrencyReply\x12\x1a\n\x12\x63onverted_currency\x18\x01 \x01(\x01\x32n\n\x11\x43urrencyConverter\x12Y\n\x0f\x43onvertCurrency\x12\".currencyconverter.CurrencyRequest\x1a .currencyconverter.CurrencyReply\"\x00\x42\x39\n\x1c\x61t.fastcar.currencyconverterB\x11\x43urrencyConverterP\x01\xa2\x02\x03\x43\x43Sb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'currencyconverter_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034at.fastcar.currencyconverterB\021CurrencyConverterP\001\242\002\003CCS'
  _CURRENCYREQUEST._serialized_start=46
  _CURRENCYREQUEST._serialized_end=96
  _CURRENCYREPLY._serialized_start=98
  _CURRENCYREPLY._serialized_end=141
  _CURRENCYCONVERTER._serialized_start=143
  _CURRENCYCONVERTER._serialized_end=253
# @@protoc_insertion_point(module_scope)
