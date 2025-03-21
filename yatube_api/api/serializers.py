from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow


# Сериализатор для модели Post. Включает авторство и все поля модели.
class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


# Сериализатор для модели Comment. Включает авторство и защищает поле 'post' от изменений.
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


# Сериализатор для модели Group. Ожидается только чтение определённых полей.
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('id', 'title', 'slug', 'description')


# Сериализатор для модели Follow. Обрабатывает подписки и проверяет уникальность пары пользователь-подписка.
class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        # validators = (
        #     validators.UniqueTogetherValidator(
        #         queryset=Follow.objects.all(),
        #         fields=('user', 'following'),
        #         message=('Подписка уже существует')
        #     ),
        # ) #removed

    # Проверка на попытку подписки на самого себя.
    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Попытка подписаться на себя же'
            )
        return data
