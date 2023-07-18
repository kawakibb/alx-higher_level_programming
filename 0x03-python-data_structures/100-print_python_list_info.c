#include <Pyobj.h>


/**
* print_python_list_info - prints basic phyton list info
* @p: py object
*
**/

void print_python_list_info(PyObject *p)
{
	long int size_list = PyList_Size(p);
	int a;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size_list);
	printf("[*] Allocated = %li\n", object->allocated);
	for (a = 0; a < size_list; a++)
		printf("Element %i: %s\n", a, Py_TYPE(object->ob_item[i])->tp_name);
}
