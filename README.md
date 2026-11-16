# 211-Checkoff-3

My topic:

Python Libraries Implemented in C: Explore how libraries like NumPy achieve high performance by implementing computationally intensive operations in C. Investigate how Python programs can call functions written in C and why this approach can improve performance.
Things to explore:
Calling C from Python: Write a simple function in C and learn how to call it from Python using a tool such as ctypes.
Compiling C for Use in Python: Explore how C code can be compiled into a shared library that Python can load and use.
How NumPy Works: Investigate how NumPy uses compiled implementations of operations to efficiently process large arrays.
Performance Comparison: Compare the performance of a computation implemented using a Python loop with an equivalent computation performed using NumPy.
Why Use C Extensions? Explore why Python programmers sometimes implement performance-critical operations in C rather than Python.

Experiments I ran:

The first experiment I ran was creating a function in C and calling it from a Python file to see what a method from a library implemented
in C may look like behind the scenes. 

Here is how to set that experiment up: 

<img width="825" height="229" alt="image" src="https://github.com/user-attachments/assets/5f869068-5d4d-4d0b-9f3a-710878af3961" />

<img width="817" height="373" alt="image" src="https://github.com/user-attachments/assets/532ba21d-749b-4d86-8cbf-d0addf6fae9a" />

<img width="820" height="553" alt="image" src="https://github.com/user-attachments/assets/c71db655-3d6b-4e30-862e-2b595501734c" />

<img width="825" height="156" alt="image" src="https://github.com/user-attachments/assets/83eab1ce-7dc4-4391-a764-9d47a70acc26" />

Then the result should be this in your terminal: 

<img width="833" height="166" alt="image" src="https://github.com/user-attachments/assets/eb2ecaff-1198-4afb-96f2-e0539dea9d8d" />

The second experiment I ran was similar to the first, but squaring each element of an array this time.

Here is how to run that experiment: 

<img width="812" height="275" alt="image" src="https://github.com/user-attachments/assets/b4ed0ce1-1cf9-4a89-94b8-0e06fdd4524d" />

<img width="815" height="380" alt="image" src="https://github.com/user-attachments/assets/429a5945-c4a2-4068-96f5-89b2345c88f2" />
<img width="849" height="256" alt="image" src="https://github.com/user-attachments/assets/1bd2a09f-4908-4c40-8ea9-ee07bd103b63" />

<img width="822" height="374" alt="image" src="https://github.com/user-attachments/assets/db403063-9b3a-4150-ac40-484eea779674" />

Then the result should be this in your terminal:

<img width="813" height="144" alt="image" src="https://github.com/user-attachments/assets/8b6ef029-22fc-4df8-96b7-d0cb0c2d2e3e" />

The third experiment I ran was to see how the calls work using a CPython extension instead of ctypes. 
Here is how to run it: 

<img width="795" height="355" alt="image" src="https://github.com/user-attachments/assets/2334af30-6507-4ead-b1b1-8cee4a17ca3a" />

<img width="833" height="343" alt="image" src="https://github.com/user-attachments/assets/2e1f176b-4d81-4e2a-9fe4-99be02042a3f" />

<img width="839" height="441" alt="image" src="https://github.com/user-attachments/assets/79efdd7e-4332-4305-8a71-950e90b5af82" />

Then the result should be this:

<img width="804" height="202" alt="image" src="https://github.com/user-attachments/assets/db3e9e53-f403-42a9-84c4-76e4c0a06349" />


Summary: 
I learned how Ctypes and a CPython Extension can both implement Python libraries in C. Authors can choose which approach to take when implementing
their libraries, and users will have similar experiences regardless of the choice the author makes. Ctypes is a versatile way for calling C functions
in Python, while a CPython Extension gives more control over how the C functions interact with Python. 


Link to presentation slides: 
https://docs.google.com/presentation/d/1burbMSgBWY5OMXmS4DGJg7EMB7wwC5cWxxwqezk1uMg/edit?usp=sharing












