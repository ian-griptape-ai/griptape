from griptape.drivers import AnthropicImageQueryDriver
from griptape.engines import ImageQueryEngine
from griptape.loaders import ImageLoader

driver = AnthropicImageQueryDriver(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
)

engine = ImageQueryEngine(
    image_query_driver=driver,
)

image_artifact = ImageLoader().load("tests/resources/mountain.png")

engine.run("Describe the weather in the image", [image_artifact])
