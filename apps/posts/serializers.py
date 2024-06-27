from rest_framework import serializers

from apps.posts.models import Post, PostFile

class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        fields = ('file',)

class PostSerializer(serializers.ModelSerializer):
    files = PostFileSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
    
    def validate_files(self, value):
        if not value:
            raise serializers.ValidationError("В посте должна быть хотябы одна фотография")
        return value

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        post = Post.objects.create(**validated_data)
        for file in files_data:
            PostFile.objects.create(post = post, file = file)
        return post