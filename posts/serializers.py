from rest_framework import serializers

from authentication.serializers import AccountSerializer
from posts.models import Country, Post


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country

        fields = ('id', 'name', 'short', 'logo_url')
        read_only_fields = ('id')


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)
    country = CountrySerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = ('id', 'author', 'country', 'name', 'tagline', 'votes_count',
                  'comments_count', 'redirect_url', 'discussion_url', 'day', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']
