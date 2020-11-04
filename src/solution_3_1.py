import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

A = 0.01
k = 0.4
m0 = 0.1


# 1
omega0 = sym.sqrt(k / m0)
x = A * sym.cos(t * omega0)

x_plot = sym.plot(x, (t, 0, 6), 
	show=False)
x_plot.title = 'Зависимость координаты материальной точки x от времени t'
x_plot.xlabel = 't, с'
x_plot.ylabel = 'x, м'
x_plot.show()

v = x.diff(t)

v_plot = sym.plot(v, (t, 0, 6), 
	show=False)
v_plot.title = 'Зависимость скорости материальной точки v от времени t'
v_plot.xlabel = 't, с'
v_plot.ylabel = 'v, м/с'
v_plot.show()

a = v.diff(t)

a_plot = sym.plot(a, (t, 0, 6), 
	show=False)
a_plot.title = 'Зависимость ускорения материальной точки a от времени t'
a_plot.xlabel = 't, с'
a_plot.ylabel = 'a, м/с^2'
a_plot.show()