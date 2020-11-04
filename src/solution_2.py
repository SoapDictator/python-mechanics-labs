import sympy as sym
import matplotlib.style as mplstl

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

a = 0.5 * sym.sin(0.25 * t + sym.pi / 3)

a_func = sym.lambdify(t, a)

a_plot = sym.plot(a, (t, 0, 30), 
	show=False)
a_plot.title = 'Зависимость ускорения материальной точки a от времени t'
a_plot.xlabel = 't, с'
a_plot.ylabel = 'a, м/с^2'
a_plot.show()

v = a.integrate(t)

v_func = sym.lambdify(t, v)
v0 = 0.2
C = v0 - v_func(0)

v = v + C

v_plot = sym.plot(v, (t, 0, 30), 
	show=False)
v_plot.title = 'Зависимость скорости материальной точки a от времени t'
v_plot.xlabel = 't, с'
v_plot.ylabel = 'v, м/с'
v_plot.show()
