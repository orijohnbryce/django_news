from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20, required=False)
    content = serializers.CharField(max_length=2000,  required=False)
    date = serializers.DateField(required=False)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.date = validated_data.get("date", instance.date)

        instance.save()
        return instance
