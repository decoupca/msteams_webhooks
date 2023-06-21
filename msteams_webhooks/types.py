from typing import Literal, NewType

URL = NewType("URL", str)
Colors = Literal["default", "accent", "good", "warning", "attention", "light", "dark"]
FontTypes = Literal["default", "monospace"]
FontSizes = Literal["default", "small", "medium", "large", "extraLarge"]
FontWeights = Literal["default", "lighter", "bolder"]
HorizontalAlignmentTypes = Literal["left", "center", "right"]
TextBlockStyles = Literal["default", "heading"]
ImageSizeTypes = Literal["auto", "stretch", "small", "medium", "large"]
ImageStyleTypes = Literal["default", "person"]
