import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')
m = sym.Symbol('m')

A = 0.01
k = 0.4
m0 = 0.1

# 2

omega = sym.sqrt(k / m)
omega_func = sym.lambdify(m, omega)

x1_1 = sym.cos(t * omega_func(m0))
x1_1_plot = sym.plot(
    x1_1, (t, 0, 6),
    label='m0',
    line_color='b',
    legend=True,
    show=False)

x1_2 = sym.cos(t * omega_func(m0 * 2))
x1_2_plot = sym.plot(
    x1_2, (t, 0, 6),
    label='2*m0',
    line_color='r',
    legend=True,
    show=False)
x1_1_plot.extend(x1_2_plot)

x1_3 = sym.cos(t * omega_func(m0 * 3))
x1_3_plot = sym.plot(
    x1_3, (t, 0, 6),
    label='3*m0',
    line_color='g',
    legend=True,
    show=False)
x1_1_plot.extend(x1_3_plot)

x1_1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x1_1_plot.xlabel = 't, с'
x1_1_plot.ylabel = 'x, м'
x1_1_plot.show()

x = sym.cos(t * omega)
x1_plot3d = symplot.plot3d(
    x, (t, 0, 6), (m, m0, 3 * m0), 
	show=False)
x1_plot3d.title = ('Зависимость координаты материальной точки x '
    'от времени t и массы m')
x1_plot3d.xlabel = 't, с'
x1_plot3d.ylabel = 'm, кг'

x1_plot3d.show()