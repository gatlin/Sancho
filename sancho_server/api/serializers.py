from rest_framework import serializers
from sancho.models import Post, ContentType, Link

class UnixEpochDateField(serializers.DateTimeField):
    '''
    Lovingly stolen from Stack Overflow:
    http://stackoverflow.com/questions/19375753/django-rest-framework-updating-time-using-epoch-time
    '''

    def to_native(self, value):
        '''
        Return epoch time for a datetime object or None
        '''
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def from_native(self, value):
        import datetime
        import time
        if value == None or value == '':
            value = time.time()
        return datetime.datetime.fromtimestamp(int(value))

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link

class PostSerializer(serializers.ModelSerializer):
    created = UnixEpochDateField()
    updated = UnixEpochDateField()

    links = LinkSerializer(many=True)

    class Meta:
        model = Post
