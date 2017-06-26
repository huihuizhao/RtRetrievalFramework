# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _twostream_driver.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_twostream_driver', [dirname(__file__)])
        except ImportError:
            import _twostream_driver
            return _twostream_driver
        if fp is not None:
            try:
                _mod = imp.load_module('_twostream_driver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _twostream_driver = swig_import_helper()
    del swig_import_helper
else:
    import _twostream_driver
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



_twostream_driver.SHARED_PTR_DISOWN_swigconstant(_twostream_driver)
SHARED_PTR_DISOWN = _twostream_driver.SHARED_PTR_DISOWN

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
class TwostreamBrdfDriver(object):
    """

    TwoStream specific BRDF driver implementation.

    C++ includes: twostream_driver.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, surface_type):
        """

        TwostreamBrdfDriver::TwostreamBrdfDriver(int surface_type)
        Initialize Twostream BRDF interface. 
        """
        _twostream_driver.TwostreamBrdfDriver_swiginit(self, _twostream_driver.new_TwostreamBrdfDriver(surface_type))
    __swig_destroy__ = _twostream_driver.delete_TwostreamBrdfDriver

    def setup_geometry(self, sza, azm, zen):
        """

        void TwostreamBrdfDriver::setup_geometry(double sza, double azm, double zen) const

        """
        return _twostream_driver.TwostreamBrdfDriver_setup_geometry(self, sza, azm, zen)


    def _v_n_brdf_kernels(self):
        """

        int TwostreamBrdfDriver::n_brdf_kernels() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_n_brdf_kernels(self)


    @property
    def n_brdf_kernels(self):
        return self._v_n_brdf_kernels()


    def _v_n_kernel_factor_wfs(self):
        """

        int TwostreamBrdfDriver::n_kernel_factor_wfs() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_n_kernel_factor_wfs(self)


    @property
    def n_kernel_factor_wfs(self):
        return self._v_n_kernel_factor_wfs()


    def _v_n_kernel_params_wfs(self):
        """

        int TwostreamBrdfDriver::n_kernel_params_wfs() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_n_kernel_params_wfs(self)


    @property
    def n_kernel_params_wfs(self):
        return self._v_n_kernel_params_wfs()


    def _v_n_surface_wfs(self):
        """

        int TwostreamBrdfDriver::n_surface_wfs() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_n_surface_wfs(self)


    @property
    def n_surface_wfs(self):
        return self._v_n_surface_wfs()


    def _v_do_shadow_effect(self):
        """

        bool TwostreamBrdfDriver::do_shadow_effect() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_do_shadow_effect(self)


    @property
    def do_shadow_effect(self):
        return self._v_do_shadow_effect()


    def _v_brdf_interface(self):
        """

        boost::shared_ptr<Twostream_Ls_Brdf_Supplement> FullPhysics::TwostreamBrdfDriver::brdf_interface() const

        """
        return _twostream_driver.TwostreamBrdfDriver__v_brdf_interface(self)


    @property
    def brdf_interface(self):
        return self._v_brdf_interface()


    def do_kparams_derivs(self, kernel_index):
        """

        bool TwostreamBrdfDriver::do_kparams_derivs(const int kernel_index) const

        """
        return _twostream_driver.TwostreamBrdfDriver_do_kparams_derivs(self, kernel_index)

TwostreamBrdfDriver.setup_geometry = new_instancemethod(_twostream_driver.TwostreamBrdfDriver_setup_geometry, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_n_brdf_kernels = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_n_brdf_kernels, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_n_kernel_factor_wfs = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_n_kernel_factor_wfs, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_n_kernel_params_wfs = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_n_kernel_params_wfs, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_n_surface_wfs = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_n_surface_wfs, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_do_shadow_effect = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_do_shadow_effect, None, TwostreamBrdfDriver)
TwostreamBrdfDriver._v_brdf_interface = new_instancemethod(_twostream_driver.TwostreamBrdfDriver__v_brdf_interface, None, TwostreamBrdfDriver)
TwostreamBrdfDriver.do_kparams_derivs = new_instancemethod(_twostream_driver.TwostreamBrdfDriver_do_kparams_derivs, None, TwostreamBrdfDriver)
TwostreamBrdfDriver_swigregister = _twostream_driver.TwostreamBrdfDriver_swigregister
TwostreamBrdfDriver_swigregister(TwostreamBrdfDriver)

class TwostreamRtDriver(object):
    """

    TwoStream specific Radiative transfer driver implementation.

    C++ includes: twostream_driver.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, nlayers, npars, surface_type, do_fullquadrature=True):
        """

        TwostreamRtDriver::TwostreamRtDriver(int nlayers, int npars, int surface_type, bool
        do_fullquadrature=true, bool pure_nadir=false)
        TwostreamRtDriver Sizes of layers, and number of jacobians must be set
        up in construtor as seen in signature.

        Use do_fullquadratures = false only for comparison against LIDORT 
        """
        _twostream_driver.TwostreamRtDriver_swiginit(self, _twostream_driver.new_TwostreamRtDriver(nlayers, npars, surface_type, do_fullquadrature))

    def setup_height_grid(self, height_grid):
        """

        void TwostreamRtDriver::setup_height_grid(const blitz::Array< double, 1 > &height_grid) const

        """
        return _twostream_driver.TwostreamRtDriver_setup_height_grid(self, height_grid)


    def setup_geometry(self, sza, azm, zen):
        """

        void TwostreamRtDriver::setup_geometry(double sza, double azm, double zen) const

        """
        return _twostream_driver.TwostreamRtDriver_setup_geometry(self, sza, azm, zen)


    def setup_optical_inputs(self, od, ssa, pf):
        """

        void TwostreamRtDriver::setup_optical_inputs(const blitz::Array< double, 1 > &od, const blitz::Array< double, 1 >
        &ssa, const blitz::Array< double, 2 > &pf) const

        """
        return _twostream_driver.TwostreamRtDriver_setup_optical_inputs(self, od, ssa, pf)


    def clear_linear_inputs(self):
        """

        void TwostreamRtDriver::clear_linear_inputs() const

        """
        return _twostream_driver.TwostreamRtDriver_clear_linear_inputs(self)


    def setup_linear_inputs(self, od, ssa, pf, do_surface_linearization):
        """

        void TwostreamRtDriver::setup_linear_inputs(const ArrayAd< double, 1 > &od, const ArrayAd< double, 1 > &ssa,
        const ArrayAd< double, 2 > &pf, bool do_surface_linearization) const

        """
        return _twostream_driver.TwostreamRtDriver_setup_linear_inputs(self, od, ssa, pf, do_surface_linearization)


    def calculate_rt(self):
        """

        void TwostreamRtDriver::calculate_rt() const

        """
        return _twostream_driver.TwostreamRtDriver_calculate_rt(self)


    def get_intensity(self):
        """

        double TwostreamRtDriver::get_intensity() const

        """
        return _twostream_driver.TwostreamRtDriver_get_intensity(self)


    def copy_jacobians(self, jac_atm, jac_surf):
        """

        void TwostreamRtDriver::copy_jacobians(blitz::Array< double, 2 > &jac_atm, blitz::Array< double, 1 >
        &jac_surf) const

        """
        return _twostream_driver.TwostreamRtDriver_copy_jacobians(self, jac_atm, jac_surf)


    def _v_twostream_brdf_driver(self):
        """

        boost::shared_ptr<TwostreamBrdfDriver> FullPhysics::TwostreamRtDriver::twostream_brdf_driver() const

        """
        return _twostream_driver.TwostreamRtDriver__v_twostream_brdf_driver(self)


    @property
    def twostream_brdf_driver(self):
        return self._v_twostream_brdf_driver()


    def _v_brdf_interface(self):
        """

        boost::shared_ptr<Twostream_Ls_Brdf_Supplement> FullPhysics::TwostreamRtDriver::brdf_interface() const

        """
        return _twostream_driver.TwostreamRtDriver__v_brdf_interface(self)


    @property
    def brdf_interface(self):
        return self._v_brdf_interface()


    def _v_twostream_interface(self):
        """

        boost::shared_ptr<Twostream_L_Master> FullPhysics::TwostreamRtDriver::twostream_interface() const

        """
        return _twostream_driver.TwostreamRtDriver__v_twostream_interface(self)


    @property
    def twostream_interface(self):
        return self._v_twostream_interface()


    def _v_do_full_quadrature(self):
        """

        bool FullPhysics::TwostreamRtDriver::do_full_quadrature() const

        """
        return _twostream_driver.TwostreamRtDriver__v_do_full_quadrature(self)


    @property
    def do_full_quadrature(self):
        return self._v_do_full_quadrature()


    def _v_pure_nadir(self):
        """

        bool FullPhysics::TwostreamRtDriver::pure_nadir() const

        """
        return _twostream_driver.TwostreamRtDriver__v_pure_nadir(self)


    @property
    def pure_nadir(self):
        return self._v_pure_nadir()

    __swig_destroy__ = _twostream_driver.delete_TwostreamRtDriver
TwostreamRtDriver.setup_height_grid = new_instancemethod(_twostream_driver.TwostreamRtDriver_setup_height_grid, None, TwostreamRtDriver)
TwostreamRtDriver.setup_geometry = new_instancemethod(_twostream_driver.TwostreamRtDriver_setup_geometry, None, TwostreamRtDriver)
TwostreamRtDriver.setup_optical_inputs = new_instancemethod(_twostream_driver.TwostreamRtDriver_setup_optical_inputs, None, TwostreamRtDriver)
TwostreamRtDriver.clear_linear_inputs = new_instancemethod(_twostream_driver.TwostreamRtDriver_clear_linear_inputs, None, TwostreamRtDriver)
TwostreamRtDriver.setup_linear_inputs = new_instancemethod(_twostream_driver.TwostreamRtDriver_setup_linear_inputs, None, TwostreamRtDriver)
TwostreamRtDriver.calculate_rt = new_instancemethod(_twostream_driver.TwostreamRtDriver_calculate_rt, None, TwostreamRtDriver)
TwostreamRtDriver.get_intensity = new_instancemethod(_twostream_driver.TwostreamRtDriver_get_intensity, None, TwostreamRtDriver)
TwostreamRtDriver.copy_jacobians = new_instancemethod(_twostream_driver.TwostreamRtDriver_copy_jacobians, None, TwostreamRtDriver)
TwostreamRtDriver._v_twostream_brdf_driver = new_instancemethod(_twostream_driver.TwostreamRtDriver__v_twostream_brdf_driver, None, TwostreamRtDriver)
TwostreamRtDriver._v_brdf_interface = new_instancemethod(_twostream_driver.TwostreamRtDriver__v_brdf_interface, None, TwostreamRtDriver)
TwostreamRtDriver._v_twostream_interface = new_instancemethod(_twostream_driver.TwostreamRtDriver__v_twostream_interface, None, TwostreamRtDriver)
TwostreamRtDriver._v_do_full_quadrature = new_instancemethod(_twostream_driver.TwostreamRtDriver__v_do_full_quadrature, None, TwostreamRtDriver)
TwostreamRtDriver._v_pure_nadir = new_instancemethod(_twostream_driver.TwostreamRtDriver__v_pure_nadir, None, TwostreamRtDriver)
TwostreamRtDriver_swigregister = _twostream_driver.TwostreamRtDriver_swigregister
TwostreamRtDriver_swigregister(TwostreamRtDriver)



