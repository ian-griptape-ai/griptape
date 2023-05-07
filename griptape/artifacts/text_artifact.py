import json
from attr import define, field
from griptape.artifacts import BaseArtifact
from griptape.tokenizers import BaseTokenizer


@define(frozen=True)
class TextArtifact(BaseArtifact):
    value: str = field()

    def token_count(self, tokenizer: BaseTokenizer) -> int:
        return tokenizer.token_count(self.value)

    def to_text(self) -> str:
        return self.value

    def __str__(self):
        from griptape.schemas import TextArtifactSchema

        return json.dumps(TextArtifactSchema().dump(self))