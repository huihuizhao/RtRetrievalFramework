# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _radiative_transfer_retrievable.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_radiative_transfer_retrievable', [dirname(__file__)])
        except ImportError:
            import _radiative_transfer_retrievable
            return _radiative_transfer_retrievable
        if fp is not None:
            try:
                _mod = imp.load_module('_radiative_transfer_retrievable', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _radiative_transfer_retrievable = swig_import_helper()
    del swig_import_helper
else:
    import _radiative_transfer_retrievable
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



_radiative_transfer_retrievable.SHARED_PTR_DISOWN_swigconstant(_radiative_transfer_retrievable)
SHARED_PTR_DISOWN = _radiative_transfer_retrievable.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.radiative_transfer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.sub_state_vector_array
class ObservableRadiativeTransferRetrievable(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _radiative_transfer_retrievable.delete_ObservableRadiativeTransferRetrievable
ObservableRadiativeTransferRetrievable.add_observer_and_keep_reference = new_instancemethod(_radiative_transfer_retrievable.ObservableRadiativeTransferRetrievable_add_observer_and_keep_reference, None, ObservableRadiativeTransferRetrievable)
ObservableRadiativeTransferRetrievable.add_observer = new_instancemethod(_radiative_transfer_retrievable.ObservableRadiativeTransferRetrievable_add_observer, None, ObservableRadiativeTransferRetrievable)
ObservableRadiativeTransferRetrievable.remove_observer = new_instancemethod(_radiative_transfer_retrievable.ObservableRadiativeTransferRetrievable_remove_observer, None, ObservableRadiativeTransferRetrievable)
ObservableRadiativeTransferRetrievable_swigregister = _radiative_transfer_retrievable.ObservableRadiativeTransferRetrievable_swigregister
ObservableRadiativeTransferRetrievable_swigregister(ObservableRadiativeTransferRetrievable)

class ObserverRadiativeTransferRetrievable(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _radiative_transfer_retrievable.ObserverRadiativeTransferRetrievable_swiginit(self, _radiative_transfer_retrievable.new_ObserverRadiativeTransferRetrievable())
    __swig_destroy__ = _radiative_transfer_retrievable.delete_ObserverRadiativeTransferRetrievable
ObserverRadiativeTransferRetrievable.notify_update = new_instancemethod(_radiative_transfer_retrievable.ObserverRadiativeTransferRetrievable_notify_update, None, ObserverRadiativeTransferRetrievable)
ObserverRadiativeTransferRetrievable.notify_add = new_instancemethod(_radiative_transfer_retrievable.ObserverRadiativeTransferRetrievable_notify_add, None, ObserverRadiativeTransferRetrievable)
ObserverRadiativeTransferRetrievable.notify_remove = new_instancemethod(_radiative_transfer_retrievable.ObserverRadiativeTransferRetrievable_notify_remove, None, ObserverRadiativeTransferRetrievable)
ObserverRadiativeTransferRetrievable_swigregister = _radiative_transfer_retrievable.ObserverRadiativeTransferRetrievable_swigregister
ObserverRadiativeTransferRetrievable_swigregister(ObserverRadiativeTransferRetrievable)

class RadiativeTransferRetrievable(full_physics_swig.radiative_transfer.RadiativeTransfer, full_physics_swig.state_vector.StateVectorObserver, ObservableRadiativeTransferRetrievable):
    """

    Interface class for radiative transfer implementations that happen to
    have retrievable parameters.

    C++ includes: radiative_transfer_retrievable.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _radiative_transfer_retrievable.delete_RadiativeTransferRetrievable
RadiativeTransferRetrievable_swigregister = _radiative_transfer_retrievable.RadiativeTransferRetrievable_swigregister
RadiativeTransferRetrievable_swigregister(RadiativeTransferRetrievable)

class SubStateVectorArrayRadiativeTransfer(RadiativeTransferRetrievable, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _radiative_transfer_retrievable.delete_SubStateVectorArrayRadiativeTransfer

    @property
    def coefficient(self):
        return self._v_coefficient()


    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayRadiativeTransfer.init = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer_init, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer.state_vector_name_i = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer_state_vector_name_i, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer.update_sub_state_hook = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer_update_sub_state_hook, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer._v_coefficient = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer__v_coefficient, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer._v_used_flag_value = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer__v_used_flag_value, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer._v_statevector_covariance = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer__v_statevector_covariance, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer._v_pressure = new_instancemethod(_radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer__v_pressure, None, SubStateVectorArrayRadiativeTransfer)
SubStateVectorArrayRadiativeTransfer_swigregister = _radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer_swigregister
SubStateVectorArrayRadiativeTransfer_swigregister(SubStateVectorArrayRadiativeTransfer)



