
#include <torch/csrc/inductor/cpp_prefix.h>
extern "C"  void  kernel(const double* in_ptr0,
                       const double* in_ptr1,
                       double* out_ptr0,
                       double* out_ptr1,
                       double* out_ptr2,
                       double* out_ptr3,
                       double* out_ptr4)
{
    {
        {
            {
                auto tmp0 = in_ptr0[static_cast<int64_t>(0LL)];
                auto tmp1 = in_ptr1[static_cast<int64_t>(0LL)];
                auto tmp4 = in_ptr1[static_cast<int64_t>(9LL)];
                auto tmp7 = in_ptr1[static_cast<int64_t>(18LL)];
                auto tmp10 = in_ptr1[static_cast<int64_t>(27LL)];
                auto tmp2 = std::tanh(tmp1);
                auto tmp3 = double(tmp0 + tmp2);
                auto tmp5 = std::tanh(tmp4);
                auto tmp6 = double(tmp3 + tmp5);
                auto tmp8 = std::tanh(tmp7);
                auto tmp9 = double(tmp6 + tmp8);
                auto tmp11 = std::tanh(tmp10);
                auto tmp12 = double(tmp9 + tmp11);
                out_ptr0[static_cast<int64_t>(0LL)] = tmp12;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr1[static_cast<int64_t>(27LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr1[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr1[static_cast<int64_t>(18LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr2[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr1[static_cast<int64_t>(9LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr3[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
    {
        {
            {
                auto tmp0 = in_ptr1[static_cast<int64_t>(0LL)];
                auto tmp1 = std::tanh(tmp0);
                auto tmp2 = double(tmp1 * tmp1);
                auto tmp3 = static_cast<double>(1.0);
                auto tmp4 = double(tmp3 - tmp2);
                out_ptr4[static_cast<int64_t>(0LL)] = tmp4;
            }
        }
    }
}

// Python bindings to call kernel():
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <sstream>
#include <cstdlib>

#ifndef _MSC_VER
#if __cplusplus < 202002L
// C++20 (earlier) code
// https://en.cppreference.com/w/cpp/language/attributes/likely
#define likely(x)       __builtin_expect(!!(x), 1)
#define unlikely(x)     __builtin_expect(!!(x), 0)
#endif
#else
#define likely(x) (x)
#define unlikely(x) (x)
#endif

// This is defined in guards.cpp so we don't need to import PyTorch headers that are slooow.
// We manually link it below to workaround issues with fbcode build.
static void* (*_torchinductor_pyobject_tensor_data_ptr)(PyObject* obj);

template <typename T> static inline T parse_arg(PyObject* args, size_t n) {
    static_assert(std::is_pointer_v<T>, "arg type must be pointer or long");
    return static_cast<T>(_torchinductor_pyobject_tensor_data_ptr(PyTuple_GET_ITEM(args, n)));
}
template <> inline int64_t parse_arg<int64_t>(PyObject* args, size_t n) {
    auto result = PyLong_AsSsize_t(PyTuple_GET_ITEM(args, n));
    if(unlikely(result == -1 && PyErr_Occurred()))
        throw std::runtime_error("expected int arg");
    return result;
}
template <> inline uintptr_t parse_arg<uintptr_t>(PyObject* args, size_t n) {
    auto result = PyLong_AsVoidPtr(PyTuple_GET_ITEM(args, n));
    if(unlikely(result == reinterpret_cast<void*>(-1) && PyErr_Occurred()))
        throw std::runtime_error("expected int arg");
    return reinterpret_cast<uintptr_t>(result);
}



static PyObject* kernel_py(PyObject* self, PyObject* args) {
    try {
        if(unlikely(!PyTuple_CheckExact(args)))
            throw std::runtime_error("tuple args required");
        if(unlikely(PyTuple_GET_SIZE(args) != 7))
            throw std::runtime_error("requires 7 args");
        kernel(parse_arg<double*>(args, 0), parse_arg<double*>(args, 1), parse_arg<double*>(args, 2), parse_arg<double*>(args, 3), parse_arg<double*>(args, 4), parse_arg<double*>(args, 5), parse_arg<double*>(args, 6)); Py_RETURN_NONE;
    } catch(std::exception const& e) {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    } catch(...) {
        PyErr_SetString(PyExc_RuntimeError, "unhandled error");
        return nullptr;
    }
}

static PyMethodDef py_methods[] = {
    {"kernel", kernel_py, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef py_module =
    {PyModuleDef_HEAD_INIT, "kernel", NULL, -1, py_methods};

PyMODINIT_FUNC PyInit_kernel(void) {
    const char* str_addr = std::getenv("_TORCHINDUCTOR_PYOBJECT_TENSOR_DATA_PTR");
    if(!str_addr) {
        PyErr_SetString(PyExc_RuntimeError, "_TORCHINDUCTOR_PYOBJECT_TENSOR_DATA_PTR must be set");
        return nullptr;
    }
    std::istringstream iss(str_addr);
    uintptr_t addr = 0;
    iss >> addr;
    _torchinductor_pyobject_tensor_data_ptr =
        reinterpret_cast<decltype(_torchinductor_pyobject_tensor_data_ptr)>(addr);
    PyObject* module = PyModule_Create(&py_module);
    if (module == NULL) {
        return NULL;
    }
    #ifdef Py_GIL_DISABLED
        PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED);
    #endif
    return module;
}
