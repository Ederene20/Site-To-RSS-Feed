from rest_framework import serializers

from feed.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["id", "public_id", "url", "global_search_pattern", "search_pattern", "feed_title", "feed_link",
                  "feed_description", "item_title_template", "item_link_template", "item_content_template",
                  "created", "updated"]
