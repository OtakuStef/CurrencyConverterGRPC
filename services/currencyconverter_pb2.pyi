from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CurrencyReply(_message.Message):
    __slots__ = ["converted_currency"]
    CONVERTED_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    converted_currency: float
    def __init__(self, converted_currency: _Optional[float] = ...) -> None: ...

class CurrencyRequest(_message.Message):
    __slots__ = ["currency", "value"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    value: float
    def __init__(self, currency: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
