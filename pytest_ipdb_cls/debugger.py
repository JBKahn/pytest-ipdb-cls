class Debugger(object):
    quitting = None

    def set_trace(self, frame):
        import ipdb  # noqa

        return ipdb.set_trace(frame)  # noqa

    def reset(self, *args, **kwargs):
        from ipdb.__main__ import _init_pdb
        pdb_obj = _init_pdb()
        pdb_obj.botframe = None  # not sure. exception otherwise at quit
        return pdb_obj.reset(*args, **kwargs)

    def interaction(self, *args, **kwargs):
        from ipdb.__main__ import _init_pdb
        pdb_obj = _init_pdb()
        pdb_obj.botframe = None  # not sure. exception otherwise at quit
        return pdb_obj.interaction(*args, **kwargs)
