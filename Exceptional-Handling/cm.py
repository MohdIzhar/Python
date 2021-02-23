# class LoggingContextManager:
#     def __enter__(self):
#         # return
#         print("Logging Context Manager.__enter__()")
#         return "You are in a with-block!"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("LoggingContextManager.__exit({}, {}, {})".format(exc_type, exc_val, exc_tb))
#         return 

# Part - 2

# class LoggingContextManager:
#     def __enter__(self):
#         # return
#         print("Logging Context Manager.__enter__()")
#         return "You are in a with-block!"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             print("LoggingContextManager.__exit__: normal exit detected")
#         else:
#             print("LoggingContextManager.__exit__: Exception Detected! type={}, value={}, traceback={})".format(exc_type, exc_val, exc_tb))
#         return 

# Part-3
# import contextlib
# import sys

# @contextlib.contextmanager
# def my_context_manager():
#     # <Enter>
#     print("logging_context_manager: Enter")
#     try:
#         yield "You'r in with-block!"
#         print("logging_context_manager: Normal Exit")
#         # normal exit
#     except Exception:
#         # <Exceptional Exit>
#         print("logging_context_manager: Exceptional Exit", sys.exc_info())
#         # testing exception propagation
#         raise

# # we have implemented now without __enter__ and __exit__ beacuse of decorator

# # with my_context_manager() as x:
# #     # 

# PART - 4

# import contextlib

# @contextlib.contextmanager
# def nest_test(name):
#     print('Entering', name)
#     # yield
#     # this for name bound testing
#     yield name
#     print('Exiting', name)

# PART - 5

import contextlib

@contextlib.contextmanager
def propagator(name, propagate):
    try:
        yield
        print(name, "Exited normally")
    except Exception:
        print(name, "recieved an Exception")
        if propagate:
            raise