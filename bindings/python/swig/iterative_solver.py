# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _iterative_solver.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_iterative_solver', [dirname(__file__)])
        except ImportError:
            import _iterative_solver
            return _iterative_solver
        if fp is not None:
            try:
                _mod = imp.load_module('_iterative_solver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _iterative_solver = swig_import_helper()
    del swig_import_helper
else:
    import _iterative_solver
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



_iterative_solver.SHARED_PTR_DISOWN_swigconstant(_iterative_solver)
SHARED_PTR_DISOWN = _iterative_solver.SHARED_PTR_DISOWN

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
class IterativeSolver(full_physics_swig.generic_object.GenericObject):
    """

    The base class for all iterative optimizers.

    This class is the base class for iterative optimizers. No derivatives
    of any order appear in the class implementation because not all
    optimization problem solvers require derivatives.

    An iterative solver, during the process of minimizing a cost function,
    moves from one point to the next in the parameter space. After
    computing a step, some optimization algorithms use some criteria to
    decide whether or not to take the step and to move to the next point.
    In the context of the class hierarchy rooted at this class, a step
    that is taken is called an accepted step, and a step that is not taken
    is called a rejected step. All the classes of the hierarchy that
    implement the solve() method must correctly record all the points and
    their associated cost function values after taking accepted steps
    only. The initial starting point and its cost value must also be
    recorded.

    This class is not associated with any problem (from the problem class
    hierarchy). Problems may appear in different formats (even if
    equivalent): residual/Jacobian, cost-function/gradient, cost-function
    only ...

    C++ includes: iterative_solver.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SUCCESS = _iterative_solver.IterativeSolver_SUCCESS
    CONTINUE = _iterative_solver.IterativeSolver_CONTINUE
    ERROR = _iterative_solver.IterativeSolver_ERROR
    UNTRIED = _iterative_solver.IterativeSolver_UNTRIED
    __swig_destroy__ = _iterative_solver.delete_IterativeSolver

    def _v_num_accepted_steps(self):
        """

        virtual int FullPhysics::IterativeSolver::num_accepted_steps() const
        Returns the number of the accepted steps.

        Number of the accepted steps 
        """
        return _iterative_solver.IterativeSolver__v_num_accepted_steps(self)


    @property
    def num_accepted_steps(self):
        return self._v_num_accepted_steps()


    def _v_accepted_points(self):
        """

        virtual std::vector< blitz::Array<double, 1> > FullPhysics::IterativeSolver::accepted_points() const
        Returns a vector (std) of accepted points.

        This method returns a std vector of accepted points in the parameter
        space. The initial starting point is always an accepted point. Then
        the second accepted point is the point obtained after taking the first
        accepted step from the initial (first) point. The third accepted point
        is the point obtained after taking the second accepted step from the
        second accepted point and so on.

        In other words, if the initial point and all the accepted points after
        taking the accepted steps are recorded correctly, then
        accepted_points()[0] is the initial starting point,

        accepted_points()[1] is the point obtained after taking the first
        accepted step from the initial point,

        accepted_points()[2] is the point obtained after taking the second
        accepted step from accepted_points()[1] point,

        ...

        accepted_points()[ num_accepted_steps()] is the last accepted point
        obtained after the last accepted step.

        Therefore, if the recording of the accepted points is done correctly,
        and num_accepted_steps() returns 2, then  accepted_points()[1] -
        accepted_points()[0] is the first accepted step, and

        accepted_points()[2] - accepted_points()[1] is the second accepted
        step

        A vector of accepted points 
        """
        return _iterative_solver.IterativeSolver__v_accepted_points(self)


    @property
    def accepted_points(self):
        return self._v_accepted_points()


    def _v_cost_at_accepted_points(self):
        """

        virtual std::vector<double> FullPhysics::IterativeSolver::cost_at_accepted_points() const
        Returns a vector (std) of cost function values at accepted points.

        This method returns a std vector of cost function values computed at
        the accepted points. In other words, if the accepted points and the
        cost function values at these points are recorded correctly, then
        cost_at_accepted_points()[0] is the value of the cost function at
        accepted_points()[0]

        cost_at_accepted_points()[1] is the value of the cost function at
        accepted_points()[1]

        ...

        and finally cost_at_accepted_points()[ num_accepted_steps()] is the
        value of the cost function at accepted_points()[ num_accepted_steps()]

        A vector of cost function values at accepted points 
        """
        return _iterative_solver.IterativeSolver__v_cost_at_accepted_points(self)


    @property
    def cost_at_accepted_points(self):
        return self._v_cost_at_accepted_points()


    def solve(self):
        """

        virtual void FullPhysics::IterativeSolver::solve()=0
        The method that solves the optimization problem.

        The algorithms that solve the optimization problem are implemented in
        this method by the leaf classes of the solver class hierarchy. 
        """
        return _iterative_solver.IterativeSolver_solve(self)


    def _v_status(self):
        """

        virtual status_t FullPhysics::IterativeSolver::status() const
        Returns a value of IterativeSolver::status_t type.

        This method returns the status of the solver. The status of the solver
        is initialized to IterativeSolver::UNTRIED, then it must be set to one
        of the following values by the implemented version of solve() method:
        IterativeSolver::SUCCESS

        IterativeSolver::CONTINUE

        IterativeSolver::ERROR

        Please, read the comments on IterativeSolver::status_t type and its
        possible values.

        Solver status 
        """
        return _iterative_solver.IterativeSolver__v_status(self)


    @property
    def status(self):
        return self._v_status()


    def _v_status_str(self):
        """

        const char *const IterativeSolver::status_str() const
        Returns the string version of the solver status.

        If the method status() returns  IterativeSolver::UNTRIED,

        IterativeSolver::SUCCESS,

        IterativeSolver::CONTINUE, or

        IterativeSolver::ERROR

        then status_str() will return "UNTRIED",

        "SUCCESS",

        "CONTINUE", or

        "ERROR"

        respectively.

        Solver status in string form 
        """
        return _iterative_solver.IterativeSolver__v_status_str(self)


    @property
    def status_str(self):
        return self._v_status_str()


    def record_accepted_point(self, point):
        """

        void FullPhysics::IterativeSolver::record_accepted_point(const blitz::Array< double, 1 > &point)
        Called to record an accepted point.

        This method is called to record an accepted point. It is the
        responsibility of the implementer of the solve() method to record the
        accepted points. The accepted points must be recorded in the same
        order that they are achieved.

        Parameters:
        -----------

        point:  an accepted point in the parameter space 
        """
        return _iterative_solver.IterativeSolver_record_accepted_point(self, point)


    def record_cost_at_accepted_point(self, cost):
        """

        void FullPhysics::IterativeSolver::record_cost_at_accepted_point(double cost)
        Called to record the cost function value at an accepted point.

        This method is called to record the cost function value at an accepted
        point. It is the responsibility of the implementer of the solve()
        method to record the cost function values at the accepted points. The
        cost values must be recorded in the same order that they are
        evaluated.

        Parameters:
        -----------

        cost:  cost funciotn value at an accepted point in the parameter space

        """
        return _iterative_solver.IterativeSolver_record_cost_at_accepted_point(self, cost)

IterativeSolver._v_num_accepted_steps = new_instancemethod(_iterative_solver.IterativeSolver__v_num_accepted_steps, None, IterativeSolver)
IterativeSolver._v_accepted_points = new_instancemethod(_iterative_solver.IterativeSolver__v_accepted_points, None, IterativeSolver)
IterativeSolver._v_cost_at_accepted_points = new_instancemethod(_iterative_solver.IterativeSolver__v_cost_at_accepted_points, None, IterativeSolver)
IterativeSolver.solve = new_instancemethod(_iterative_solver.IterativeSolver_solve, None, IterativeSolver)
IterativeSolver._v_status = new_instancemethod(_iterative_solver.IterativeSolver__v_status, None, IterativeSolver)
IterativeSolver._v_status_str = new_instancemethod(_iterative_solver.IterativeSolver__v_status_str, None, IterativeSolver)
IterativeSolver.record_accepted_point = new_instancemethod(_iterative_solver.IterativeSolver_record_accepted_point, None, IterativeSolver)
IterativeSolver.record_cost_at_accepted_point = new_instancemethod(_iterative_solver.IterativeSolver_record_cost_at_accepted_point, None, IterativeSolver)
IterativeSolver.__str__ = new_instancemethod(_iterative_solver.IterativeSolver___str__, None, IterativeSolver)
IterativeSolver_swigregister = _iterative_solver.IterativeSolver_swigregister
IterativeSolver_swigregister(IterativeSolver)



