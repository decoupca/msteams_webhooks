"""msteams_webhooks.types."""
from typing import Literal, Union

Colors = Literal["default", "accent", "good", "warning", "attention", "light", "dark"]
ColumnWidthTypes = Union[Literal["auto", "stretch"], str]
ContainerStyleTypes = Literal["default", "emphasis", "good", "attention", "warning", "accent"]
FontSizes = Literal["default", "small", "medium", "large", "extraLarge"]
FontTypes = Literal["default", "monospace"]
FontWeights = Literal["default", "lighter", "bolder"]
HorizontalAlignmentTypes = Literal["left", "center", "right"]
ImageSizeTypes = Literal["auto", "stretch", "small", "medium", "large"]
ImageStyleTypes = Literal["default", "person"]
SpacingTypes = Literal["default", "none", "small", "medium", "large", "extraLarge", "padding"]
TextBlockStyles = Literal["default", "heading"]
VerticalAlignmentTypes = Literal["top", "center", "bottom"]
