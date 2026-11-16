#include <Python.h>

static PyObject *square(PyObject *module, PyObject *arg)
{
    (void)module; // This function doesn't need the module object.

    double x = PyFloat_AsDouble(arg);
    if (x == -1.0 && PyErr_Occurred())
    {
        return NULL;
    }

    return PyFloat_FromDouble(x * x);
}

static PyMethodDef methods[] = {
    {"square", square, METH_O, "Return x squared."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "fastmath",
    .m_size = -1,
    .m_methods = methods,
};

PyMODINIT_FUNC PyInit_fastmath(void)
{
    return PyModule_Create(&module);
}