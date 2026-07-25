"""Python packaging for the Conduit message-envelope protocol.

Bundles the JSON Schema, RabbitMQ transport doc, and cross-client
conformance fixtures from this repo so Python clients can depend on
them without vendoring copies. The schema and fixtures themselves
remain the canonical, language-neutral files under schemas/ and
conformance/ at the repo root; this package just exposes them.
"""

from __future__ import annotations

from importlib import resources
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from importlib.resources.abc import Traversable


def schema_path() -> "Traversable":
    """The canonical message-envelope JSON Schema."""
    return resources.files(__package__) / "schemas" / "conduit-message.schema.json"


def conformance_fixtures_dir() -> "Traversable":
    """The directory of cross-client conformance fixtures."""
    return resources.files(__package__) / "conformance" / "fixtures"


def rabbitmq_transport_doc() -> "Traversable":
    """The RabbitMQ transport-binding documentation."""
    return resources.files(__package__) / "transports" / "rabbitmq.md"
