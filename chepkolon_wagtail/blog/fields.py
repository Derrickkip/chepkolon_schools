from rest_framework import serializers

class TagField(serializers.Field):
    def to_representation(self, tags):
        try:
            return [{"name": tag.name, "slug": tag.slug, "id": tag.id} for tag in tags.all()]
        except Exception:
            return []