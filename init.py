def classFactory(iface):
    from .main_plugin import BufferPlugin
    return BufferPlugin(iface)
