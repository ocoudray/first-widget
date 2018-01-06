import ipywidgets as widgets
from traitlets import Unicode, CFloat

@widgets.register
class FirstWidget(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('FirstView').tag(sync=True)
    _model_name = Unicode('FirstModel').tag(sync=True)
    _view_module = Unicode('FirstWidget').tag(sync=True)
    _model_module = Unicode('FirstWidget').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Unicode('Hello World!').tag(sync=True)
