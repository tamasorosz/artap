from .problem import Problem
from .algorithm import Algorithm
from .config import artap_root
from .job import JobSimple

import time

import sys
import os
sys.path.append(artap_root + os.sep + "lib")

import _nlopt

import builtins as __builtin__


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
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _nlopt.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _nlopt.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _nlopt.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _nlopt.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _nlopt.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _nlopt.SwigPyIterator_equal(self, x)

    def copy(self):
        return _nlopt.SwigPyIterator_copy(self)

    def next(self):
        return _nlopt.SwigPyIterator_next(self)

    def __next__(self):
        return _nlopt.SwigPyIterator___next__(self)

    def previous(self):
        return _nlopt.SwigPyIterator_previous(self)

    def advance(self, n):
        return _nlopt.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _nlopt.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _nlopt.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _nlopt.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _nlopt.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _nlopt.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _nlopt.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _nlopt.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class nlopt_doublevector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nlopt_doublevector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nlopt_doublevector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _nlopt.nlopt_doublevector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _nlopt.nlopt_doublevector___nonzero__(self)

    def __bool__(self):
        return _nlopt.nlopt_doublevector___bool__(self)

    def __len__(self):
        return _nlopt.nlopt_doublevector___len__(self)

    def __getslice__(self, i, j):
        return _nlopt.nlopt_doublevector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _nlopt.nlopt_doublevector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _nlopt.nlopt_doublevector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _nlopt.nlopt_doublevector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _nlopt.nlopt_doublevector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _nlopt.nlopt_doublevector___setitem__(self, *args)

    def pop(self):
        return _nlopt.nlopt_doublevector_pop(self)

    def append(self, x):
        return _nlopt.nlopt_doublevector_append(self, x)

    def empty(self):
        return _nlopt.nlopt_doublevector_empty(self)

    def size(self):
        return _nlopt.nlopt_doublevector_size(self)

    def swap(self, v):
        return _nlopt.nlopt_doublevector_swap(self, v)

    def begin(self):
        return _nlopt.nlopt_doublevector_begin(self)

    def end(self):
        return _nlopt.nlopt_doublevector_end(self)

    def rbegin(self):
        return _nlopt.nlopt_doublevector_rbegin(self)

    def rend(self):
        return _nlopt.nlopt_doublevector_rend(self)

    def clear(self):
        return _nlopt.nlopt_doublevector_clear(self)

    def get_allocator(self):
        return _nlopt.nlopt_doublevector_get_allocator(self)

    def pop_back(self):
        return _nlopt.nlopt_doublevector_pop_back(self)

    def erase(self, *args):
        return _nlopt.nlopt_doublevector_erase(self, *args)

    def __init__(self, *args):
        this = _nlopt.new_nlopt_doublevector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _nlopt.nlopt_doublevector_push_back(self, x)

    def front(self):
        return _nlopt.nlopt_doublevector_front(self)

    def back(self):
        return _nlopt.nlopt_doublevector_back(self)

    def assign(self, n, x):
        return _nlopt.nlopt_doublevector_assign(self, n, x)

    def resize(self, *args):
        return _nlopt.nlopt_doublevector_resize(self, *args)

    def insert(self, *args):
        return _nlopt.nlopt_doublevector_insert(self, *args)

    def reserve(self, n):
        return _nlopt.nlopt_doublevector_reserve(self, n)

    def capacity(self):
        return _nlopt.nlopt_doublevector_capacity(self)
    __swig_destroy__ = _nlopt.delete_nlopt_doublevector
    __del__ = lambda self: None
nlopt_doublevector_swigregister = _nlopt.nlopt_doublevector_swigregister
nlopt_doublevector_swigregister(nlopt_doublevector)


ForcedStop = _nlopt.ForcedStop
RoundoffLimited = _nlopt.RoundoffLimited
__version__ = str(_nlopt.version_major())+'.'+str(_nlopt.version_minor())+'.'+str(_nlopt.version_bugfix())


def nlopt_get_initial_step(opt, dx):
    return _nlopt.nlopt_get_initial_step(opt, dx)
nlopt_get_initial_step = _nlopt.nlopt_get_initial_step
GN_DIRECT = _nlopt.GN_DIRECT
GN_DIRECT_L = _nlopt.GN_DIRECT_L
GN_DIRECT_L_RAND = _nlopt.GN_DIRECT_L_RAND
GN_DIRECT_NOSCAL = _nlopt.GN_DIRECT_NOSCAL
GN_DIRECT_L_NOSCAL = _nlopt.GN_DIRECT_L_NOSCAL
GN_DIRECT_L_RAND_NOSCAL = _nlopt.GN_DIRECT_L_RAND_NOSCAL
GN_ORIG_DIRECT = _nlopt.GN_ORIG_DIRECT
GN_ORIG_DIRECT_L = _nlopt.GN_ORIG_DIRECT_L
GD_STOGO = _nlopt.GD_STOGO
GD_STOGO_RAND = _nlopt.GD_STOGO_RAND
LD_LBFGS_NOCEDAL = _nlopt.LD_LBFGS_NOCEDAL
LD_LBFGS = _nlopt.LD_LBFGS
LN_PRAXIS = _nlopt.LN_PRAXIS
LD_VAR1 = _nlopt.LD_VAR1
LD_VAR2 = _nlopt.LD_VAR2
LD_TNEWTON = _nlopt.LD_TNEWTON
LD_TNEWTON_RESTART = _nlopt.LD_TNEWTON_RESTART
LD_TNEWTON_PRECOND = _nlopt.LD_TNEWTON_PRECOND
LD_TNEWTON_PRECOND_RESTART = _nlopt.LD_TNEWTON_PRECOND_RESTART
GN_CRS2_LM = _nlopt.GN_CRS2_LM
GN_MLSL = _nlopt.GN_MLSL
GD_MLSL = _nlopt.GD_MLSL
GN_MLSL_LDS = _nlopt.GN_MLSL_LDS
GD_MLSL_LDS = _nlopt.GD_MLSL_LDS
LD_MMA = _nlopt.LD_MMA
LN_COBYLA = _nlopt.LN_COBYLA
LN_NEWUOA = _nlopt.LN_NEWUOA
LN_NEWUOA_BOUND = _nlopt.LN_NEWUOA_BOUND
LN_NELDERMEAD = _nlopt.LN_NELDERMEAD
LN_SBPLX = _nlopt.LN_SBPLX
LN_AUGLAG = _nlopt.LN_AUGLAG
LD_AUGLAG = _nlopt.LD_AUGLAG
LN_AUGLAG_EQ = _nlopt.LN_AUGLAG_EQ
LD_AUGLAG_EQ = _nlopt.LD_AUGLAG_EQ
LN_BOBYQA = _nlopt.LN_BOBYQA
GN_ISRES = _nlopt.GN_ISRES
AUGLAG = _nlopt.AUGLAG
AUGLAG_EQ = _nlopt.AUGLAG_EQ
G_MLSL = _nlopt.G_MLSL
G_MLSL_LDS = _nlopt.G_MLSL_LDS
LD_SLSQP = _nlopt.LD_SLSQP
LD_CCSAQ = _nlopt.LD_CCSAQ
GN_ESCH = _nlopt.GN_ESCH
GN_AGS = _nlopt.GN_AGS
NUM_ALGORITHMS = _nlopt.NUM_ALGORITHMS
FAILURE = _nlopt.FAILURE
INVALID_ARGS = _nlopt.INVALID_ARGS
OUT_OF_MEMORY = _nlopt.OUT_OF_MEMORY
ROUNDOFF_LIMITED = _nlopt.ROUNDOFF_LIMITED
FORCED_STOP = _nlopt.FORCED_STOP
SUCCESS = _nlopt.SUCCESS
STOPVAL_REACHED = _nlopt.STOPVAL_REACHED
FTOL_REACHED = _nlopt.FTOL_REACHED
XTOL_REACHED = _nlopt.XTOL_REACHED
MAXEVAL_REACHED = _nlopt.MAXEVAL_REACHED
MAXTIME_REACHED = _nlopt.MAXTIME_REACHED
class roundoff_limited(Exception):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, roundoff_limited, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, roundoff_limited, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _nlopt.new_roundoff_limited()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _nlopt.delete_roundoff_limited
    __del__ = lambda self: None
roundoff_limited_swigregister = _nlopt.roundoff_limited_swigregister
roundoff_limited_swigregister(roundoff_limited)

class forced_stop(Exception):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, forced_stop, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, forced_stop, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _nlopt.new_forced_stop()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _nlopt.delete_forced_stop
    __del__ = lambda self: None
forced_stop_swigregister = _nlopt.forced_stop_swigregister
forced_stop_swigregister(forced_stop)

class opt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, opt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, opt, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _nlopt.delete_opt
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _nlopt.new_opt(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def optimize(self, *args):
        return _nlopt.opt_optimize(self, *args)

    def last_optimize_result(self):
        return _nlopt.opt_last_optimize_result(self)

    def last_optimum_value(self):
        return _nlopt.opt_last_optimum_value(self)

    def get_algorithm(self):
        return _nlopt.opt_get_algorithm(self)

    def get_algorithm_name(self):
        return _nlopt.opt_get_algorithm_name(self)

    def get_dimension(self):
        return _nlopt.opt_get_dimension(self)

    def set_min_objective(self, *args):
        return _nlopt.opt_set_min_objective(self, *args)

    def set_max_objective(self, *args):
        return _nlopt.opt_set_max_objective(self, *args)

    def remove_inequality_constraints(self):
        return _nlopt.opt_remove_inequality_constraints(self)

    def remove_equality_constraints(self):
        return _nlopt.opt_remove_equality_constraints(self)

    def add_inequality_constraint(self, *args):
        return _nlopt.opt_add_inequality_constraint(self, *args)

    def add_equality_constraint(self, *args):
        return _nlopt.opt_add_equality_constraint(self, *args)

    def add_inequality_mconstraint(self, *args):
        return _nlopt.opt_add_inequality_mconstraint(self, *args)

    def add_equality_mconstraint(self, *args):
        return _nlopt.opt_add_equality_mconstraint(self, *args)

    def get_lower_bounds(self, *args):
        return _nlopt.opt_get_lower_bounds(self, *args)

    def set_lower_bounds(self, *args):
        return _nlopt.opt_set_lower_bounds(self, *args)

    def get_upper_bounds(self, *args):
        return _nlopt.opt_get_upper_bounds(self, *args)

    def set_upper_bounds(self, *args):
        return _nlopt.opt_set_upper_bounds(self, *args)

    def get_stopval(self):
        return _nlopt.opt_get_stopval(self)

    def set_stopval(self, stopval):
        return _nlopt.opt_set_stopval(self, stopval)

    def get_ftol_rel(self):
        return _nlopt.opt_get_ftol_rel(self)

    def set_ftol_rel(self, ftol_rel):
        return _nlopt.opt_set_ftol_rel(self, ftol_rel)

    def get_ftol_abs(self):
        return _nlopt.opt_get_ftol_abs(self)

    def set_ftol_abs(self, ftol_abs):
        return _nlopt.opt_set_ftol_abs(self, ftol_abs)

    def get_xtol_rel(self):
        return _nlopt.opt_get_xtol_rel(self)

    def set_xtol_rel(self, xtol_rel):
        return _nlopt.opt_set_xtol_rel(self, xtol_rel)

    def get_xtol_abs(self, *args):
        return _nlopt.opt_get_xtol_abs(self, *args)

    def set_xtol_abs(self, *args):
        return _nlopt.opt_set_xtol_abs(self, *args)

    def get_maxeval(self):
        return _nlopt.opt_get_maxeval(self)

    def set_maxeval(self, maxeval):
        return _nlopt.opt_set_maxeval(self, maxeval)

    def get_numevals(self):
        return _nlopt.opt_get_numevals(self)

    def get_maxtime(self):
        return _nlopt.opt_get_maxtime(self)

    def set_maxtime(self, maxtime):
        return _nlopt.opt_set_maxtime(self, maxtime)

    def get_force_stop(self):
        return _nlopt.opt_get_force_stop(self)

    def set_force_stop(self, force_stop):
        return _nlopt.opt_set_force_stop(self, force_stop)

    def force_stop(self):
        return _nlopt.opt_force_stop(self)

    def get_errmsg(self):
        return _nlopt.opt_get_errmsg(self)

    def set_local_optimizer(self, lo):
        return _nlopt.opt_set_local_optimizer(self, lo)

    def get_population(self):
        return _nlopt.opt_get_population(self)

    def set_population(self, population):
        return _nlopt.opt_set_population(self, population)

    def get_vector_storage(self):
        return _nlopt.opt_get_vector_storage(self)

    def set_vector_storage(self, vector_storage):
        return _nlopt.opt_set_vector_storage(self, vector_storage)

    def set_initial_step(self, *args):
        return _nlopt.opt_set_initial_step(self, *args)

    def set_default_initial_step(self, x):
        return _nlopt.opt_set_default_initial_step(self, x)

    def get_initial_step(self, *args):
        return _nlopt.opt_get_initial_step(self, *args)

    def get_initial_step_(self, x):
        return _nlopt.opt_get_initial_step_(self, x)
opt_swigregister = _nlopt.opt_swigregister
opt_swigregister(opt)


def srand(seed):
    return _nlopt.srand(seed)
srand = _nlopt.srand

def srand_time():
    return _nlopt.srand_time()
srand_time = _nlopt.srand_time

def version(major, minor, bugfix):
    return _nlopt.version(major, minor, bugfix)
version = _nlopt.version

def version_major():
    return _nlopt.version_major()
version_major = _nlopt.version_major

def version_minor():
    return _nlopt.version_minor()
version_minor = _nlopt.version_minor

def version_bugfix():
    return _nlopt.version_bugfix()
version_bugfix = _nlopt.version_bugfix

def algorithm_name(a):
    return _nlopt.algorithm_name(a)
algorithm_name = _nlopt.algorithm_name
# This file is compatible with both classic and new-style classes.

_algorithm = [GN_DIRECT_L, GN_DIRECT_L_RAND, GN_MLSL, GN_CRS2_LM, GN_ISRES, GN_ESCH, LN_BOBYQA, LN_COBYLA, LN_NELDERMEAD, LN_SBPLX,  LN_PRAXIS, LN_AUGLAG_EQ]

class NLopt(Algorithm):
    """ NLopt algorithms """

    def __init__(self, problem: Problem, name="NLopt"):
        super().__init__(problem, name)

        self.job = JobSimple(self.problem)
        self.options.declare(name='algorithm', default=LN_BOBYQA, values=_algorithm,
                             desc='Algorithm')
        self.options.declare(name='n_iterations', default=50, lower=1,
                             desc='Maximum evaluations')
        self.options.declare(name='xtol_rel', default=1e-6, lower=0.0,
                             desc='xtol_rel')
        self.options.declare(name='xtol_abs', default=1e-12, lower=0.0,
                             desc='xtol_abs')
        self.options.declare(name='ftol_rel', default=1e-6, lower=0.0,
                             desc='ftol_rel')
        self.options.declare(name='ftol_abs', default=1e-12, lower=0.0,
                             desc='ftol_abs')

    def _function(self, x, grad):
        return self.job.evaluate_scalar(x)

    def _constraint(x, grad, a, b):
        # if grad.size > 0:
        #     grad[0] = 3 * a * (a * x[0] + b) ** 2
        #     grad[1] = -1.0
        # return (a * x[0] + b) ** 3 - x[1]
        return 0

    def run(self):
        # Figure out bounds vectors.
        lb = []
        ub = []
        for parameter in self.problem.parameters:
            bounds = parameter['bounds']

            lb.append(bounds[0])
            ub.append(bounds[1])

        op = opt(self.options['algorithm'], len(self.problem.parameters))
        op.set_lower_bounds(lb)
        op.set_upper_bounds(ub)
        op.set_min_objective(self._function)
        op.set_xtol_rel(self.options['xtol_rel'])
        op.set_xtol_abs(self.options['xtol_abs'])
        op.set_ftol_rel(self.options['ftol_rel'])
        op.set_ftol_abs(self.options['ftol_abs'])
        op.set_maxeval(self.options['n_iterations'])

        # constraint
        # op.add_inequality_constraint(lambda x, grad: myconstraint(x, grad, 2, 0), 1e-8)
        # op.add_inequality_constraint(lambda x, grad: myconstraint(x, grad, -1, 1), 1e-8)

        try:
            t_s = time.time()
            self.problem.logger.info("NLopt: {}".format(op.get_algorithm_name()))
            x = op.optimize(self.problem.get_initial_values())
            # print('initial values:',x)
            t = time.time() - t_s
            self.problem.logger.info("NLopt: elapsed time: {} s".format(t))

            """
            if self.options['verbose_level'] >= 1:
                print('method: ', op.get_algorithm_name())
                print('optimum at ', x)
                print('minimum value = ', op.last_optimum_value())
                print('nevals = ', op.get_numevals())
            """
        except RuntimeError:
            print('Optimization FAILED.')
            print(op.get_errmsg())
        except ValueError:
            print('Optimization FAILED.')
            print(op.get_errmsg())

        msg_nlopt = {-1: 'failure - generic failure code',
                     -2: 'failure - invalid arguments',
                     -3: 'failure - out of memory',
                     -4: 'failure - round off limited',
                     -5: 'failure - forced stop',
                      1: 'success - generic success code',
                      2: 'success - stop value reached',
                      3: 'success - ftol reached',
                      4: 'success - xtol reached',
                      5: 'success - maxeval reached',
                      6: 'success - maxtime reached'
                     }

        if self.options['verbose_level'] >= 1:
            print('optimum = ', op.last_optimum_value())
            print('result code and meaning = ', op.last_optimize_result(), msg_nlopt[op.last_optimize_result()])