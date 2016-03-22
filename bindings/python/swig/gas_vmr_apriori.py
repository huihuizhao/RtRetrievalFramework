# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _gas_vmr_apriori.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gas_vmr_apriori', [dirname(__file__)])
        except ImportError:
            import _gas_vmr_apriori
            return _gas_vmr_apriori
        if fp is not None:
            try:
                _mod = imp.load_module('_gas_vmr_apriori', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gas_vmr_apriori = swig_import_helper()
    del swig_import_helper
else:
    import _gas_vmr_apriori
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



_gas_vmr_apriori.SHARED_PTR_DISOWN_swigconstant(_gas_vmr_apriori)
SHARED_PTR_DISOWN = _gas_vmr_apriori.SHARED_PTR_DISOWN

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

import full_physics_swig.generic_object
import full_physics_swig.state_vector
class GasVmrApriori(full_physics_swig.generic_object.GenericObject):
    """

    Adapts the ReferenceVmrApriori class into a form that is easier to
    work with in the context of how this framework works.

    This class deals keys off of pressure levels like the rest of the
    framework. It also uses the increasing pressure levels convention.

    The VMR returned will be in the order of levels expected elsewhere in
    the framework.

    C++ includes: gas_vmr_apriori.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Ecmwf_file, L1b_file, Alt, Hdf_static_input, Hdf_group, Gas_name):
        """

        GasVmrApriori::GasVmrApriori(const boost::shared_ptr< Ecmwf > &Ecmwf_file, const
        boost::shared_ptr< Level1b > &L1b_file, const boost::shared_ptr<
        Altitude > &Alt, const HdfFile &Hdf_static_input, const std::string
        &Hdf_group, const std::string &Gas_name)

        """
        _gas_vmr_apriori.GasVmrApriori_swiginit(self, _gas_vmr_apriori.new_GasVmrApriori(Ecmwf_file, L1b_file, Alt, Hdf_static_input, Hdf_group, Gas_name))

    def _v_apriori_vmr(self):
        """

        const blitz::Array< double, 1 > GasVmrApriori::apriori_vmr() const

        """
        return _gas_vmr_apriori.GasVmrApriori__v_apriori_vmr(self)


    @property
    def apriori_vmr(self):
        return self._v_apriori_vmr()

    __swig_destroy__ = _gas_vmr_apriori.delete_GasVmrApriori
GasVmrApriori._v_apriori_vmr = new_instancemethod(_gas_vmr_apriori.GasVmrApriori__v_apriori_vmr, None, GasVmrApriori)
GasVmrApriori.__str__ = new_instancemethod(_gas_vmr_apriori.GasVmrApriori___str__, None, GasVmrApriori)
GasVmrApriori_swigregister = _gas_vmr_apriori.GasVmrApriori_swigregister
GasVmrApriori_swigregister(GasVmrApriori)



