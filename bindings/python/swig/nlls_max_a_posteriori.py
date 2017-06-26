# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _nlls_max_a_posteriori.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_nlls_max_a_posteriori', [dirname(__file__)])
        except ImportError:
            import _nlls_max_a_posteriori
            return _nlls_max_a_posteriori
        if fp is not None:
            try:
                _mod = imp.load_module('_nlls_max_a_posteriori', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _nlls_max_a_posteriori = swig_import_helper()
    del swig_import_helper
else:
    import _nlls_max_a_posteriori
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



_nlls_max_a_posteriori.SHARED_PTR_DISOWN_swigconstant(_nlls_max_a_posteriori)
SHARED_PTR_DISOWN = _nlls_max_a_posteriori.SHARED_PTR_DISOWN

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

import full_physics_swig.nlls_problem
import full_physics_swig.cost_func_diff
import full_physics_swig.cost_func
import full_physics_swig.problem_state
import full_physics_swig.generic_object
import full_physics_swig.nlls_problem_state
import full_physics_swig.model_measure
import full_physics_swig.model_state
class NLLSMaxAPosteriori(full_physics_swig.nlls_problem.NLLSProblem, full_physics_swig.nlls_problem_state.NLLSProblemState):
    """

    C++ includes: nlls_max_a_posteriori.h

    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, map, together=False):
        """

        FullPhysics::NLLSMaxAPosteriori::NLLSMaxAPosteriori(const boost::shared_ptr< MaxAPosteriori > &map, bool together=false)
        Constructor. 
        """
        _nlls_max_a_posteriori.NLLSMaxAPosteriori_swiginit(self, _nlls_max_a_posteriori.new_NLLSMaxAPosteriori(map, together))
    __swig_destroy__ = _nlls_max_a_posteriori.delete_NLLSMaxAPosteriori

    def _v_residual(self):
        """

        Array< double, 1 > NLLSMaxAPosteriori::residual()
        Return the residual of the NLLS problem at the current set point.

        Residual 
        """
        return _nlls_max_a_posteriori.NLLSMaxAPosteriori__v_residual(self)


    @property
    def residual(self):
        return self._v_residual()


    def _v_jacobian(self):
        """

        Array< double, 2 > NLLSMaxAPosteriori::jacobian()
        Return the Jacobian of the residual of the NLLS problem at the current
        set point.

        The Jacobian of the cost function. 
        """
        return _nlls_max_a_posteriori.NLLSMaxAPosteriori__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    @property
    def residual_size(self):
        return self._v_residual_size()


    @property
    def expected_parameter_size(self):
        return self._v_expected_parameter_size()


    def _v_parameters(self, *args):
        """

        virtual blitz::Array<double, 1> FullPhysics::NLLSMaxAPosteriori::parameters() const
        Just returns the current values of parameters.

        This method is redefined here (see the root base class) because of a
        compiler bug; otherwise, there should be no need for its redefinition.

        Current parameter values 
        """
        return _nlls_max_a_posteriori.NLLSMaxAPosteriori__v_parameters(self, *args)


    @property
    def parameters(self):
        return self._v_parameters()

    @parameters.setter
    def parameters(self, value):
      self._v_parameters(value)


    def _v_max_a_posteriori(self):
        """

        boost::shared_ptr<MaxAPosteriori> FullPhysics::NLLSMaxAPosteriori::max_a_posteriori()

        """
        return _nlls_max_a_posteriori.NLLSMaxAPosteriori__v_max_a_posteriori(self)


    @property
    def max_a_posteriori(self):
        return self._v_max_a_posteriori()

NLLSMaxAPosteriori._v_residual = new_instancemethod(_nlls_max_a_posteriori.NLLSMaxAPosteriori__v_residual, None, NLLSMaxAPosteriori)
NLLSMaxAPosteriori._v_jacobian = new_instancemethod(_nlls_max_a_posteriori.NLLSMaxAPosteriori__v_jacobian, None, NLLSMaxAPosteriori)
NLLSMaxAPosteriori._v_parameters = new_instancemethod(_nlls_max_a_posteriori.NLLSMaxAPosteriori__v_parameters, None, NLLSMaxAPosteriori)
NLLSMaxAPosteriori._v_max_a_posteriori = new_instancemethod(_nlls_max_a_posteriori.NLLSMaxAPosteriori__v_max_a_posteriori, None, NLLSMaxAPosteriori)
NLLSMaxAPosteriori_swigregister = _nlls_max_a_posteriori.NLLSMaxAPosteriori_swigregister
NLLSMaxAPosteriori_swigregister(NLLSMaxAPosteriori)



