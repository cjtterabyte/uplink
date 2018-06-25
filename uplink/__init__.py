# Local imports
from uplink.__about__ import __version__
from uplink._extras import install, load_entry_points as _load_entry_points
from uplink import accepts, content_type, returns, types
from uplink.clients import AiohttpClient, RequestsClient, TwistedClient

# todo: remove this in v1.0.0
from uplink.converters import MarshmallowConverter

from uplink.builder import build, Consumer
from uplink.commands import get, head, put, post, patch, delete
from uplink.exceptions import (
    Error,
    UplinkBuilderError,
    InvalidRequestDefinition,
    AnnotationError,
)
from uplink.decorators import (
    headers,
    params,
    form_url_encoded,
    multipart,
    json,
    timeout,
    args,
    response_handler,
    error_handler,
    inject,
)
from uplink.models import loads, dumps
from uplink.arguments import (
    Path,
    Query,
    QueryMap,
    Header,
    HeaderMap,
    Field,
    FieldMap,
    Part,
    PartMap,
    Body,
    Url,
)

__all__ = [
    "__version__",
    "install",
    "returns",
    "types",
    "accepts",
    "content_type",
    "AiohttpClient",
    "RequestsClient",
    "TwistedClient",
    "MarshmallowConverter",
    "build",
    "Consumer",
    "get",
    "head",
    "put",
    "post",
    "patch",
    "delete",
    "Error",
    "UplinkBuilderError",
    "InvalidRequestDefinition",
    "AnnotationError",
    "headers",
    "params",
    "form_url_encoded",
    "multipart",
    "json",
    "timeout",
    "args",
    "response_handler",
    "error_handler",
    "inject",
    "loads",
    "dumps",
    "Path",
    "Query",
    "QueryMap",
    "Header",
    "HeaderMap",
    "Field",
    "FieldMap",
    "Part",
    "PartMap",
    "Body",
    "Url",
]

_load_entry_points()
