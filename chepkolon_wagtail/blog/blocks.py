from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class CustomImageChooserBlock(ImageChooserBlock):
    pass

class ImageText(blocks.StructBlock):
    reverse = blocks.BooleanBlock(required=False)
    text = blocks.RichTextBlock()
    image = CustomImageChooserBlock()

class BodyBlock(blocks.StreamBlock):
    h1 = blocks.CharBlock()
    h2 = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image_text = ImageText()
    image_carousel = blocks.ListBlock(CustomImageChooserBlock())
    thumbnail_gallery = blocks.ListBlock(CustomImageChooserBlock())