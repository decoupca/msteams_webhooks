from typing import Literal, NewType, Union

URL = NewType("URL", str)
Colors = Literal["default", "accent", "good", "warning", "attention", "light", "dark"]
FontTypes = Literal["default", "monospace"]
FontSizes = Literal["default", "small", "medium", "large", "extraLarge"]
FontWeights = Literal["default", "lighter", "bolder"]
HorizontalAlignmentTypes = Literal["left", "center", "right"]
VerticalAlignmentTypes = Literal["top", "center", "bottom"]
TextBlockStyles = Literal["default", "heading"]
ImageSizeTypes = Literal["auto", "stretch", "small", "medium", "large"]
ImageStyleTypes = Literal["default", "person"]
ContainerStyleTypes = Literal[
    "default", "emphasis", "good", "attention", "warning", "accent"
]
SpacingTypes = Literal[
    "default", "none", "small", "medium", "large", "extraLarge", "padding"
]
ColumnWidthTypes = Union[Literal["auto", "stretch"], str]
