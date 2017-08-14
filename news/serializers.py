from rest_framework import serializers
from django.contrib.auth.models import User, Group
from news.models import Article
from django.contrib.auth.hashers import make_password

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name', )


class UserArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = (
            'url',
            'name')

# First Version (Problem with adding user to group. New group was created everytime)
'''
class UserSerializer(serializers.ModelSerializer):
    articles = UserArticleSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'password',
            'articles',
            'groups',
            )
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        password = make_password(validated_data['password']),
    )   
        group_id = validated_data['groups']
        print("Group: "+str(group_id[0]))
        print("Type: "+str(type(group_id[0])))
        group = Group.objects.get(name = str(group_id[0]))
        group.user_set.add(user)
        user.save()
        return user
'''

# Second Version. Everything works fine
class ReadUserSerializer(serializers.ModelSerializer):
    articles = UserArticleSerializer(many=True, read_only=True)
    #groups = serializers.SlugRelatedField(queryset = Group.objects.all(), many = False, slug_field='name')
    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'password',
            'articles',
            'groups',
            )
        extra_kwargs = {'password': {'write_only': True},}

class UserSerializer(serializers.ModelSerializer):
    articles = UserArticleSerializer(many=True, read_only=True)
    groups = serializers.SlugRelatedField(queryset = Group.objects.all(), many = True, slug_field='name')
    def from_native(self, data, files):
        data['groups'] = data['groups']['id']
        return serializers.ModelSerializer.from_native(self, data, files)

    def to_native(self, obj):
        return ReadUserSerializer(obj).data

    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'password',
            'articles',
            'groups',
            )
        extra_kwargs = {'password': {'write_only': True},}

       

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        depth = 4
        fields = ('url', 'pk', 'owner', 'name', 'content', 'created')

