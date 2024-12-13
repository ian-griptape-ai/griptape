from attrs import define, field
from schema import Schema

from griptape.artifacts import BaseArtifact
from griptape.artifacts.json_artifact import JsonArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity


@define
class StructuredOutputTool(BaseTool):
    output_schema: Schema = field(kw_only=True)

    @activity(
        config={
            "description": "The final response which ends this conversation.",
            "schema": lambda self: self.output_schema,
        }
    )
    def provide_output(self, params: dict) -> BaseArtifact:
        return JsonArtifact(params["values"])
