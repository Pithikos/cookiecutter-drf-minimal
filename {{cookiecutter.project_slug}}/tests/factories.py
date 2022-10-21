from pytest_factoryboy import register
import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


@register
class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda x: faker.user_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    class Meta:
        model = 'authentication.User'