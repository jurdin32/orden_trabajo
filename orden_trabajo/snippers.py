from django.http import HttpResponse
from django.template.loader import get_template
from six import BytesIO
from xhtml2pdf import pisa
import os

from orden_trabajo import settings


def Attr(cls):
    model= cls.__name__
    return cls.__doc__.replace(model,"").replace("(","").replace(")","").replace(" ","").split(",")

def fetch_resources(uri, rel):
    path = os.path.join(settings.STATICFILES_DIRS, uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("utf8")),result)
    return HttpResponse(result.getvalue(),content_type="application/pdf")
