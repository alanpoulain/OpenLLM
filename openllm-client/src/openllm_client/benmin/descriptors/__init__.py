"""'openllm_client.benmin.descriptors' holds a minimal implementation of some IO Descriptors protocol.

Note that not all IO Descriptor is supported. It currently only contains IO Descriptor implementation that OpenLLM uses."""
from __future__ import annotations
import typing as t
class OpenApiSpec(t.TypedDict):
  id: str
  args: t.Dict[str, t.Any]
_supported: dict[str, t.Any] = {'bentoml.io.JSON': 'json', 'bentoml.io.Text': 'text'}
def from_spec(spec: dict[str, t.Any]):
  ...
