# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _aerosol.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_aerosol', [dirname(__file__)])
        except ImportError:
            import _aerosol
            return _aerosol
        if fp is not None:
            try:
                _mod = imp.load_module('_aerosol', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _aerosol = swig_import_helper()
    del swig_import_helper
else:
    import _aerosol
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



_aerosol.SHARED_PTR_DISOWN_swigconstant(_aerosol)
SHARED_PTR_DISOWN = _aerosol.SHARED_PTR_DISOWN

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

import full_physics_swig.state_vector
import full_physics_swig.generic_object
import full_physics_swig.pressure
class ObserverAerosol(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _aerosol.ObserverAerosol_swiginit(self, _aerosol.new_ObserverAerosol())
    __swig_destroy__ = _aerosol.delete_ObserverAerosol
ObserverAerosol.notify_update = new_instancemethod(_aerosol.ObserverAerosol_notify_update, None, ObserverAerosol)
ObserverAerosol.notify_add = new_instancemethod(_aerosol.ObserverAerosol_notify_add, None, ObserverAerosol)
ObserverAerosol.notify_remove = new_instancemethod(_aerosol.ObserverAerosol_notify_remove, None, ObserverAerosol)
ObserverAerosol_swigregister = _aerosol.ObserverAerosol_swigregister
ObserverAerosol_swigregister(ObserverAerosol)

class ObservableAerosol(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol.delete_ObservableAerosol
ObservableAerosol.add_observer_and_keep_reference = new_instancemethod(_aerosol.ObservableAerosol_add_observer_and_keep_reference, None, ObservableAerosol)
ObservableAerosol.add_observer = new_instancemethod(_aerosol.ObservableAerosol_add_observer, None, ObservableAerosol)
ObservableAerosol.remove_observer = new_instancemethod(_aerosol.ObservableAerosol_remove_observer, None, ObservableAerosol)
ObservableAerosol_swigregister = _aerosol.ObservableAerosol_swigregister
ObservableAerosol_swigregister(ObservableAerosol)

class Aerosol(full_physics_swig.state_vector.StateVectorObserver, ObservableAerosol):
    """

    This class maintains the aerosol portion of the state.

    Other objects may depend on the aerosol, and should be updated when
    the aerosol is updated. To facilitate that, this class in an
    Oberverable, and objects can add themselves as Observers to be
    notified when the aerosol is updated.

    I'm not really sure what the interface for this class should be. Right
    now it is used only by AtmosphereOco, and there is only one instance
    AerosolOptical, so the functions are what AtmosphereOco needs. But we
    may perhaps want to modify this in the future to be more general.

    C++ includes: aerosol.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def pf_mom(self, wn, frac_aer, nummom=-1, numscat=-1):
        """

        virtual ArrayAd<double, 3> FullPhysics::Aerosol::pf_mom(double wn, const ArrayAd< double, 2 > &frac_aer, int nummom=-1, int
        numscat=-1) const =0
        This calculates the portion of the phase function moments that come
        from the aerosol.

        Parameters:
        -----------

        wn:  The wave number.

        frac_aer:  This is number_active_layer() x number_particle()

        nummom:  Number of moments to fill in

        numscat:  Number of scatters to fill in 
        """
        return _aerosol.Aerosol_pf_mom(self, wn, frac_aer, nummom, numscat)


    def optical_depth_each_layer(self, wn):
        """

        virtual ArrayAd<double, 2> FullPhysics::Aerosol::optical_depth_each_layer(double wn) const =0
        This gives the optical depth for each layer, for the given wave
        number.

        Note this only includes the aerosol portion of this, Atmosphere class
        combines this with Absorbers and rayleigh scattering.

        This calculates the derivatives with respect to the state vector.

        This has size of number_active_layer() x number_particle(). 
        """
        return _aerosol.Aerosol_optical_depth_each_layer(self, wn)


    def ssa_each_layer(self, wn, particle_index, Od):
        """

        virtual ArrayAd<double, 1> FullPhysics::Aerosol::ssa_each_layer(double wn, int particle_index, const ArrayAd< double, 1 > &Od) const
        =0
        This gives the single scatter albedo for each layer, for the given
        wave number, for the given particle.

        Note this only includes the aerosol portion of this, Atmosphere class
        combines this with Rayleigh scattering.

        We take in the optical depth of each layer. This is just what is
        returned by optical_depth_each_layer(), we take this in because we can
        change what the derivative of optical_depth_each_layer is respect to,
        e.g. in AtmosphereOco we use taua_i.

        This calculates the derivative with respect to whatever variables Od
        is relative to.

        This has size of number_active_layer() 
        """
        return _aerosol.Aerosol_ssa_each_layer(self, wn, particle_index, Od)


    def _v_number_particle(self):
        """

        virtual int FullPhysics::Aerosol::number_particle() const =0
        Number of aerosol particles. 
        """
        return _aerosol.Aerosol__v_number_particle(self)


    @property
    def number_particle(self):
        return self._v_number_particle()


    def clone(self, *args):
        """

        virtual boost::shared_ptr<Aerosol> FullPhysics::Aerosol::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        RelativeHumidity > &Rh) const =0

        """
        return _aerosol.Aerosol_clone(self, *args)

    __swig_destroy__ = _aerosol.delete_Aerosol
Aerosol.__str__ = new_instancemethod(_aerosol.Aerosol___str__, None, Aerosol)
Aerosol.pf_mom = new_instancemethod(_aerosol.Aerosol_pf_mom, None, Aerosol)
Aerosol.optical_depth_each_layer = new_instancemethod(_aerosol.Aerosol_optical_depth_each_layer, None, Aerosol)
Aerosol.ssa_each_layer = new_instancemethod(_aerosol.Aerosol_ssa_each_layer, None, Aerosol)
Aerosol._v_number_particle = new_instancemethod(_aerosol.Aerosol__v_number_particle, None, Aerosol)
Aerosol.clone = new_instancemethod(_aerosol.Aerosol_clone, None, Aerosol)
Aerosol_swigregister = _aerosol.Aerosol_swigregister
Aerosol_swigregister(Aerosol)



