from collections import Counter
import datetime
import re
import typing


class ArticleField:
    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type

    def __repr__(self):
        return '<{} descriptor with field_type={}>'\
            .format(self.__class__.__name__, self.field_type)

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.field_type):
            raise TypeError\
                (f"expected an instance of type '{self.field_type.__name__}'"
                 f" for attribute '{self.name}',"
                 f" got '{type(value).__name__}' instead")
        if self.name == 'content':
            instance._last_edited = datetime.datetime.now()
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)


class Article:
    _id = 0

    title = ArticleField(str)
    author = ArticleField(str)
    publication_date = ArticleField(datetime.datetime)
    content = ArticleField(str)

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self._id = Article._id
        Article._id += 1
        self._last_edited = None

    @property
    def id(self):
        return self._id

    @property
    def last_edited(self):
        return self._last_edited

    def __repr__(self):
        return "<Article title=\"{}\" author='{}' publication_date='{}'>"\
            .format(self.title, self.author, self.publication_date.isoformat())

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    @staticmethod
    def _validate_integer(value, str_repr):
        if not isinstance(value, int):
            raise TypeError\
                (f"Expected an instance of type 'int' for '{str_repr}',"
                 f" got '{type(value).__name__}' instead")
        if value <= 0:
            raise ValueError(f"{str_repr} must be greater than 0")

    def short_introduction(self, n_characters):
        Article._validate_integer(n_characters, 'n_characters')
        for i in range(n_characters + 1)[::-1]:
            if self.content[i] in (' ', '\n'):
                return self.content[:i]

    def most_common_words(self, n_words):
        Article._validate_integer(n_words, 'n_words')
        content = re.findall(r'\w+', self.content.lower())
        return dict(Counter(content).most_common(n_words))
