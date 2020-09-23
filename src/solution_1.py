import sympy as sym
import matplotlib.style as mplstl

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

x = 5 + 2 * t + 3 * t**2
v = x.diff(t)
a = v.diff(t)

x_func = sym.lambdify(t, x)
v_func = sym.lambdify(t, v)
a_func = sym.lambdify(t, a)

x_plot = sym.plot(x, (t, 0, 1), axis_center=(0, x_func(0)), show=False)
x_plot.title = 'Зависимость координаты материальной точки x от времени t'
x_plot.xlabel = 't, с'
x_plot.ylabel = 'x, м'
x_plot.show()

v_plot = sym.plot(v, (t, 0, 1), axis_center=(0, v_func(0)), show=False)
v_plot.title = 'Зависимость скорости материальной точки v от времени t'
v_plot.xlabel = 't, с'
v_plot.ylabel = 'v, м/с'
v_plot.show()

a_plot = sym.plot(a, (t, 0, 1), axis_center=(0, a_func(0)), show=False)
a_plot.title = 'Зависимость ускорения материальной точки a от времени t'
a_plot.xlabel = 't, с'
a_plot.ylabel = 'a, м/с^2'
a_plot.show()
