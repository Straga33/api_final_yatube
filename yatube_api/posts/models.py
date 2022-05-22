from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст нового поста',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время публикации',
        help_text='Время публикации поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Автор поста',
    )

    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост',
    )

    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок группы',
        help_text='Заголовок новой группы',
    )
    slug = models.SlugField(
        unique=True,
        default='',
        verbose_name='Идентификатор',
        help_text='Идентификатор группы',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание группы',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемый текст',
        help_text='Текст поста для комментариев',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор поста',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Добавить комментарий:',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время публикации',
        help_text='Время публикации комментария',
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписавшийся пользователь',
        help_text='Пользователь подписки',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписка на автора',
        help_text='Автор подписки',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='detection_user_following'
            ),
        )
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
