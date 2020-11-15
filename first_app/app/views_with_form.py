from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, SimpleFormView
from flask_babel import lazy_gettext as _

from . import appbuilder, db


from .forms import MyForm


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = "This is my first form view"
    message = "My form was submitted"

    def form_get(self, form):
        form.field1.data = "This was prefilled"

    def form_post(self, form):
        # post process form
        flash(self.message, "info")


appbuilder.add_view(
    MyFormView,
    "My form View",
    icon="fa-group",
    label=_("My form View"),
    category="My Forms",
    category_icon="fa-cogs",
)



"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
