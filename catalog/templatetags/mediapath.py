from django import template
from django.templatetags.static import PrefixNode
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()


class MediaPathNode(PrefixNode):
    def url(self, context):
        path = self.path.resolve(context)
        return staticfiles_storage.url(path)


@register.tag('mediapath')
def do_mediapath(parser, token):
    return MediaPathNode.handle_token(parser, token)
